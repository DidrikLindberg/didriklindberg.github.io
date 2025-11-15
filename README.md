# Python Web Development Boilerplate

A modern Python web development boilerplate using Flask, designed with best practices for building scalable web applications.

## Features

- **Flask Framework**: Lightweight and flexible web framework
- **Modular Architecture**: Well-organized project structure with blueprints
- **Configuration Management**: Environment-based configuration with dotenv
- **Database Ready**: SQLAlchemy integration with Flask-Migrate
- **Docker Support**: Containerization with Docker and Docker Compose
- **Testing**: Pytest setup with fixtures and coverage reporting
- **Code Quality**: Pre-commit hooks, Black, Flake8, isort, mypy
- **API Ready**: RESTful API structure with sample endpoints
- **CORS Support**: Cross-Origin Resource Sharing enabled

## Project Structure

```
.
├── app/
│   ├── __init__.py          # Application factory
│   ├── api/                 # API blueprints
│   │   ├── __init__.py
│   │   └── routes.py        # API routes
│   ├── models/              # Database models
│   ├── services/            # Business logic
│   ├── static/              # Static files (CSS, JS, images)
│   └── templates/           # HTML templates
├── config/
│   ├── __init__.py
│   └── settings.py          # Configuration classes
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Test fixtures
│   └── test_api.py          # API tests
├── .env.example             # Environment variables template
├── .flake8                  # Flake8 configuration
├── .gitignore               # Git ignore rules
├── .pre-commit-config.yaml  # Pre-commit hooks
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Docker image definition
├── pyproject.toml           # Python project configuration
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies
├── run.py                   # Application entry point
└── README.md                # This file
```

## Getting Started

### Prerequisites

- Python 3.11+
- pip
- virtualenv (recommended)
- Docker & Docker Compose (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd website-v1
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

   The application will be available at `http://localhost:5000`

### Using Docker

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Access the application**
   - Application: `http://localhost:5000`
   - PostgreSQL: `localhost:5432`

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_api.py
```

### Code Quality

```bash
# Format code with Black
black .

# Sort imports with isort
isort .

# Lint with Flake8
flake8 .

# Type check with mypy
mypy app/
```

### Pre-commit Hooks

Install pre-commit hooks to automatically check code before commits:

```bash
pre-commit install
```

## API Endpoints

### Health Check
- **GET** `/health` - Application health status

### API Routes
- **GET** `/api/` - API root with version info
- **GET** `/api/hello/<name>` - Sample greeting endpoint

## Configuration

The application supports multiple configuration environments:

- **Development**: Debug mode enabled, SQLite database
- **Production**: Optimized settings, PostgreSQL recommended
- **Testing**: In-memory SQLite database

Configure via environment variables or `config/settings.py`.

## Environment Variables

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
PORT=5000
```

## Database Migrations

```bash
# Initialize migrations
flask db init

# Create migration
flask db migrate -m "Initial migration"

# Apply migration
flask db upgrade
```

## Deployment

### Docker Deployment

```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

### Production Considerations

1. Set `FLASK_ENV=production`
2. Use a strong `SECRET_KEY`
3. Configure a production database (PostgreSQL recommended)
4. Set up reverse proxy (nginx, Apache)
5. Use a WSGI server (gunicorn, uWSGI)
6. Enable HTTPS
7. Set up monitoring and logging

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linters
5. Submit a pull request

## License

This project is open source and available under the MIT License.