
[![Formatting with ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Type checking with pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)
[![Security checking with bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

![Backend](https://github.com/informatter/fullstack-fastapi-rag-sample/actions/workflows/backend_ci_cd.yml/badge.svg?branch=develop)

# Backend 🚀

This is the general documentation for the backend and will be updated as the repo progresses.


## Setup

### Python
This project uses Python 3.11.7. Make sure your system supports python 3. 

### Poetry
Make sure poetry is installed in your local development machine. Please see this guide: "https://python-poetry.org/docs/#installation"
and follow the installation steps for your particular OS

### Getting the project

clone the project and then run `poetry init` inside the root directory of the project. This command will create a `pyproject.toml` file and install the necessary dependencies


### Linting and code formatting

**Linting**

Format all files in the current directory (and any subdirectories).
`ruff check .`

Format all files in `/path/to/code` (and any subdirectories).
`ruff check path/to/code/`

Format individual files
`ruff check path/to/file path/to/file path/to/file`

**Formatting**

Format all files in the current directory (and any subdirectories).
`ruff format .`     

Format all files in `/path/to/code` (and any subdirectories).
`ruff format path/to/code/`

Format individual files
`ruff format path/to/file path/to/file path/to/file`

For more info see: "https://github.com/astral-sh/ruff?tab=readme-ov-file#getting-started"

**Type checking**

Format all files in the current directory (and any subdirectories).
`poetry run pyright .`

Format all files in `/path/to/code` (and any subdirectories).
`poetry run pyright path/to/code/`    

Format individual files
`poetry run pyright path/to/file path/to/file path/to/file`

Line-level Diagnostic supression.

`PEP 484` defines a special comment `# type: ignore` that can be used at the end of a line to suppress all diagnostics emitted by a type checker on that line. Pyright supports this mechanism.

Pyright also supports a `# pyright: ignore` comment at the end of a line to suppress all Pyright diagnostics on that line. This can be useful if you use multiple type checkers on your source base and want to limit suppression of diagnostics to Pyright only.

The `# pyright: ignore` comment accepts an optional list of comma-delimited diagnostic rule names surrounded by square brackets. If such a list is present, only diagnostics within those diagnostic rule categories are suppressed on that line. For example, `# pyright: ignore [reportPrivateUsage, reportGeneralTypeIssues]` would suppress diagnostics related to those two categories but no others.

For more information see: [text](https://microsoft.github.io/pyright/#/comments)

**Security scanning**

Format all files in the current directory (and any subdirectories).
`poetry run bandit -r .`

Format all files in `/path/to/code` (and any subdirectories).
`poetry run bandit -r path/to/code/`    

Format individual files
`poetry run bandit -r path/to/file path/to/file path/to/file`

For more info see: [text](https://bandit.readthedocs.io/en/latest/start.html#usage)

Exclusions:

The line can be marked with a # nosec and any results associated with it will not be reported.

For example, although this line may cause Bandit to report a potential security issue, it will not be reported:

`self.process = subprocess.Popen('/bin/echo', shell=True)  # nosec`

For example, this will suppress the report of `B602` and `B607`:

`self.process = subprocess.Popen('/bin/ls *', shell=True)  # nosec B602, B607`

For more info see: [text](https://bandit.readthedocs.io/en/latest/config.html)

## Running tests 🧪
**TBD**

## Running the project


**On UNIX like systems:**

`poetry run env ENV=local uvicorn main:app --reload`
defaults to port 8000

**On Windows:**

In a Powershell terminal run:

`$env:ENV = "local"; poetry run uvicorn main:app --reload`

defaults to port 8000

see `poetry run uvicorn --help` for more options

### Docker 🐋
**Install Docker Desktop**
https://www.docker.com/products/docker-desktop/

**Build the image**

Make sure you are in the same directory as the `Dockerfile`

`docker build -t rag-api:local -f backend.dockerfile .`

The image uses layer caching for the dependencies so it does not re-install the dependencies every time the image is built if they have not changed.


**Run the container**

To run the API service your local environmen without using Docker Compose:

```bash
docker run --platform=linux/amd64 -p 8000:80 --rm --name rag-api-local -e ENV=local --env-file ..\.env.local rag-api:local
```

The API service is now running in your local machine at http://localhost:8000


