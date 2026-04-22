# 🚀 Enterprise DevOps Lab: From Bare Metal IaC to Kubernetes

[![CI/CD Pipeline](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange?style=flat-square&logo=github-actions)](https://github.com/Ekzillar/fullstack-deployment-lab/actions)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-blue?style=flat-square&logo=kubernetes)]()
[![Infrastructure as Code](https://img.shields.io/badge/IaC-Ansible-black?style=flat-square&logo=ansible)]()
[![Monitoring](https://img.shields.io/badge/Monitoring-Prometheus%20%7C%20Grafana-red?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Production%20Ready-green?style=flat-square)]()

Комплексный проект по автоматизации инфраструктуры, доставке кода (CI/CD) и оркестрации микросервисов. Проект демонстрирует эволюцию архитектуры: от развертывания на виртуальных машинах (Docker Compose + Ansible) до облачного K8s-кластера.

## 🏗 Архитектура и Технологический стек
- **Frontend**: SPA (HTML/JS) через Nginx
- **Backend**: FastAPI (Python 3.11+)
- **База Данных**: PostgreSQL 15
- **IaC & Automation**: Ansible, Ansible Vault
- **Оркестрация**: Kubernetes (Deployment, Service, Secret) / Docker Compose
- **CI/CD**: GitHub Actions (Self-hosted Runners)
- **Observability**: Prometheus + Grafana + Node Exporter

---

## ☸️ Режим 1: Cloud-Native (Kubernetes)
Приложение разделено на микросервисы и развернуто в локальном кластере K8s.

**Ключевые инженерные решения:**
1. **Separation of Concerns**: Фронтенд (Nginx) и Бэкенд (FastAPI) изолированы в разных подах с собственными деплойментами.
2. **Hybrid Networking**: Настроена маршрутизация между изолированной сетью Minikube и внешней БД (`docker network connect`), имитируя VPC Peering.
3. **Безопасность**: Учетные данные БД передаются через манифесты `Secret` (исключено попадание в Git), настроены политики CORS для API.
4. **Управление трафиком**: Доступ к сервисам реализован через `NodePort`.

*Локальный запуск K8s:*
```bash
kubectl apply -f k8s/db-secret.yaml
kubectl apply -f k8s/
```

---

## 🛠 Режим 2: Bare Metal IaC & CI/CD (Ansible + Docker Compose)
Автоматизация подготовки "голых" Ubuntu-серверов с разделением на **Staging** и **Production**.

### Фаза 1: Infrastructure Provisioning (Ansible)
- Автоматическая установка Docker Engine и зависимостей (Идемпотентный подход).
- Ansible Vault "на лету" расшифровывает пароли и безопасно генерирует `.env`.

*Запуск конфигурации:*
```bash
ansible-playbook -i ansible/hosts.ini ansible/playbook.yml -K -J
```

### Фаза 2: CI/CD Pipeline (GitHub Actions)
- **Build & Push**: Автоматическая сборка образов и пуш в Docker Hub при мердже в `main`.
- **Deploy**: Self-hosted раннеры автоматически раскатывают обновления (сначала Staging, затем Production при успешном прохождении тестов).

---

## 📊 Мониторинг (Observability)
Интегрирован стек мониторинга для отслеживания состояния хостов и контейнеров:
- **Grafana**: `http://<server-ip>:3000` (Дашборды)
- **Prometheus**: `http://<server-ip>:9090` (Сбор метрик)
```