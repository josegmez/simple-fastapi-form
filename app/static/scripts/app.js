const apiUrl = "http://localhost:8000/incidents";

const SEVERITIES = {
  "low": "Baja",
  "medium": "Media",
  "high": "Alta",
}

const STATUSES = {
  "Open": "Abierto",
  "Closed": "Cerrado",
}

document.addEventListener("DOMContentLoaded", () => {
  loadIncidents();

  document.getElementById("incident-form").addEventListener("submit", (event) => {
    event.preventDefault();
    const id = document.getElementById("incident-id").value;
    if (id) {
      updateIncident(id);
    } else {
      createIncident();
    }
  });
});

function loadIncidents() {
  fetch(`${apiUrl}/`)
    .then(response => response.json())
    .then(data => {
      const incidentList = document.getElementById("incident-list");
      incidentList.innerHTML = "";
      if (data.length === 0) {
        incidentList.innerHTML = "<li>No se encontraron incidentes</li>";
      }
      data.forEach(incident => {
        const li = document.createElement("li");
        const date_created = new Date(incident.date_created).toLocaleDateString();

        li.innerHTML = `
                    <div style="display: flex; justify-content: space-between; flex-direction: column;"> 
                    <strong>${incident.title}</strong>
                    <p>${incident.description}</p>
                    <p><strong>Severidad:</strong> ${SEVERITIES[incident.severity]}</p> 
                    <p><strong>Asignado a:</strong> ${incident.assigned_to}</p>
                    <p><strong>Estado:</strong> ${STATUSES[incident.status]}</p>
                    <p><strong>Fecha de creación:</strong> ${date_created}</p>
                    <div>
                    <button onclick="editIncident('${incident.id}')" style="background: #2844a7">Editar</button>
                    <button onclick="deleteIncident('${incident.id}')" style="background: #a72828">Eliminar</button>
                    </div>
                    </div>
                `;
        incidentList.appendChild(li);
      });
    })
    .catch(error => console.error('Error loading incidents:', error));
}

function createIncident() {
  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;
  const severity = document.getElementById("severity").value;
  const assignedTo = document.getElementById("assigned_to").value;

  fetch(`${apiUrl}/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title, description, severity, assigned_to: assignedTo }),
  })
    .then(response => response.json())
    .then(data => {
      loadIncidents();
      clearForm();
    })
    .catch(error => console.error('Error creating incident:', error));
}

function editIncident(id) {
  fetch(`${apiUrl}/${id}`)
    .then(response => response.json())
    .then(incident => {
      document.getElementById("title").value = incident.title;
      document.getElementById("description").value = incident.description;
      document.getElementById("severity").value = incident.severity;
      document.getElementById("assigned_to").value = incident.assigned_to;
      document.getElementById("incident-id").value = id;

      document.getElementById("update-btn").style.display = "inline";
    })
    .catch(error => console.error('Error fetching incident:', error));
}

function updateIncident(id) {
  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;
  const severity = document.getElementById("severity").value;
  const assignedTo = document.getElementById("assigned_to").value;

  fetch(`${apiUrl}/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title, description, severity, assigned_to: assignedTo, status: "Open" }),
  })
    .then(response => response.json())
    .then(data => {
      loadIncidents();
      clearForm();
    })
    .catch(error => console.error('Error updating incident:', error));
}

function deleteIncident(id) {
  fetch(`${apiUrl}/${id}`, {
    method: "DELETE",
  })
    .then(response => {
      if (response.ok) {
        loadIncidents();
      }
    })
    .catch(error => console.error('Error deleting incident:', error));
}

function clearForm() {
  document.getElementById("incident-form").reset();
  document.getElementById("incident-id").value = "";
  document.getElementById("update-btn").style.display = "none";
}
