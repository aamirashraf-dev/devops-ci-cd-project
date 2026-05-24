# DevOps CI/CD Pipeline Project

A DevOps project demonstrating CI/CD automation using GitHub Actions, Docker, Python Flask, and automated testing.

---

## Tech Stack

- Python
- Flask
- Docker
- GitHub Actions
- Pytest
- Flake8
- Git
- GitHub

---

## Features

- Automated CI/CD pipeline
- Dockerized Flask application
- Automated testing with Pytest
- Linting with Flake8
- GitHub Actions workflow
- Containerized deployment
- Feature branch workflow
- Pull request validation
- Protected main branch

---

## Project Structure

```bash
devops-ci-cd-project/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── tests/
│   └── test_app.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .flake8
```

---

## Run Locally

```bash
docker build -t devops-flask-app .
docker run -p 5000:5000 devops-flask-app
```

Application runs at:

```bash
http://localhost:5000
```

---

## Run Tests

```bash
python -m pytest
```

---

## Run Linter

```bash
python -m flake8 app/
```

---

## CI/CD Pipeline

This project uses GitHub Actions for Continuous Integration.

Pipeline steps:
- Install dependencies
- Run linting with Flake8
- Run automated tests with Pytest
- Build Docker image

---

## Git Workflow

This project follows a professional Git workflow:

- Feature branches
- Pull requests
- Branch protection rules
- Automated CI validation before merge

---

## Future Improvements

- Kubernetes deployment
- Terraform infrastructure
- AWS deployment
- Docker Compose multi-container setup
- Monitoring and logging
