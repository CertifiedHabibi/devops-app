import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from app import app

def test_home():
    r = app.test_client().get("/")
    assert r.status_code == 200
    assert b"DevOps App" in r.data

def test_health():
    r = app.test_client().get("/health")
    assert r.get_json() == {"status": "ok"}
