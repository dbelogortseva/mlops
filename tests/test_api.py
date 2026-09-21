def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert "model_version" in response.json()


def test_ready(client):
    assert client.get("/ready").status_code == 200


def test_bad_month_is_422(client, good_row):
    response = client.post("/v1/predict", json={**good_row, "month": 13})
    assert response.status_code == 422


def test_garbage_is_422(client, good_row):
    response = client.post("/v1/predict", json={**good_row, "month": "garbage"})
    assert response.status_code == 422


def test_invalid_json_is_422(client):
    response = client.post(
        "/v1/predict",
        content=b"not-json",
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 422


def test_missing_field_is_422(client, good_row):
    row = dict(good_row)
    del row["month"]
    assert client.post("/v1/predict", json=row).status_code == 422


def test_extra_field_is_422(client, good_row):
    response = client.post(
        "/v1/predict",
        json={**good_row, "hacker_field": 1},
    )
    assert response.status_code == 422
