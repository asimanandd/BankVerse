# 🏦 BankVerse

BankVerse is a simple banking system API built with **Python, FastAPI and PostgreSQL**, and progressively transformed into a containerized and Kubernetes-based application using modern DevOps practices.

The project was intentionally built in stages to understand **why each DevOps tool is needed**, rather than adding tools without a practical purpose.

---

## 🚀 Project Overview

BankVerse provides core banking operations such as:

- User registration and authentication
- Automatic bank account creation
- Account balance management
- Deposits
- Withdrawals
- Account-to-account transfers
- Transaction history
- JWT-based authentication
- PostgreSQL database persistence

The application was then progressively DevOpsified using:

- Docker
- Docker Compose
- Kubernetes
- Helm
- GitHub Actions
- GitOps
- Argo CD
- Kubernetes HPA
- NGINX Ingress Controller

---

# 🏗️ Architecture

```text
                         ┌─────────────────┐
                         │     GitHub      │
                         │  Source of Truth│
                         └────────┬────────┘
                                  │
                                  │ Git Push
                                  ▼
                         ┌─────────────────┐
                         │ GitHub Actions  │
                         │       CI        │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │   Helm Chart    │
                         │   Packaging     │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │     Argo CD     │
                         │   GitOps / CD   │
                         └────────┬────────┘
                                  │
                                  ▼
                    ┌──────────────────────────┐
                    │       Kubernetes        │
                    │                          │
                    │  Deployment              │
                    │  Service                 │
                    │  HPA                     │
                    │  Ingress                 │
                    │  Probes                  │
                    │  Resource Management     │
                    └────────────┬─────────────┘
                                 │
                    ┌────────────┼────────────┐
                    ▼            ▼            ▼
                  Pod          Pod          Pod
                    │            │            │
                    └────────────┼────────────┘
                                 │
                                 ▼
                           PostgreSQL