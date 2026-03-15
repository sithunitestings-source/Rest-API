# Antigravity REST API

An extremely simple, fast, and production-ready REST API template built with [FastAPI](https://fastapi.tiangolo.com/). It follows the "Antigravity" philosophy of removing boilerplate and keeping things lean, scalable, and easy to deploy.

## Features

- **FastAPI**: High performance, easy to learn, fast to code.
- **CRUD Operations**: Complete Create, Read, Update, Delete for a 'Project' resource.
- **Auto-Documentation**: Built-in Swagger UI and ReDoc.
- **Containerized**: Ready-to-use Dockerfile.
- **Type Hinting**: Fully typed according to PEP8 and modern Python standards.

## Quick Start

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd antigravity-rest-api
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the API
```bash
uvicorn app.main:app --reload
```

### 5. View Documentation
Open your browser and navigate to:
- Swagger UI (Interactive Docs): `http://127.0.0.1:8000/docs`
- ReDoc (Alternative Docs): `http://127.0.0.1:8000/redoc`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Health Check endpoint |
| GET | `/projects` | Get all projects |
| POST | `/projects` | Create a new project |
| GET | `/projects/{id}` | Get a full project by ID |
| PATCH | `/projects/{id}` | Update an existing project |
| DELETE | `/projects/{id}` | Delete a project |

## Deployment

This API is designed to be easily deployed using Docker.

### Render
1. Create a new "Web Service" in Render.
2. Connect your GitHub repository.
3. Select "Docker" as the Environment.
4. Render will automatically detect the `Dockerfile` and deploy the application.

### Railway
1. Click "New Project" in Railway.
2. Select "Deploy from GitHub repo".
3. Railway will automatically build and deploy from the `Dockerfile`.

## Testing
To run the included test suite:
```bash
pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
