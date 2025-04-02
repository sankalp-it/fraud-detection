# ✅ Fraud Detection Platform v1 – Deployment Checklist

This checklist ensures a smooth local and cloud deployment of the complete shelf-ready DevOps platform.

## 🧪 LOCAL DEVELOPMENT

### 🔧 Setup
- [ ] Install Python 3.9+, Docker, and Docker Compose
- [ ] Clone the repo
- [ ] Run `python train_model.py` to generate `model.joblib`

### 🐳 Docker Compose
- [ ] Run `docker-compose up --build`
- [ ] Confirm the following services are up:
  - Kafka
  - Zookeeper
  - FastAPI (model-service)
  - Kafka Consumer

### 🔁 Validate
- [ ] POST to `http://localhost:8000/predict` with test payload
- [ ] Kafka messages processed and forwarded correctly

## ☁️ TERRAFORM (CLOUD INFRASTRUCTURE)

### Prerequisites
- [ ] AWS CLI authenticated and configured
- [ ] Terraform installed
- [ ] IAM role with EKS, VPC, S3, IAM, and EC2 permissions

### 📦 Terraform Steps
- [ ] Run `terraform init` inside `terraform/`
- [ ] Run `terraform apply` to provision:
  - VPC, Subnets
  - IAM Roles
  - EC2 (optional)
  - EKS Cluster
  - ArgoCD
  - S3 Bucket
  - Vault

## ☸️ KUBERNETES DEPLOYMENT

### Option A: Raw Manifests
- [ ] Apply manifests with `kubectl apply -f k8s/manifests/`

### Option B: Helm Chart
- [ ] Run `helm install model-service ./k8s/helm-chart`

### Option C: Kustomize
- [ ] Run `kubectl apply -k k8s/kustomize/overlays/prod`

## 🤖 GITOPS (ARGOCD)

### Setup
- [ ] Deploy ArgoCD via Terraform or Helm
- [ ] Apply `argocd-app.yaml` to sync from GitHub

### Validate
- [ ] Log into ArgoCD UI
- [ ] Confirm auto-sync is working
- [ ] Validate deployment status and rollout

## 🔐 VAULT INTEGRATION

### Setup
- [ ] Start Vault (in dev or cluster mode)
- [ ] Run `vault-config.sh` to populate secrets
- [ ] Deploy Vault Agent Injector
- [ ] Annotate Pods with secret injection metadata

## 📊 OBSERVABILITY STACK

### Deploy Helm Chart
- [ ] Run `helm install observability ./k8s/helm-observability/`

### Access Dashboards
- [ ] Grafana: `http://<grafana-lb-ip>:3000`
- [ ] Kibana: `http://<kibana-lb-ip>:5601`

### Verify
- [ ] Prometheus is scraping model-service
- [ ] Dashboards are showing metrics
- [ ] Alerts are firing for error rates

## 🔄 CI/CD (GITHUB ACTIONS)

### Setup
- [ ] Set GitHub repo secrets:
  - `DOCKER_USERNAME`
  - `DOCKER_PASSWORD`

### Trigger Pipeline
- [ ] Push to `main` branch
- [ ] Confirm GitHub Actions builds and pushes Docker image

## ✅ Post-Deployment Verification

| Component              | Validation                        |
|------------------------|------------------------------------|
| FastAPI Inference      | `curl /predict` working           |
| Kafka Consumer         | Processing messages successfully   |
| ArgoCD Sync            | Auto-deploys from repo             |
| Vault Secret Injection | Environment variable injected      |
| Grafana Dashboard      | Live metrics appear                |
| Alerts (Grafana)       | Alerts fire on simulated errors    |
