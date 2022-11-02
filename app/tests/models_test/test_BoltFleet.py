import pytest
from app.models import BoltFleet


@pytest.fixture
def test_BoltFleet(db) -> BoltFleet:
    return BoltFleet.objects.create(name='bolt')


def test_db(test_BoltFleet):
    assert BoltFleet.objects.filter(name='bolt').exists()
    assert BoltFleet.objects.filter(name='bolt').exists()