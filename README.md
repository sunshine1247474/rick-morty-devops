# נ§× Rick and Morty Character Fetcher

![CI/CD Pipeline](https://github.com/sunshine1247474/rick-morty-devops/actions/workflows/ci-cd.yaml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white)

DevOps Home Exercise - Complete CI/CD Pipeline with Monitoring Stack.

## נ—ן¸ Architecture Overview

```
ג”ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”
ג”‚                           MONITORING STACK                                   ג”‚
ג”‚  ג”ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”    ג”‚
ג”‚  ג”‚                                                                      ג”‚    ג”‚
ג”‚  ג”‚   ג”ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”     scrape     ג”ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”                  ג”‚    ג”‚
ג”‚  ג”‚   ג”‚              ג”‚ ג—„ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ ג”‚              ג”‚                  ג”‚    ג”‚
ג”‚  ג”‚   ג”‚   GRAFANA    ג”‚                ג”‚  PROMETHEUS  ג”‚                  ג”‚    ג”‚
ג”‚  ג”‚   ג”‚   :3000      ג”‚  ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג–÷  ג”‚    :9090     ג”‚                  ג”‚    ג”‚
ג”‚  ג”‚   ג”‚              ג”‚    query       ג”‚              ג”‚                  ג”‚    ג”‚
ג”‚  ג”‚   ג””ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”˜                ג””ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”˜                  ג”‚    ג”‚
ג”‚  ג”‚          ג”‚                               ג”‚                          ג”‚    ג”‚
ג”‚  ג”‚          ג”‚ dashboards                    ג”‚ /metrics                 ג”‚    ג”‚
ג”‚  ג”‚          ג–¼                               ג–¼                          ג”‚    ג”‚
ג”‚  ג”‚   ג”ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”   ג”‚    ג”‚
ג”‚  ג”‚   ג”‚                                                             ג”‚   ג”‚    ג”‚
ג”‚  ג”‚   ג”‚                    RICK & MORTY API                         ג”‚   ג”‚    ג”‚
ג”‚  ג”‚   ג”‚                        :5000                                ג”‚   ג”‚    ג”‚
ג”‚  ג”‚   ג”‚                                                             ג”‚   ג”‚    ג”‚
ג”‚  ג”‚   ג”‚   ג”ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”  ג”ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”  ג”ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”          ג”‚   ג”‚    ג”‚
ג”‚  ג”‚   ג”‚   ג”‚ /health    ג”‚  ג”‚/characters ג”‚  ג”‚ /metrics   ג”‚          ג”‚   ג”‚    ג”‚
ג”‚  ג”‚   ג”‚   ג””ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”˜  ג””ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”˜  ג””ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”˜          ג”‚   ג”‚    ג”‚
ג”‚  ג”‚   ג”‚                                                             ג”‚   ג”‚    ג”‚
ג”‚  ג”‚   ג””ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”˜   ג”‚    ג”‚
ג”‚  ג”‚                                                                      ג”‚    ג”‚
ג”‚  ג””ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”˜    ג”‚
ג”‚                                                                              ג”‚
ג””ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”˜
```

## נ“‹ Requirements

Fetch all characters that match:
- **Species**: Human
- **Status**: Alive
- **Origin**: Earth

Output: CSV file with Name, Location, and Image URL.

---

## נ€ Quick Start (Script)

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

## נ³ Docker (REST API Service)

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

## ג˜¸ן¸ Kubernetes Deployment

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

## נ“ Project Structure

```
.
ג”ג”€ג”€ app/
ג”‚   ג”ג”€ג”€ main.py              # Script version (outputs CSV)
ג”‚   ג”ג”€ג”€ api.py               # REST API service + Prometheus metrics
ג”‚   ג””ג”€ג”€ requirements.txt
ג”ג”€ג”€ yamls/
ג”‚   ג”ג”€ג”€ deployment.yaml
ג”‚   ג”ג”€ג”€ service.yaml
ג”‚   ג””ג”€ג”€ ingress.yaml
ג”ג”€ג”€ helm/
ג”‚   ג””ג”€ג”€ rick-morty-api/
ג”‚       ג”ג”€ג”€ Chart.yaml
ג”‚       ג”ג”€ג”€ values.yaml
ג”‚       ג””ג”€ג”€ templates/
ג”ג”€ג”€ monitoring/                    # נ“ Monitoring Stack
ג”‚   ג”ג”€ג”€ prometheus/
ג”‚   ג”‚   ג”ג”€ג”€ prometheus.yml        # Scrape config
ג”‚   ג”‚   ג””ג”€ג”€ alerts.yml            # Alert rules
ג”‚   ג””ג”€ג”€ grafana/
ג”‚       ג””ג”€ג”€ provisioning/
ג”‚           ג”ג”€ג”€ datasources/
ג”‚           ג””ג”€ג”€ dashboards/
ג”ג”€ג”€ .github/
ג”‚   ג””ג”€ג”€ workflows/
ג”‚       ג””ג”€ג”€ ci-cd.yaml           # GitHub Actions pipeline
ג”ג”€ג”€ docker-compose.yaml           # Full stack with monitoring
ג”ג”€ג”€ Dockerfile
ג””ג”€ג”€ README.md
```

---

## נ“ Notes

- The script handles **pagination** automatically (the API returns ~800+ characters across multiple pages)
- Origin filter uses `contains 'Earth'` to catch variations like "Earth (C-137)", "Earth (Replacement Dimension)", etc.

---

## נ“¦ Helm Deployment

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
ג”ג”€ג”€ Chart.yaml          # Chart metadata
ג”ג”€ג”€ values.yaml         # Default configuration
ג””ג”€ג”€ templates/
    ג”ג”€ג”€ deployment.yaml # Deployment template
    ג”ג”€ג”€ service.yaml    # Service template
    ג””ג”€ג”€ ingress.yaml    # Ingress template
```

---

## נ”„ CI/CD Pipeline (GitHub Actions)

The project includes a complete CI/CD pipeline that runs automatically on every push to `main`.

### Pipeline Stages

```
ג”ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”
ג”‚                    CI/CD Pipeline Flow                          ג”‚
ג”ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”₪
ג”‚                                                                  ג”‚
ג”‚   1. BUILD & TEST                                               ג”‚
ג”‚   ג”ג”€ג”€ Checkout code                                             ג”‚
ג”‚   ג”ג”€ג”€ Setup Python 3.11                                         ג”‚
ג”‚   ג”ג”€ג”€ Install dependencies                                      ג”‚
ג”‚   ג”ג”€ג”€ Run main.py script                                        ג”‚
ג”‚   ג””ג”€ג”€ Upload CSV artifact                                       ג”‚
ג”‚                                                                  ג”‚
ג”‚   2. DOCKER BUILD                                               ג”‚
ג”‚   ג”ג”€ג”€ Build Docker image                                        ג”‚
ג”‚   ג”ג”€ג”€ Run container                                             ג”‚
ג”‚   ג”ג”€ג”€ Test /healthcheck endpoint                                ג”‚
ג”‚   ג””ג”€ג”€ Test /characters endpoint                                 ג”‚
ג”‚                                                                  ג”‚
ג”‚   3. KUBERNETES DEPLOY                                          ג”‚
ג”‚   ג”ג”€ג”€ Create kind cluster                                       ג”‚
ג”‚   ג”ג”€ג”€ Load Docker image                                         ג”‚
ג”‚   ג”ג”€ג”€ Apply K8s manifests                                       ג”‚
ג”‚   ג”ג”€ג”€ Wait for deployment                                       ג”‚
ג”‚   ג””ג”€ג”€ Test endpoints                                            ג”‚
ג”‚                                                                  ג”‚
ג”‚   4. HELM LINT                                                  ג”‚
ג”‚   ג””ג”€ג”€ Validate Helm chart                                       ג”‚
ג”‚                                                                  ג”‚
ג””ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”€ג”˜
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
   - Go to Actions ג†’ CI/CD Pipeline
   - Click "Run workflow"

### Pipeline File Location

```
.github/workflows/ci-cd.yaml
```

---

## נ“ Monitoring Stack (Prometheus + Grafana)

Full observability with Prometheus metrics and beautiful Grafana dashboards!

### נ€ Quick Start - Full Stack with Monitoring

```bash
# Start everything with one command!
docker-compose up -d

# Wait for services to start (about 30 seconds)
sleep 30

# Check services
docker-compose ps
```

### נ Access Points

| Service | URL | Credentials |
|---------|-----|-------------|
| **Rick & Morty API** | http://localhost:5000 | - |
| **Prometheus** | http://localhost:9090 | - |
| **Grafana** | http://localhost:3000 | admin / admin |

### נ“ˆ Grafana Dashboard Features

The pre-configured dashboard includes:


### Grafana Dashboard - Monitoring in Action

![Grafana Dashboard](screenshots/grafana-dashboard.png)

### נ”” Configured Alerts

| Alert | Condition | Severity |
|-------|-----------|----------|
| **APIDown** | Service unreachable for 1m | נ”´ Critical |
| **HighErrorRate** | Error rate > 5% for 2m | נ¡ Warning |
| **SlowResponseTime** | p95 latency > 2s for 5m | נ¡ Warning |
| **HighRequestRate** | > 100 req/s for 2m | נ¡ Warning |

### נ“ Available Metrics

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

### נ§¹ Cleanup

```bash
# Stop and remove all containers
docker-compose down

# Remove volumes (monitoring data)
docker-compose down -v
```

### נ“ Monitoring Stack Structure

```
monitoring/
ג”ג”€ג”€ prometheus/
ג”‚   ג”ג”€ג”€ prometheus.yml        # Scrape configuration
ג”‚   ג””ג”€ג”€ alerts.yml           # Alert rules
ג””ג”€ג”€ grafana/
    ג””ג”€ג”€ provisioning/
        ג”ג”€ג”€ datasources/
        ג”‚   ג””ג”€ג”€ datasources.yml    # Auto-configure Prometheus
        ג””ג”€ג”€ dashboards/
            ג”ג”€ג”€ dashboards.yml     # Dashboard provisioning
            ג””ג”€ג”€ rick-morty-api.json # Pre-built dashboard
```

**Dashboard Features:**
- ג… **API Status** - Real-time UP/DOWN indicator
- נ“ **Request Rate** - Requests per second by endpoint
- ג±ן¸ **Response Time Percentiles** - p50, p95, p99 latency
- נ“ˆ **HTTP Status Codes** - Success/Error distribution
- נ¥§ **Status Code Distribution** - Pie chart visualization
- נ“‹ **Requests by Endpoint** - Count per endpoint table

### How to Access
1. Run `docker-compose up -d`
2. Navigate to http://localhost:3000
3. Login: admin / admin
4. Go to Dashboards ג†’ Rick & Morty API Dashboard

### Prometheus Targets
> Navigate to http://localhost:9090/targets to see scrape status

---

## נ‘₪ Author
Itay Shklyar
DevOps Home Exercise Solution - Complete with CI/CD and Monitoring


