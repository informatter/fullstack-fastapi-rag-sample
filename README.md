[![Formatting with ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Type checking with pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)
[![Security checking with bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
![Frontend](https://github.com/informatter/fullstack-fastapi-rag-sample/actions/workflows/frontend_ci_cd.yml/badge.svg?branch=develop)
![Backend](https://github.com/informatter/fullstack-fastapi-rag-sample/actions/workflows/backend_ci_cd.yml/badge.svg?branch=develop)

# Sample Retrieval Augmented Generation (RAG) Full Stack Application 🤖 🦙

⚠️ Currently in the process of getting built 🛠️

This repo will be a full stack application which uses RAG for an AI agent to have domain specific knowledge. It currently uses the OpenAI API, but the goal is to have the functionality
to swap it for open source models which can be self hosted. 

### Tech stack:
**backend**
- Python 🐍  3.11.7 
- FastAPI ⚡
- Llama Index 🦙

**tooling**
- auto formatting and linting : [Ruff](https://github.com/astral-sh/ruff)
- data validation :  [pydantic](https://github.com/pydantic/pydantic)
- static type checking :  [pydantic](https://github.com/microsoft/pyright)
- logging: [structlog](https://github.com/hynek/structlog)
- security: [bandit](https://github.com/openstack/bandit)
- testing : [pytest](https://github.com/pytest-dev/pytest)


**frontend**
- Vue 3
- Typescript
- Vite

**Infrastructure**
- **AWS** is currently the cloud provider
- **GitHub Actions** is currently being used for building the CI/CD pipeline. 
- **Docker** is currently being used for containarizing the application
- **Kubernetes** Will be used to orchestrate the containers
- **Terraform** Will be used for infrastructure provisioning


### Auth
Auth0 will be used as the authentication service and JWTs will be used to authenticate the users of the app with the API.


### Usage
[Backend](https://github.com/informatter/fullstack-fastapi-rag-sample/blob/develop/backend/README.md)

[Frontend](https://github.com/informatter/fullstack-fastapi-rag-sample/blob/develop/frontend/README.md)

