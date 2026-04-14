# 🚀 Fullstack DevOps Lab: FastAPI + Docker + CI/CD

[![CI/CD Pipeline](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange?style=flat-square&logo=github-actions)](https://github.com/Ekzillar/fullstack-deployment-lab/actions)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-Images-blue?style=flat-square&logo=docker)](https://hub.docker.com/r/ekzillar/devops-fastapi)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-green?style=flat-square)]()

Комплексный проект по автоматизации развертывания веб-приложения с разделением на **Staging** и **Production** окружения. Реализован полный цикл доставки (CI/CD) с использованием self-hosted раннеров.

## 🏗 Архитектура системы

Проект развернут на двух изолированных серверах Ubuntu:
* **Staging Server**: Среда для тестирования и проверки интеграции.
* **Production Server**: Стабильная среда для конечных пользователей.

## 🛠 Технологический стек

- **Backend**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL 15 (Alpine)
- **Proxy**: Nginx (Reverse Proxy)
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions (Self-hosted Runners)
- **Monitoring**: Prometheus + Grafana + Node Exporter

## 🚀 Как это работает (CI/CD Pipeline)

1. **Build**: При каждом пуше в `main` GitHub Actions поднимает временную облачную виртуалку.
2. **Push**: Собирается Docker-образ и отправляется в Docker Hub с тегом `latest`.
3. **Deploy Staging**: После успешного билда первый self-hosted раннер скачивает обновление и перезапускает стек на тестовом сервере.
4. **Deploy Production**: Если стейджинг прошел успешно, запускается деплой на боевой сервер.

## ⚙️ Локальный запуск

1. Склонируйте репозиторий:
   ```bash
   git clone [https://github.com/Ekzillar/fullstack-deployment-lab.git](https://github.com/Ekzillar/fullstack-deployment-lab.git)
   ```
2. Создайте файл `.env` на основе примера:
   ```env
   DB_USER=your_user
   DB_PASSWORD=your_password
   DB_NAME=your_db
   ```
3. Запустите весь стек одной командой:
   ```bash
   docker-compose up -d
   ```

## 📊 Мониторинг
Система мониторинга доступна по адресам:
- **Grafana**: `http://<server-ip>:3000` (Визуализация метрик)
- **Prometheus**: `http://<server-ip>:9090` (Сбор метрик)
- **API Status**: `http://<server-ip>/docs` (Swagger UI)

---
*Проект выполнен в рамках обучения администрированию инфраструктуры и DevOps практикам.*
```
