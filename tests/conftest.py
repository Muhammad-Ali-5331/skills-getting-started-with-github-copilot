from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture()
def client():
    original_activities = deepcopy(activities)

    with TestClient(app) as test_client:
        yield test_client

    activities.clear()
    activities.update(deepcopy(original_activities))


@pytest.fixture()
def reset_activities():
    original_activities = deepcopy(activities)

    yield activities

    activities.clear()
    activities.update(deepcopy(original_activities))