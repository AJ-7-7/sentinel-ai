
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def valid_transaction():
    return {
        "account_id": "ACC-1001",
        "merchant": "Amazon",
        "amount": "249.99",
        "currency": "USD",
    }


def test_create_transaction():
    response = client.post(
        "/api/v1/transactions",
        json=valid_transaction(),
    )

    assert response.status_code == 201

    data = response.json()

    assert data["merchant"] == "Amazon"
    assert data["amount"] == "249.99"
    assert "id" in data
    assert "created_at" in data


def test_reject_negative_amount():
    payload = valid_transaction()
    payload["amount"] = "-50.00"

    response = client.post(
        "/api/v1/transactions",
        json=payload,
    )

    assert response.status_code == 422


def test_reject_missing_merchant():
    payload = valid_transaction()
    del payload["merchant"]

    response = client.post(
        "/api/v1/transactions",
        json=payload,
    )

    assert response.status_code == 422


def test_retrieve_transaction():
    created = client.post(
        "/api/v1/transactions",
        json=valid_transaction(),
    )

    assert created.status_code == 201

    transaction_id = created.json()["id"]

    response = client.get(
        f"/api/v1/transactions/{transaction_id}"
    )

    assert response.status_code == 200
    assert response.json()["id"] == transaction_id


def test_unknown_transaction():
    response = client.get(
        "/api/v1/transactions/"
        "00000000-0000-0000-0000-000000000000"
    )

    assert response.status_code == 404
