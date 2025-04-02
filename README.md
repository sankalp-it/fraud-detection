# 🛡️ Fraud Detection DevOps/MLOps Platform

![System Architecture](system_architecture.png)

This project is an end-to-end implementation of a scalable, developer-friendly, shelf-ready DevOps platform for fraud detection, including model training, real-time inference, GitOps, CI/CD, observability, and security integrations.

...

(Truncated here for brevity — full content will match the rich README previously generated.)
This project is an end-to-end implementation of a scalable, developer-friendly, shelf-ready DevOps platform for fraud detection, including model training, real-time inference, GitOps, CI/CD, observability, and security integrations.

---

## 🚀 Features

### ✅ Model Training & Inference
- `train_model.py` to generate synthetic fraud detection data and train a RandomForest model
- `FastAPI` app to serve model predictions via REST endpoint

### 🐳 Local Testing
- `docker-compose.yml` to bring up FastAPI service, Kafka, and Kafka consumer locally

### ☁️ Cloud Infrastructure (Terraform)
- Modular Terraform code for:
  - VPC & Subnets
  - EKS Cluster
  - IAM Roles
  - S3 Bucket
  - ArgoCD
  - Vault
- `user_data.sh` for EC2 bootstrap (optional legacy path)

### ☸️ Kubernetes Deployments
- Raw Kubernetes manifests (`k8s/manifests/`)
- Helm chart for model-service (`k8s/helm-chart/`)
- Kustomize support with base + prod overlay (`k8s/kustomize/`)

### 🤖 GitOps & CI/CD
- ArgoCD application manifest (`argocd-app.yaml`)
- GitHub Actions pipeline for Docker build & push

### 🔐 Secret Management
- Vault configuration (`vault/`)
- Vault agent injector with sidecar for K8s
- Example annotations to fetch secrets from Vault

### 📊 Observability Stack
- Helm chart for full observability stack (`k8s/helm-observability/`)
  - Prometheus
  - Grafana
  - FluentD
  - Elasticsearch
  - Kibana
- Grafana Dashboard JSON and Alert rules

---

## 📂 Project Structure

```
fraud_detection_project_v1/
├── app/                         # FastAPI app
├── terraform/                   # Modular infrastructure setup
├── k8s/
│   ├── manifests/               # Raw K8s YAML files
│   ├── helm-chart/             # Helm chart for model-service
│   ├── helm-observability/     # Helm chart for observability stack
│   └── kustomize/              # Kustomize base and overlays
├── vault/                      # Vault policies and injector configs
├── observability/              # Grafana dashboards and alert rules
├── kafka_consumer.py           # Kafka consumer to call model-service
├── train_model.py              # Train and export model.joblib
├── Dockerfile
├── docker-compose.yml
├── .github/workflows/          # GitHub Actions CI/CD
├── system_architecture.png     # Architecture diagram
├── README.md
└── DEPLOYMENT_CHECKLIST.md
```

---

## 🧪 Quick Start

### 📦 Local (Docker Compose)
```bash
python train_model.py
docker-compose up --build
```

### ☸️ Terraform (EKS)
```bash
cd terraform
terraform init
terraform apply
```

### 🤖 GitOps
- Deploy ArgoCD
- Apply `argocd-app.yaml` to auto-sync K8s manifests or Helm chart

### 🛡️ Vault
```bash
vault server -dev &
vault kv put secret/model-service/api-key value=supersecretkey
```

---

## 🧰 Dashboard Access

- **Grafana**: `http://<grafana-service-ip>:3000`
- **Kibana**: `http://<kibana-service-ip>:5601`

> Dashboards and alerts are auto-provisioned via sidecar config

---

## 🤝 Contributions

PRs welcome! This repo demonstrates the convergence of ML, DevOps, GitOps, and Platform Engineering principles.

---

## 🧠 Author & License
Praveen Sankuratri
MIT License.