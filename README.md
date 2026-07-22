# 🚀 Flask PostgreSQL Todo App on AWS EKS with GitOps

A production-inspired cloud-native Todo application built from scratch using **Flask**, **PostgreSQL**, **Docker**, **Kubernetes**, **Amazon EKS**, **GitHub Actions**, and **ArgoCD** following GitOps principles.

This project demonstrates the complete CI/CD lifecycle—from writing application code to automated deployment on Kubernetes—using modern DevOps practices.

---

## 📌 Project Overview

This project started as a simple Flask Todo application and was progressively containerized, deployed to Kubernetes, and automated using GitOps.

The final architecture includes:

- Flask REST Application
- PostgreSQL Database
- Docker Containers
- Kubernetes Deployments & Services
- Amazon EKS Cluster
- AWS ALB Ingress Controller
- GitHub Actions CI Pipeline
- ArgoCD GitOps Continuous Delivery
- Automatic Rolling Updates using immutable Docker image tags

---

# 🏗️ Architecture

```text
                        Developer
                            │
                     git push (main)
                            │
                            ▼
                  GitHub Repository
                            │
        ┌───────────────────┴───────────────────┐
        │                                       │
        ▼                                       ▼
 GitHub Actions (CI)                      ArgoCD (CD)
        │                                       │
 Build Docker Image                     Watches Git Repository
        │                                       │
 Push Image to Docker Hub              Detects Manifest Changes
        │                                       │
 Update Deployment Manifest                   Sync
        │                                       │
 Commit Updated Manifest                       ▼
        └──────────────► Amazon EKS ◄───────────┘
                              │
                 Kubernetes Rolling Update
                              │
                Flask + PostgreSQL Application
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Backend | Flask, Python |
| Database | PostgreSQL |
| Containerization | Docker |
| Orchestration | Kubernetes |
| Cloud | AWS EKS |
| Storage | Amazon EBS CSI Driver |
| Networking | AWS ALB Ingress Controller |
| CI | GitHub Actions |
| CD | ArgoCD |
| GitOps | ArgoCD + GitHub |
| Version Control | Git |

---

# 📁 Repository Structure

```text
.
├── app/
│   ├── app.py
│   ├── templates/
│   └── requirements.txt
│
├── k8s/
│   ├── app/
│   ├── database/
│   ├── ingress/
│   ├── namespace.yaml
│   └── kustomization.yaml
│
├── Dockerfile
├── docker-compose.yml
│
└── .github/
    └── workflows/
        └── docker-build.yml
```

---

# ⚙️ Features

- Flask Todo CRUD application
- PostgreSQL persistent storage
- Dockerized application
- Kubernetes Deployments & Services
- Health checks (Liveness & Readiness Probes)
- Persistent Volumes using Amazon EBS
- AWS Application Load Balancer Ingress
- Automated Docker image builds
- Immutable Docker image versioning (`v001`, `v002`, ...)
- GitOps deployment with ArgoCD
- Automatic rolling updates
- Self-healing Kubernetes deployment

---

# 🚀 CI/CD Pipeline

## Continuous Integration (GitHub Actions)

Every push to the `main` branch automatically:

- Builds the Docker image
- Creates a version tag (`v001`, `v002`, ...)
- Pushes the image to Docker Hub
- Updates the Kubernetes Deployment manifest
- Commits the updated manifest back to GitHub

---

## Continuous Delivery (ArgoCD)

ArgoCD continuously watches the Git repository.

Whenever the Deployment manifest changes:

- Detects drift
- Synchronizes Kubernetes manifests
- Performs Rolling Update
- Keeps the cluster synchronized with Git

No manual `kubectl apply` is required.

---

# 🔄 GitOps Workflow

```text
Developer

git push
    │
    ▼
GitHub Actions
    │
Build Docker Image
    │
Push Docker Image
    │
Update deployment.yaml
    │
Commit & Push
    │
    ▼
GitHub Repository
    │
    ▼
ArgoCD detects change
    │
    ▼
Amazon EKS
    │
Rolling Update
```

---

# ☁️ Kubernetes Resources

The application deploys the following Kubernetes resources:

- Namespace
- Deployment (Flask)
- Deployment (PostgreSQL)
- Services
- Persistent Volume Claim
- Secret
- Job (Database Initialization)
- ALB Ingress

---

# ❤️ Health Checks

The application uses Kubernetes probes for high availability.

### Liveness Probe

```text
GET /health
```

Ensures unhealthy containers are restarted.

### Readiness Probe

```text
GET /health
```

Ensures traffic is routed only to healthy Pods.

---

# 📦 Docker Image Versioning

Instead of using `latest`, every deployment uses immutable version tags.

Example:

```
v001
v002
v003
v004
...
```

Benefits:

- Easy rollback
- Deployment traceability
- Immutable releases
- GitOps friendly

---

# 📊 Deployment Workflow

```text
Code Change

↓

Git Push

↓

GitHub Actions

↓

Docker Hub

↓

Update Manifest

↓

GitHub

↓

ArgoCD

↓

Amazon EKS

↓

Rolling Deployment
```

---

# 📷 Screenshots

Add screenshots here:

- Flask Application
- GitHub Actions Workflow
- Docker Hub Image Tags
- ArgoCD Dashboard
- AWS Load Balancer
- EKS Pods

---

# 🧠 Key Learnings

Through this project I gained hands-on experience with:

- Containerizing Python applications
- Kubernetes architecture
- Persistent storage using Amazon EBS
- Kubernetes health probes
- Kubernetes Jobs
- AWS Application Load Balancer
- GitHub Actions CI pipelines
- GitOps workflow
- ArgoCD continuous deployment
- Kubernetes rolling deployments
- Infrastructure troubleshooting
- Kubernetes manifest management with Kustomize

---

# 🚀 Future Improvements

- HTTPS using AWS Certificate Manager
- Prometheus Monitoring
- Grafana Dashboards
- Horizontal Pod Autoscaler
- AWS Secrets Manager Integration
- External Secrets Operator
- Multi-environment Kustomize overlays
- Terraform Infrastructure Automation

---

# 📚 References

- Kubernetes Documentation
- ArgoCD Documentation
- AWS EKS Documentation
- GitHub Actions Documentation
- Docker Documentation

---

# 👨‍💻 Author

**Krutik Ukunde**

Cloud Infrastructure & DevOps Engineer

- AWS Certified Solutions Architect – Associate
- Kubernetes Enthusiast
- Passionate about Cloud, DevOps, SRE & Platform Engineering

GitHub: https://github.com/Krutik2710

LinkedIn: https://www.linkedin.com/in/krutik-ukunde/

---

## ⭐ If you found this project helpful, consider giving it a star!
