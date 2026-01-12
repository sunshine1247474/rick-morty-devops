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

## 📦 Helm Deployment

### Prerequisites
- Helm 3.x installed
- Kubernetes cluster running

### Install with Helm

```bash
# Install the chart
helm install rick-morty ./helm/rick-morty-api

# Install with custom values
helm install rick-morty ./helm/rick-morty-api --set replicaCount=3

# Upgrade
helm upgrade rick-morty ./helm/rick-morty-api

# Uninstall
helm uninstall rick-morty
```

### Helm Chart Structure

```
helm/rick-morty-api/
├── Chart.yaml          # Chart metadata
├── values.yaml         # Default configuration
└── templates/
    ├── deployment.yaml # Deployment template
    ├── service.yaml    # Service template
    └── ingress.yaml    # Ingress template
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

The project includes a complete CI/CD pipeline that runs automatically on every push to `main`.

### Pipeline Stages

```
┌─────────────────────────────────────────────────────────────────┐
│                    CI/CD Pipeline Flow                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   1. BUILD & TEST                                               │
│   ├── Checkout code                                             │
│   ├── Setup Python 3.11                                         │
│   ├── Install dependencies                                      │
│   ├── Run main.py script                                        │
│   └── Upload CSV artifact                                       │
│                                                                  │
│   2. DOCKER BUILD                                               │
│   ├── Build Docker image                                        │
│   ├── Run container                                             │
│   ├── Test /healthcheck endpoint                                │
│   └── Test /characters endpoint                                 │
│                                                                  │
│   3. KUBERNETES DEPLOY                                          │
│   ├── Create kind cluster                                       │
│   ├── Load Docker image                                         │
│   ├── Apply K8s manifests                                       │
│   ├── Wait for deployment                                       │
│   └── Test endpoints                                            │
│                                                                  │
│   4. HELM LINT                                                  │
│   └── Validate Helm chart                                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### How to See CI/CD in Action

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add CI/CD pipeline and Helm chart"
   git push origin main
   ```

2. **View the Pipeline:**
   - Go to your GitHub repository
   - Click on "Actions" tab
   - Watch the pipeline run!

3. **Manual Trigger:**
   - Go to Actions → CI/CD Pipeline
   - Click "Run workflow"

### Pipeline File Location

```
.github/workflows/ci-cd.yaml
```

---

## 🎯 Complete Exercise Checklist

| Task | Status | File/Location |
|------|--------|---------------|
| ✅ Python Script (CSV output) | Done | `app/main.py` |
| ✅ REST API with Flask | Done | `app/api.py` |
| ✅ /healthcheck endpoint | Done | `app/api.py` |
| ✅ /characters endpoint | Done | `app/api.py` |
| ✅ Dockerfile | Done | `Dockerfile` |
| ✅ Kubernetes Deployment | Done | `yamls/deployment.yaml` |
| ✅ Kubernetes Service | Done | `yamls/service.yaml` |
| ✅ Kubernetes Ingress | Done | `yamls/ingress.yaml` |
| ✅ Helm Chart | Done | `helm/rick-morty-api/` |
| ✅ GitHub Actions CI/CD | Done | `.github/workflows/ci-cd.yaml` |
| ✅ README Documentation | Done | `README.md` |

---

## 👤 Author

DevOps Home Exercise Solution

