from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_predict():
    client = app.test_client()
    response = client.get("/predict")
    assert response.status_code == 200
