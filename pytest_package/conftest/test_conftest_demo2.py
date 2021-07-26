# py.test -v -s conftest/test_conftest_demo2.py

import pytest


def test_demo2_methodA(oneTimeSetUp, setUp):
    print("Running conftest demo 2 method A")


def test_demo2_methodB():
    print("Running conftest demo 2 method B")