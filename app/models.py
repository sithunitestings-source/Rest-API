from typing import Dict, Any, Optional

class Database:
    """
    In-memory database for extreme simplicity and speed.
    In a real production environment, this would be backed by an ORM like SQLAlchemy
    and a real persistence layer like PostgreSQL.
    """
    def __init__(self):
        self.projects: Dict[int, Any] = {}
        self._id_counter: int = 1

    def get_all(self) -> list:
        return list(self.projects.values())

    def get_by_id(self, project_id: int) -> Optional[dict]:
        return self.projects.get(project_id)

    def create(self, project_data: dict) -> dict:
        project_id = self._id_counter
        project = {**project_data, "id": project_id}
        self.projects[project_id] = project
        self._id_counter += 1
        return project

    def update(self, project_id: int, project_data: dict) -> Optional[dict]:
        if project_id in self.projects:
            self.projects[project_id].update(project_data)
            return self.projects[project_id]
        return None

    def delete(self, project_id: int) -> bool:
        if project_id in self.projects:
            del self.projects[project_id]
            return True
        return False

# Global database instance
db = Database()
