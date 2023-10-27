from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_data() -> None:
    """
    Test getting data
    """
    r = client.get("/data")
    assert r.status_code == 200
