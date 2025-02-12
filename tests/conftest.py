import pytest

from app.boat import RowingBoat


@pytest.fixture
def boat():
    return RowingBoat()
