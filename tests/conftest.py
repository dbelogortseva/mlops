import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from mlops_playground.service.app import app

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture()
def good_row():
    return json.loads((ROOT / "good.json").read_text(encoding="utf-8"))
