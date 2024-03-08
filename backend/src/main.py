from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
from fastapi.responses import JSONResponse
from structlog.stdlib import BoundLogger
import traceback
import sys
import structlog
from uuid import uuid4

from core.config import build_settings, Settings
from core.logging import get_logger
from schemas.errors import ErrorResponse

from api.api_v1.api import api_router

settings: Settings = build_settings()
logger: BoundLogger = get_logger()

app = FastAPI(
    title="RAG Sample 🦙",
    # openapi_url=f"{settings.api_v1_str}/openapi.json",
    openapi_url=f"{'/api/v1'}/openapi.json",
)


def _calculate_process_time(start_time: float) -> float:
    """
    Calculates the total time in milliseconds a request took to process.
    """
    process_time = (time.time() - start_time) * 1000.0
    return round(process_time, 5)


def _set_logging_contextvars(request: Request):
    """
    Sets the loggers context vars so they persist during every application log.
    """

    structlog.contextvars.clear_contextvars()

    reques_id = str(uuid4())
    headers = dict(request.headers)
    url = str(request.url)
    method = request.method
    path = request.url.path
    structlog.contextvars.bind_contextvars(reques_id=reques_id)
    structlog.contextvars.bind_contextvars(headers=headers)
    structlog.contextvars.bind_contextvars(url=url)
    structlog.contextvars.bind_contextvars(method=method)
    if request.query_params:
        path += f"?{request.query_params}"

    structlog.contextvars.bind_contextvars(path=path)


@app.middleware("http")
async def process_requests(request: Request, call_next):
    start_time = time.time()
    _set_logging_contextvars(request)

    try:
        response = await call_next(request)
    # handles internal server errors
    except Exception:
        # Get the exception information
        exc_type, exc_value, _ = sys.exc_info()

        logger.error(
            "internal_server_error",
            data={
                "status": "failed",
                "process_time": f" {_calculate_process_time(start_time)} ms",
                "exception_type": exc_type.__name__,  # pyright: ignore reportOptionalMemberAccess
                "exception_value": exc_value,
                "stack_trace": traceback.format_exc(),
                "status_code": 500,
            },
        )
        return JSONResponse(
            status_code=500,
            content=ErrorResponse(
                error="Internal Server Error", message="An unexpected error occurred."
            ),
        )

    process_time = _calculate_process_time(start_time)
    response.headers["X-Process-Time"] = f"{str(process_time)} ms"
    status_code = response.status_code
    status = "successful" if status_code < 400 else "failed"

    logger.info(
        "response",
        data={
            "process_time": f"{process_time} ms",
            "status": status,
            "status_code": status_code,
        },
    )

    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.api_v1_str)
