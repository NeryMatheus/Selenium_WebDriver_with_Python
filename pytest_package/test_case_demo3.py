"""
py.test test_case_demo3.py                       ->  run tests in module
py.test -v -s                                    ->  run all tests below somepath
py.test -v -s test_case_demo3.py::test_methodB   ->  only run test_method in test_module


-s: to print statements
-v: verbose
"""

import pytest


@pytest.fixture()
def setUp():
    print("Running Test Case Demo 3 setUp")
    yield
    print("Running Test Case Demo 3 tearDown")


def test_methodA(setUp):
    print("Running Method A")


def test_methodB(setUp):
    print("Running Method B")