# DevOps CI/CD Pipeline Project

A DevOps project demonstrating CI/CD automation using GitHub Actions, Docker, Python Flask, and automated testing.

## Tech Stack

- Python
- Flask
- Docker
- GitHub Actions
- Pytest
- Flake8

## Features

- Automated CI/CD pipeline
- Dockerized Flask application
- Automated testing with Pytest
- Linting with Flake8
- GitHub Actions workflow
- Containerized deployment

## Run Locally

```bash
docker build -t devops-flask-app .
docker run -p 5000:5000 devops-flask-app
```

## Run Tests

```bash
python -m pytest
```

## Run Linter

```bash
python -m flake8 app/
```
## CI/CD Pipeline

This project uses GitHub Actions for Continuous Integration.

Pipeline steps:
- Install dependencies
- Run linting with Flake8
- Run automated tests with Pytest
- Build Docker image

```
Production-style GitHub workflow enabled.