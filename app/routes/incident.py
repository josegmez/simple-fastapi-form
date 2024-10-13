from typing import Any, List

from fastapi import APIRouter, HTTPException

from app.models.incident import Incident

router = APIRouter()


@router.get("/", response_model=List[dict])
def read_incidents(skip: int = 0, limit: int = 100) -> Any:
    """Retrieve incidents."""
    incidents = Incident.get_all_incidents(skip, limit)
    return incidents


@router.get("/{id}", response_model=dict)
def read_incident(id: str) -> Any:
    """Get incident by ID."""
    incident = Incident.get_incident_by_id(id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident


@router.post("/", response_model=dict)
def create_incident(incident_in: dict) -> Any:
    """Create a new incident."""
    return Incident.create_incident(
        incident_in["title"],
        incident_in["description"],
        incident_in["severity"],
        incident_in["assigned_to"],
    )


@router.put("/{id}", response_model=dict)
def update_incident(id: str, incident_in: dict) -> Any:
    """Update an incident."""
    updated_incident = Incident.update_incident(
        id,
        incident_in["title"],
        incident_in["description"],
        incident_in["severity"],
        incident_in["assigned_to"],
        incident_in["status"],
    )
    if not updated_incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return updated_incident


@router.delete("/{id}")
def delete_incident(id: str) -> dict:
    """Delete an incident."""
    result = Incident.delete_incident_by_id(id)
    if result is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    return result
