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
  "count": 109,
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

## ⎈ Helm Chart Deployment

### Prerequisites
- Helm 3.x installed
- Kubernetes cluster (minikube/kind/etc.)

### Chart Structure

```
helm/rick-morty-api/
├── Chart.yaml          # Chart metadata
├── values.yaml         # Default configuration values
└── templates/
    ├── deployment.yaml # Deployment template
    ├── service.yaml    # Service template
    └── ingress.yaml    # Ingress template
```

### Install the Chart

```bash
# Build Docker image first
docker build -t rick-morty-api:latest .

# For minikube - load image
eval $(minikube docker-env)
docker build -t rick-morty-api:latest .

# Install with default values
helm install rick-morty ./helm/rick-morty-api

# Install with custom values
helm install rick-morty ./helm/rick-morty-api \
  --set replicaCount=3 \
  --set image.tag=v1.0.0

# Install with custom values file
helm install rick-morty ./helm/rick-morty-api -f custom-values.yaml
```

### Upgrade the Release

```bash
helm upgrade rick-morty ./helm/rick-morty-api --set replicaCount=5
```

### Uninstall

```bash
helm uninstall rick-morty
```

### Customizable Values

| Parameter | Description | Default |
|-----------|-------------|---------|
| `replicaCount` | Number of replicas | `2` |
| `image.repository` | Docker image name | `rick-morty-api` |
| `image.tag` | Docker image tag | `latest` |
| `service.type` | Kubernetes service type | `ClusterIP` |
| `service.port` | Service port | `80` |
| `ingress.enabled` | Enable ingress | `true` |
| `ingress.host` | Ingress hostname | `rick-morty.local` |
| `resources.requests.memory` | Memory request | `64Mi` |
| `resources.limits.memory` | Memory limit | `128Mi` |

---

## 🔄 CI/CD Pipeline (GitHub Actions)

The project includes a complete CI/CD pipeline that runs on every push to the `main` branch.

### Workflow Location

```
.github/workflows/ci-cd.yaml
```

### Pipeline Jobs

#### Job 1: Build
- ✅ Checkout code
- ✅ Set up Python 3.11
- ✅ Install dependencies
- ✅ Run script and verify CSV output
- ✅ Build Docker image
- ✅ Save image as artifact

#### Job 2: Deploy and Test
- ✅ Create Kubernetes cluster (using Kind)
- ✅ Load Docker image into cluster
- ✅ Deploy application using kubectl
- ✅ Wait for deployment to be ready
- ✅ Test `/healthcheck` endpoint
- ✅ Test `/characters` endpoint
- ✅ Test `/` root endpoint

### Trigger the Workflow

The workflow runs automatically on:
- Push to `main` branch
- Pull requests to `main` branch
- Manual trigger (workflow_dispatch)

### View Workflow Results

1. Go to the repository on GitHub
2. Click on **Actions** tab
3. Select the latest workflow run
4. View logs for each job and step

### Manual Trigger

```bash
# Via GitHub CLI
gh workflow run ci-cd.yaml

# Or via GitHub UI: Actions → CI/CD Pipeline → Run workflow
```

---

## 📁 Project Structure

```
.
├── app/
│   ├── main.py              # Script version (outputs CSV)
│   ├── api.py               # REST API service
│   ├── requirements.txt     # Python dependencies
│   └── output.csv           # Generated output
├── yamls/
│   ├── deployment.yaml      # K8s Deployment manifest
│   ├── service.yaml         # K8s Service manifest
│   └── ingress.yaml         # K8s Ingress manifest
├── helm/
│   └── rick-morty-api/
│       ├── Chart.yaml       # Helm chart metadata
│       ├── values.yaml      # Default values
│       └── templates/       # K8s templates
├── .github/
│   └── workflows/
│       └── ci-cd.yaml       # GitHub Actions pipeline
├── Dockerfile               # Docker build instructions
└── README.md                # This file
```

---

## 📝 Technical Notes

- **Pagination**: The script handles pagination automatically (826 characters across 42 pages)
- **Origin Filter**: Uses `contains 'Earth'` to catch variations like:
  - "Earth (C-137)"
  - "Earth (Replacement Dimension)"
  - "Earth (Evil Rick's Target Dimension)"
- **Health Checks**: Implemented at all levels (Docker, Kubernetes probes)
- **Helm Templating**: All values are configurable via `values.yaml`

---

## 🎯 Exercise Completion Status

| Task | Status |
|------|--------|
| Script (query API, filter, CSV) | ✅ Complete |
| GitHub Repository | ✅ Complete |
| Docker + REST API | ✅ Complete |
| Kubernetes Manifests | ✅ Complete |
| Helm Chart | ✅ Complete |
| GitHub Actions CI/CD | ✅ Complete |

---

## 👤 Author

DevOps Home Exercise Solution
