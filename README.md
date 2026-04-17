# 🚀 Fullstack DevOps Lab: FastAPI + Docker + Ansible + CI/CD

[![CI/CD Pipeline](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange?style=flat-square&logo=github-actions)](https://github.com/Ekzillar/fullstack-deployment-lab/actions)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-Images-blue?style=flat-square&logo=docker)](https://hub.docker.com/r/ekzillar/devops-fastapi)
[![Infrastructure as Code](https://img.shields.io/badge/IaC-Ansible-black?style=flat-square&logo=ansible)]()
[![Security](https://img.shields.io/badge/DevSecOps-Ansible%20Vault-lightgrey?style=flat-square&logo=security)]()
[![Status](https://img.shields.io/badge/Status-Production%20Ready-green?style=flat-square)]()

Комплексный проект по автоматизации подготовки инфраструктуры и развертывания веб-приложения с разделением на **Staging** и **Production** окружения. Реализован подход Infrastructure as Code (IaC) и полный цикл доставки (CI/CD) с использованием self-hosted раннеров.

## 🏗 Архитектура системы

Проект развернут на двух изолированных серверах Ubuntu:
* **Staging Server**: Среда для тестирования и проверки интеграции.
* **Production Server**: Стабильная среда для конечных пользователей.

## 🛠 Технологический стек

- **Backend**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL 15 (Alpine)
- **Proxy**: Nginx (Reverse Proxy)
- **Containerization**: Docker & Docker Compose
- **Infrastructure as Code (IaC)**: Ansible
- **Secrets Management**: Ansible Vault
- **CI/CD**: GitHub Actions (Self-hosted Runners)
- **Monitoring**: Prometheus + Grafana + Node Exporter

## 🚀 Как это работает

Процесс разделен на два независимых этапа: подготовка инфраструктуры и доставка кода.

### Фаза 1: Автоматизация инфраструктуры (Ansible)
Перед деплоем кода серверы готовятся автоматически с нуля:
1. Ansible устанавливает Docker Engine и необходимые зависимости.
2. Создается структура директорий для проекта.
3. Ansible Vault "на лету" расшифровывает пароли баз данных и безопасно генерирует файл `.env` на серверах.

### Фаза 2: CI/CD Pipeline (GitHub Actions)
1. **Build**: При каждом пуше в `main` GitHub Actions поднимает временную облачную виртуалку.
2. **Push**: Собирается Docker-образ и отправляется в Docker Hub с тегом `latest`.
3. **Deploy Staging**: Self-hosted раннер скачивает обновление и перезапускает стек на тестовом сервере.
4. **Deploy Production**: Если стейджинг прошел успешно, запускается деплой на боевой сервер.

## ⚙️ Установка и запуск

### 1. Подготовка серверов (Infrastructure Provisioning)
Для настройки "голых" серверов используется Ansible. В репозитории не хранятся открытые пароли, все секреты зашифрованы с помощью Ansible Vault.
```bash
cd ansible
ansible-playbook -i hosts.ini playbook.yml -K -J
```
*(Для запуска потребуется пароль sudo от серверов и мастер-пароль от Vault)*.

### 2. Локальный запуск (Для разработки)
Если вы хотите поднять проект локально без Ansible:
1. Создайте файл `.env` в корне проекта:
   ```env
   DB_USER=your_user
   DB_PASSWORD=your_password
   DB_NAME=your_db
   ```
2. Запустите весь стек одной командой:
   ```bash
   docker-compose up -d
   ```

## 📊 Мониторинг
Система мониторинга доступна по адресам:
- **Grafana**: `http://<server-ip>:3000` (Визуализация метрик)
- **Prometheus**: `http://<server-ip>:9090` (Сбор метрик)
- **API Status**: `http://<server-ip>/docs` (Swagger UI)

---
*Проект выполнен в рамках обучения администрированию инфраструктуры и DevOps-практикам.*