# DevOps CI/CD Pipeline Project

A DevOps project demonstrating CI/CD automation using GitHub Actions, Docker, Docker Compose, Kubernetes, Python Flask, Redis, and automated testing.

---

## Tech Stack

* Python
* Flask
* Docker
* Docker Compose
* Kubernetes
* Redis
* GitHub Actions
* Pytest
* Flake8
* Git
* GitHub

---

## Features

* Automated CI/CD pipeline
* Dockerized Flask application
* Multi-container setup with Docker Compose
* Redis integration
* Automated testing with Pytest
* Linting with Flake8
* GitHub Actions workflow
* Kubernetes deployment
* Feature branch workflow
* Pull request validation
* Protected main branch

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
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
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

## Run with Docker Compose

```bash
docker compose up --build
```

This starts:

* Flask application
* Redis container

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

* Install dependencies
* Run linting with Flake8
* Run automated tests with Pytest
* Build Docker image

---

## Kubernetes

This project includes Kubernetes manifests for container orchestration.

Components:

* Deployment
* Service
* Replica management
* Multi-pod architecture

Commands:

```bash
kubectl apply -f k8s/
kubectl get pods
kubectl get services
```

---

## Git Workflow

This project follows a professional Git workflow:

* Feature branches
* Pull requests
* Branch protection rules
* Automated CI validation before merge

---

## Future Improvements

* Terraform infrastructure
* AWS deployment
* Monitoring and logging
* Helm charts

```
```
