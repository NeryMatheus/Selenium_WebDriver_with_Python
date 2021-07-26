import pytest


@pytest.fixture()
def setUp():
    print("Running conftest method setUp")
    yield
    print("Running conftest method tearDown")