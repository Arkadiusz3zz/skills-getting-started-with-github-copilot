from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_participants():
    """Keep tests isolated by restoring participants lists between tests."""
    # Arrange
    original_state = {name: deepcopy(data["participants"]) for name, data in activities.items()}

    yield

    # Assert cleanup
    for name, data in activities.items():
        data["participants"] = original_state[name]
