# Rick and Morty Character Fetcher

DevOps Home Exercise - Fetches characters from Rick and Morty API based on specific criteria.

## 📋 Requirements

Fetch all characters that match:
- **Species**: Human
- **Status**: Alive
- **Origin**: Earth

Output: CSV file with Name, Location, and Image URL.

---

## 🚀 Quick Start (Script)

### Prerequisites
- Python 3.8+

### Run the Script

```bash
cd app
pip install -r requirements.txt
python main.py
```

Output will be saved to `output.csv`.

---

## 🐳 Docker (REST API Service)

### Build the Docker Image

```bash
docker build -t rick-morty-api .
```

### Run the Container

```bash
docker run -d -p 5000:5000 --name rick-morty-api rick-morty-api
```

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API documentation |
| `/characters` | GET | Get all filtered characters (JSON) |
| `/healthcheck` | GET | Health check endpoint |
| `/health` | GET | Health check endpoint (alias) |

### Example Usage

```bash
# Health check
curl http://localhost:5000/healthcheck

# Get characters
curl http://localhost:5000/characters
```

### Sample Response

```json
{
  "count": 42,
  "characters": [
    {
      "name": "Rick Sanchez",
      "location": "Citadel of Ricks",
      "image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg"
    }
  ]
}
```

---

## ☸️ Kubernetes Deployment

### Prerequisites
- Minikube or any Kubernetes cluster
- kubectl configured

### Deploy to Kubernetes

```bash
# Build image (for minikube)
eval $(minikube docker-env)
docker build -t rick-morty-api:latest .

# Apply manifests
kubectl apply -f yamls/

# Or apply individually
kubectl apply -f yamls/deployment.yaml
kubectl apply -f yamls/service.yaml
kubectl apply -f yamls/ingress.yaml
```

### Verify Deployment

```bash
kubectl get pods
kubectl get services
kubectl get ingress
```

### Access the Service

```bash
# Port forward for testing
kubectl port-forward service/rick-morty-api-service 8080:80

# Then access
curl http://localhost:8080/characters
```

### For Ingress (add to /etc/hosts)

```
<minikube-ip> rick-morty.local
```

---

## 📁 Project Structure

```
.
├── app/
│   ├── main.py          # Script version (outputs CSV)
│   ├── api.py           # REST API service
│   └── requirements.txt
├── yamls/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── Dockerfile
└── README.md
```

---

## 📝 Notes

- The script handles **pagination** automatically (the API returns ~800+ characters across multiple pages)
- Origin filter uses `contains 'Earth'` to catch variations like "Earth (C-137)", "Earth (Replacement Dimension)", etc.

---

## 👤 Author

DevOps Home Exercise Solution

