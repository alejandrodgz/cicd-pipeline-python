# 🧮 CI/CD Pipeline Python Calculator

A Flask-based web calculator application demonstrating modern CI/CD practices, automated testing, code quality checks, and containerized deployment.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Development](#development)
- [Testing](#testing)
- [CI/CD Pipeline](#cicd-pipeline)
- [Docker Deployment](#docker-deployment)
- [Code Quality](#code-quality)
- [Contributing](#contributing)

## 🎯 Overview

This project is a comprehensive demonstration of modern software development practices using Python and Flask. It implements a simple web-based calculator with a complete CI/CD pipeline including automated testing, code quality checks, security scanning, and containerized deployment.

## ✨ Features

- **Web Calculator**: Clean, responsive web interface for basic arithmetic operations
- **REST API**: Backend API for calculator operations (addition, subtraction, multiplication, division)
- **Automated CI/CD**: Complete GitHub Actions pipeline
- **Code Quality**: Integrated linting, formatting, and static analysis
- **Testing Suite**: Unit tests and acceptance tests with coverage reporting
- **Docker Support**: Containerized application for easy deployment
- **SonarCloud Integration**: Code quality and security analysis

## 🛠 Technology Stack

### Backend
- **Python 3.12**: Programming language
- **Flask**: Web framework for API and web interface
- **Gunicorn**: WSGI HTTP Server for production deployment

### Development & Testing
- **pytest**: Testing framework
- **pytest-cov**: Coverage reporting
- **pytest-html**: HTML test reports
- **Selenium**: Web application testing
- **webdriver-manager**: Browser driver management

### Code Quality
- **Black**: Code formatter
- **Pylint**: Code linter and static analysis
- **Flake8**: Style guide enforcement
- **SonarCloud**: Code quality and security analysis

### DevOps & Deployment
- **Docker**: Containerization
- **GitHub Actions**: CI/CD automation
- **Docker Hub**: Container registry

## 📁 Project Structure

```
cicd-pipeline-python/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD pipeline
├── app/
│   ├── __init__.py
│   ├── app.py                  # Flask application main file
│   ├── calculadora.py          # Calculator logic
│   └── templates/              # HTML templates
├── tests/
│   ├── test_calculadora.py     # Unit tests
│   └── test_acceptance_app.py  # Acceptance tests
├── .dockerignore               # Docker ignore file
├── .gitignore                  # Git ignore file
├── Dockerfile                  # Container definition
├── pytest.ini                 # Pytest configuration
├── requirements.txt            # Python dependencies
├── sonar-project.properties    # SonarCloud configuration
└── README.md                   # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)

### Local Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd cicd-pipeline-python
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python -m flask --app app.app run
   ```

5. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`

## 💻 Development

### Running in Development Mode

```bash
# Enable debug mode
export FLASK_ENV=development
python -m flask --app app.app run --debug
```

### Code Formatting

```bash
# Format code with Black
black app/

# Check formatting
black app/ --check
```

### Code Linting

```bash
# Run Pylint
pylint app/

# Run Flake8
flake8 app/
```

## 🧪 Testing

### Running Unit Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Generate HTML coverage report
pytest --cov=app --cov-report=html
```

### Running Acceptance Tests

```bash
# Start the application first
gunicorn --workers=2 --bind=0.0.0.0:8000 app.app:app &

# Run acceptance tests
pytest tests/test_acceptance_app.py
```

### Test Coverage

The project maintains high test coverage with both unit tests and acceptance tests:
- **Unit Tests**: Test individual calculator functions
- **Acceptance Tests**: Test the web interface using Selenium
- **Coverage Reporting**: Generates detailed HTML reports

## 🔄 CI/CD Pipeline

The project uses GitHub Actions for automated CI/CD with the following stages:

### Build and Test Stage
1. **Environment Setup**: Python 3.12 environment
2. **Dependency Installation**: Install project dependencies
3. **Code Quality Checks**:
   - Black formatting verification
   - Pylint static analysis
   - Flake8 style enforcement
4. **Testing**:
   - Unit tests with coverage
   - Acceptance tests with Selenium
5. **Quality Analysis**: SonarCloud code quality scan

### Deployment Stage (on main branch)
1. **Docker Image Build**: Multi-platform container creation
2. **Registry Push**: Push to Docker Hub
3. **Artifact Upload**: Test reports and coverage data

### Pipeline Triggers
- **Push to main**: Full pipeline including deployment
- **Pull Requests**: Build and test only
- **Manual Trigger**: Via workflow_dispatch

## 🐳 Docker Deployment

### Building the Docker Image

```bash
# Build the image
docker build -t calculator-app .

# Run the container
docker run -p 8000:8000 calculator-app
```

### Using Docker Compose (if available)

```bash
# Start the application
docker-compose up -d

# Stop the application
docker-compose down
```

### Production Deployment

The application is configured for production deployment using:
- **Gunicorn**: WSGI server for handling multiple requests
- **Multi-worker setup**: Improved performance and reliability
- **Health checks**: Container health monitoring
- **Security**: Non-root user execution

## 📊 Code Quality

### SonarCloud Integration

The project integrates with SonarCloud for:
- **Code Quality**: Maintainability, reliability, and security metrics
- **Test Coverage**: Tracking test coverage trends
- **Security**: Vulnerability detection and remediation
- **Technical Debt**: Code smell identification

### Quality Gates

- **Pylint Score**: Minimum score of 9/10
- **Test Coverage**: Comprehensive test coverage tracking
- **Code Formatting**: Strict adherence to Black formatting
- **Style Compliance**: Flake8 style guide enforcement

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Run tests and quality checks**
   ```bash
   pytest
   black app/ --check
   pylint app/
   flake8 app/
   ```
5. **Commit your changes**
   ```bash
   git commit -m "Add your descriptive commit message"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Maintain test coverage above 80%
- Add unit tests for new functionality
- Update documentation for API changes
- Use meaningful commit messages

## 📈 Monitoring and Metrics

- **GitHub Actions**: Pipeline success/failure rates
- **SonarCloud**: Code quality metrics and trends
- **Test Reports**: Coverage and performance metrics
- **Docker Hub**: Image download statistics

## 📄 License

This project is part of a CI/CD course and is intended for educational purposes.

## 🆘 Support

For questions, issues, or contributions, please:
1. Check existing issues in the repository
2. Create a new issue with detailed description
3. Follow the contributing guidelines for pull requests

---

**Built with ❤️ for learning modern DevOps practices**

te
