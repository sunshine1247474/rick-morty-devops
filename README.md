# 🧪 Rick and Morty Character Fetcher

![CI/CD Pipeline](https://github.com/YOUR-USERNAME/YOUR-REPO/actions/workflows/ci-cd.yaml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white)

DevOps Home Exercise - Complete CI/CD Pipeline with Monitoring Stack.

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           MONITORING STACK                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                                                                      │    │
│  │   ┌──────────────┐     scrape     ┌──────────────┐                  │    │
│  │   │              │ ◄───────────── │              │                  │    │
│  │   │   GRAFANA    │                │  PROMETHEUS  │                  │    │
│  │   │   :3000      │  ───────────►  │    :9090     │                  │    │
│  │   │              │    query       │              │                  │    │
│  │   └──────────────┘                └──────────────┘                  │    │
│  │          │                               │                          │    │
│  │          │ dashboards                    │ /metrics                 │    │
│  │          ▼                               ▼                          │    │
│  │   ┌────────────────────────────────────────────────────────────┐   │    │
│  │   │                                                             │   │    │
│  │   │                    RICK & MORTY API                         │   │    │
│  │   │                        :5000                                │   │    │
│  │   │                                                             │   │    │
│  │   │   ┌────────────┐  ┌────────────┐  ┌────────────┐          │   │    │
│  │   │   │ /health    │  │/characters │  │ /metrics   │          │   │    │
│  │   │   └────────────┘  └────────────┘  └────────────┘          │   │    │
│  │   │                                                             │   │    │
│  │   └────────────────────────────────────────────────────────────┘   │    │
│  │                                                                      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

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
│   ├── main.py              # Script version (outputs CSV)
│   ├── api.py               # REST API service + Prometheus metrics
│   └── requirements.txt
├── yamls/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── helm/
│   └── rick-morty-api/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
├── monitoring/                    # 📊 Monitoring Stack
│   ├── prometheus/
│   │   ├── prometheus.yml        # Scrape config
│   │   └── alerts.yml            # Alert rules
│   └── grafana/
│       └── provisioning/
│           ├── datasources/
│           └── dashboards/
├── .github/
│   └── workflows/
│       └── ci-cd.yaml           # GitHub Actions pipeline
├── docker-compose.yaml           # Full stack with monitoring
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

## 📊 Monitoring Stack (Prometheus + Grafana)

Full observability with Prometheus metrics and beautiful Grafana dashboards!

### 🚀 Quick Start - Full Stack with Monitoring

```bash
# Start everything with one command!
docker-compose up -d

# Wait for services to start (about 30 seconds)
sleep 30

# Check services
docker-compose ps
```

### 🌐 Access Points

| Service | URL | Credentials |
|---------|-----|-------------|
| **Rick & Morty API** | http://localhost:5000 | - |
| **Prometheus** | http://localhost:9090 | - |
| **Grafana** | http://localhost:3000 | admin / admin |

### 📈 Grafana Dashboard Features

The pre-configured dashboard includes:


### Grafana Dashboard - Monitoring in Action

![Grafana Dashboard](screenshots/grafana-dashboard.png)

### 🔔 Configured Alerts

| Alert | Condition | Severity |
|-------|-----------|----------|
| **APIDown** | Service unreachable for 1m | 🔴 Critical |
| **HighErrorRate** | Error rate > 5% for 2m | 🟡 Warning |
| **SlowResponseTime** | p95 latency > 2s for 5m | 🟡 Warning |
| **HighRequestRate** | > 100 req/s for 2m | 🟡 Warning |

### 📊 Available Metrics

The API exposes Prometheus metrics at `/metrics`:

```bash
# View raw metrics
curl http://localhost:5000/metrics
```

**Key Metrics:**
- `flask_http_request_total` - Total HTTP requests by endpoint, method, status
- `flask_http_request_duration_seconds` - Request latency histogram
- `flask_http_request_exceptions_total` - Total exceptions raised
- `up` - Target availability (1 = up, 0 = down)

### 🧹 Cleanup

```bash
# Stop and remove all containers
docker-compose down

# Remove volumes (monitoring data)
docker-compose down -v
```

### 📁 Monitoring Stack Structure

```
monitoring/
├── prometheus/
│   ├── prometheus.yml        # Scrape configuration
│   └── alerts.yml           # Alert rules
└── grafana/
    └── provisioning/
        ├── datasources/
        │   └── datasources.yml    # Auto-configure Prometheus
        └── dashboards/
            ├── dashboards.yml     # Dashboard provisioning
            └── rick-morty-api.json # Pre-built dashboard
```

**Dashboard Features:**
- ✅ **API Status** - Real-time UP/DOWN indicator
- 📊 **Request Rate** - Requests per second by endpoint
- ⏱️ **Response Time Percentiles** - p50, p95, p99 latency
- 📈 **HTTP Status Codes** - Success/Error distribution
- 🥧 **Status Code Distribution** - Pie chart visualization
- 📋 **Requests by Endpoint** - Count per endpoint table

### How to Access
1. Run `docker-compose up -d`
2. Navigate to http://localhost:3000
3. Login: admin / admin
4. Go to Dashboards → Rick & Morty API Dashboard

### Prometheus Targets
> Navigate to http://localhost:9090/targets to see scrape status

---

## 👤 Author

DevOps Home Exercise Solution - Complete with CI/CD and Monitoring

