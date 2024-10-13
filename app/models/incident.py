import uuid
from datetime import datetime

from tinydb import Query, TinyDB

# Inicializa TinyDB
db = TinyDB("db.json")
IncidentQuery = Query()


class Incident:
    def __init__(self, title: str, description: str, severity: str, assigned_to: str):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.severity = severity
        self.status = "Open"  # Estado inicial
        self.date_created = datetime.now().isoformat()
        self.assigned_to = assigned_to
        self.resolved_date = None

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "severity": self.severity,
            "status": self.status,
            "date_created": self.date_created,
            "assigned_to": self.assigned_to,
            "resolved_date": self.resolved_date,
        }

    @staticmethod
    def from_dict(data):
        incident = Incident(
            data["title"], data["description"], data["severity"], data["assigned_to"]
        )
        incident.id = data["id"]
        incident.status = data["status"]
        incident.date_created = data["date_created"]
        incident.resolved_date = data.get("resolved_date")
        return incident

    @classmethod
    def create_incident(
        cls, title: str, description: str, severity: str, assigned_to: str
    ):
        incident = cls(title, description, severity, assigned_to)
        db.insert(incident.to_dict())
        return incident.to_dict()

    @classmethod
    def get_incident_by_id(cls, id: str):
        incident = db.search(IncidentQuery.id == id)
        return incident[0] if incident else None

    @classmethod
    def update_incident(
        cls,
        id: str,
        title: str,
        description: str,
        severity: str,
        assigned_to: str,
        status: str,
    ):
        incident = db.search(IncidentQuery.id == id)
        if not incident:
            return None
        db.update(
            {
                "title": title,
                "description": description,
                "severity": severity,
                "assigned_to": assigned_to,
                "status": status,
            },
            IncidentQuery.id == id,
        )
        return db.search(IncidentQuery.id == id)[0]

    @classmethod
    def delete_incident_by_id(cls, id: str):
        incident = db.search(IncidentQuery.id == id)
        if not incident:
            return None
        db.remove(IncidentQuery.id == id)
        return {"message": "Incident deleted successfully"}

    @classmethod
    def get_all_incidents(cls, skip: int = 0, limit: int = 100):
        incidents = db.all()
        return incidents[skip : skip + limit]
