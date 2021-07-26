"""
Instalar pelo cmd: pip3 install pytest-ordering
"""

import pytest


@pytest.fixture()
def setUp():
    print("Running conftest method setUp")
    yield
    print("Running conftest method tearDown")


@pytest.fixture(scope="module")
def oneTimeSetUp():
    print("Running conftest one time setUp")
    yield
    print("Running conftest one time tearDown")