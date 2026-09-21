# MLOps Playground

## Проверка

Требуются `uv`, Docker, `kind` и `kubectl`.

```powershell
uv run pytest
docker compose up -d --build
if (-not ((kind get clusters) -contains "mlops-playground")) { kind create cluster --name mlops-playground }; kind load docker-image mlops-playground:1.0 --name mlops-playground; kubectl apply -f k8s; kubectl rollout status deployment/mlops-api --timeout=120s
```

## Результаты

### Тесты

![Результат pytest](screenshots/pytest.png)

### Логи запросов в PostgreSQL

![SELECT из таблицы predictions](screenshots/postgres.png)

### Kubernetes и ответ модели

![Две реплики и predict через port-forward](screenshots/kubernetes.png)

### Поды в k9s

![Поды в k9s](screenshots/k9s.png)
