# FastAPI application with CI pipeline

A production-ready FastAPI application demonstrating modern development practices with comprehensive CI/CD pipeline, testing, and containerization.

## ✨ Features

- **FastAPI** with async/await support
- **Pydantic V2** for data validation and settings management
- **Comprehensive testing** with pytest and coverage reporting
- **GitHub Actions CI/CD** with multi-Python version testing
- **Docker** with optimized builds and security best practices
- **Code quality tools** (Black, Flake8, MyPy, Bandit)
- **Security middleware** (CORS, TrustedHost)
- **Request logging** and error handling
- **Health checks** for monitoring

## 🚀 Quick Start

### Prerequisites
- Python 3.11+ 
- Docker (optional)

### Local Development

1. **Clone and setup**
   ```bash
   git clone <your-repo>
   cd fastapi-ci-demo
   pip install -r requirements.txt
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

3. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Visit the API**
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - Health check: http://localhost:8000/health

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test class
pytest tests/test_main.py::TestEchoEndpoint -v
```

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Root status endpoint |
| `GET` | `/health` | Health check with timestamp |
| `POST` | `/echo` | Echo message with validation |
| `GET` | `/version` | Application version info |
| `GET` | `/error` | Simulate error (for testing) |

### Example Usage

```bash
# Health check
curl http://localhost:8000/health

# Echo message
curl -X POST http://localhost:8000/echo \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, World!"}'
```

## 🐳 Docker

### Build and run with Docker

```bash
# Build image
docker build -t fastapi-ci-demo .

# Run container
docker run -p 8000:8000 fastapi-ci-demo

# Run with environment file
docker run -p 8000:8000 --env-file .env fastapi-ci-demo
```

## 🔄 CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) provides:

### **Testing Stage**
- ✅ Multi-Python version testing (3.11, 3.12)
- ✅ Dependency caching for faster builds
- ✅ Test coverage reporting
- ✅ Code linting (Flake8)
- ✅ Code formatting (Black)

### **Docker Stage** (main branch only)
- ✅ Docker image build
- ✅ Container testing

### **Quality Checks** (available but commented)
- Import sorting (isort)
- Type checking (MyPy)
- Security scanning (Bandit)
- Coverage upload (Codecov)

## ⚙️ Configuration

Configuration is managed through environment variables using Pydantic Settings:

```bash
# .env file
APP_NAME=FastAPI CI Demo
APP_VERSION=1.0.0
DEBUG=false
HOST=0.0.0.0
PORT=8000
LOG_LEVEL=INFO
SECRET_KEY=your-super-secret-key
```

## 🛠️ Development Tools

### Code Quality
```bash
# Format code
black app tests

# Lint code
flake8 app tests

# Sort imports
isort app tests

# Type checking
mypy app

# Security scan
bandit -r app
```

### Pre-commit hooks
```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## 📁 Project Structure

```
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   └── config.py        # Configuration management
├── tests/
│   ├── __init__.py
│   └── test_main.py     # Comprehensive test suite
├── .github/workflows/
│   └── ci.yml           # GitHub Actions pipeline
├── Dockerfile           # Multi-stage Docker build
├── requirements.txt     # Python dependencies
├── .env.example         # Environment template
└── README.md
```

## 🚦 Production Readiness

This application includes production-ready features:

- **Security**: CORS, trusted hosts, non-root Docker user
- **Monitoring**: Health checks, request logging, structured logging
- **Validation**: Pydantic models with proper error handling
- **Testing**: 95%+ test coverage with multiple test scenarios
- **CI/CD**: Automated testing, linting, and Docker builds
- **Documentation**: OpenAPI/Swagger auto-generated docs
