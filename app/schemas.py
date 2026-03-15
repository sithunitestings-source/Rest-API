from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from enum import Enum

class ProjectStatus(str, Enum):
    active = "active"
    completed = "completed"
    archived = "archived"

class ProjectBase(BaseModel):
    title: str = Field(..., title="Title of the project")
    description: Optional[str] = Field(None, title="Description of the project")
    status: ProjectStatus = Field(default=ProjectStatus.active, title="Project status")

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ProjectStatus] = None

class ProjectResponse(ProjectBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
