# Production-Ready FastAPI Starter with CI/CD

[![CI Pipeline](https://github.com/berkecengiz/fastapi-github-actions-ci-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/berkecengiz/fastapi-github-actions-ci-demo/actions/workflows/ci.yml)
[![Code Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/berkecengiz/fastapi-github-actions-ci-demo/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository serves as a robust, production-ready starter template for building high-performance APIs with FastAPI. It comes pre-configured with a comprehensive CI/CD pipeline, automated testing, code quality checks, and Docker support to ensure your application is reliable, maintainable, and scalable from day one.

## ✨ Features

* **Modern API Framework**: Built with **FastAPI** for high performance and asynchronous capabilities.
* **Modular Architecture**: Organized using API Routers for a clean and scalable structure.
* **Data Validation**: Leverages **Pydantic V2** for robust data validation and settings management.
* **Containerization**: Multi-stage **Docker** file for creating optimized and lightweight production images.
* **Comprehensive Testing**: Includes a full test suite with **Pytest**, `pytest-cov` for coverage reports, and `pytest-asyncio` for testing async code.
* **Automated CI/CD**: **GitHub Actions** workflow that automatically runs tests, linting, and security scans on every push and pull request.
* **Code Quality Enforcement**: Pre-configured with a suite of tools to maintain high code quality:
    * **Black**: For consistent code formatting.
    * **isort**: For organizing imports.
    * **Flake8**: For linting and style checks.
    * **MyPy**: For static type checking.
    * **Bandit**: For identifying common security issues.
* **Dependency Management**: Simple and effective dependency management using `requirements.txt`.
* **Centralized Configuration**: Easy and secure configuration management using environment variables and `pydantic-settings`.

## 📂 Project Structure

The project follows a modular structure to promote separation of concerns and scalability.

```
.
├── .github/workflows/      # GitHub Actions CI/CD pipeline
│   └── ci.yml
├── app/
│   ├── __init__.py
│   ├── api/                  # API versioning and endpoint aggregation
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── api.py          # Main router for API v1
│   │       └── endpoints/      # Feature-specific routers
│   │           ├── __init__.py
│   │           └── echo.py
│   ├── core/                 # Core application logic and config
│   │   ├── __init__.py
│   │   └── config.py
│   ├── schemas/              # Pydantic models (data schemas)
│   │   ├── __init__.py
│   │   └── echo.py
│   └── main.py               # Main application entry point
├── requirements.txt
├── tests/
│   ├── __init__.py
│   └── test_api/             # Tests organized by feature
│       ├── __init__.py
│       └── test_echo.py
└── Dockerfile
```

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

* Python 3.11+
* Docker (optional, for containerized setup)
* An active internet connection

### 1. Clone the Repository

```bash
git clone [https://github.com/berkecengiz/fastapi-github-actions-ci-demo.git](https://github.com/berkecengiz/fastapi-github-actions-ci-demo.git)
cd fastapi-github-actions-ci-demo
```

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# For Unix/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

Install all the required packages from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

The application uses a `.env` file for configuration. Create one from the example (even though it's empty, it's good practice).

```bash
# This project doesn't require any specific variables to run,
# but you can create the file for future use.
touch .env
```

### 5. Run the Application

You can now run the FastAPI application using `uvicorn`.

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The `--reload` flag will automatically restart the server whenever you make changes to the code.

## 🐳 Running with Docker

You can also build and run the application using Docker for a more isolated environment.

### 1. Build the Docker Image

```bash
docker build -t fastapi-starter .
```

### 2. Run the Docker Container

```bash
docker run -d -p 8000:8000 --name my-fastapi-app fastapi-starter
```

The application will be available at `http://localhost:8000`.

## 🧪 Testing

This project uses `pytest` for testing.

### Run All Tests

To run the complete test suite and see the coverage report in your terminal:

```bash
pytest tests/ --cov=app -v
```

### Generate HTML Coverage Report

For a more detailed, interactive report, generate the HTML version:

```bash
pytest tests/ --cov=app --cov-report=html
```

You can then open `htmlcov/index.html` in your browser.

## 🎨 Code Quality

This starter kit is equipped with several tools to ensure your code stays clean, consistent, and secure.

```bash
# Auto-format code with Black
black .

# Sort imports with isort
isort .

# Check for style issues with Flake8
flake8 .

# Run static type checks with MyPy
mypy .

# Scan for security vulnerabilities with Bandit
bandit -r .
```

## ⚙️ CI/CD Pipeline

The GitHub Actions workflow in `.github/workflows/ci.yml` automates the quality assurance process. It is triggered on every `push` and `pull_request` to the `main` branch and performs the following jobs:

1.  **Lint & Format**: Checks if the code is correctly formatted with `black` and `isort`.
2.  **Security Scan**: Uses `bandit` to scan the code for potential security vulnerabilities.
3.  **Run Tests**: Executes the entire `pytest` suite across multiple Python versions to ensure compatibility. It also uploads the coverage report.
4.  **Build Docker Image**: Builds the production Docker image to ensure the `Dockerfile` is working correctly.

## 📚 API Documentation

Once the application is running, FastAPI provides automatic, interactive API documentation. Note that all endpoints are now prefixed with `/v1`.

* **Swagger UI**: `http://localhost:8000/docs`
* **ReDoc**: `http://localhost:8000/redoc`

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, please open an issue or create a pull request.

1.  Fork the repository.
2.  Create a new feature branch (`git checkout -b feature/amazing-feature`).
3.  Commit your changes (`git commit -m 'Add some amazing feature'`).
4.  Push to the branch (`git push origin feature/amazing-feature`).
5.  Open a pull request.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
