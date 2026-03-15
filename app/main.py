from fastapi import FastAPI, HTTPException, status
from typing import List

from app.schemas import ProjectCreate, ProjectUpdate, ProjectResponse
from app.models import db

app = FastAPI(
    title="Antigravity API",
    description="An extremely simple and fast REST API, built for speed and production readiness.",
    version="1.0.0"
)

@app.get("/", tags=["Root"])
def read_root():
    """Root endpoint welcoming users to the API."""
    return {"message": "Welcome to the Antigravity API! Visit /docs for documentation."}

@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint to ensure API is up and running."""
    return {"status": "ok"}

@app.post("/projects", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED, tags=["Projects"])
def create_project(project: ProjectCreate):
    """Create a new project resource."""
    return db.create(project.model_dump())

@app.get("/projects", response_model=List[ProjectResponse], tags=["Projects"])
def get_projects():
    """Retrieve all project resources."""
    return db.get_all()

@app.get("/projects/{project_id}", response_model=ProjectResponse, tags=["Projects"])
def get_project(project_id: int):
    """Retrieve a single project resource by ID."""
    project = db.get_by_id(project_id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project

@app.patch("/projects/{project_id}", response_model=ProjectResponse, tags=["Projects"])
def update_project(project_id: int, project_update: ProjectUpdate):
    """Update an existing project by ID."""
    existing_project = db.get_by_id(project_id)
    if not existing_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    
    update_data = project_update.model_dump(exclude_unset=True)
    updated_project = db.update(project_id, update_data)
    return updated_project

@app.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Projects"])
def delete_project(project_id: int):
    """Delete a project by ID."""
    if not db.delete(project_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return None
