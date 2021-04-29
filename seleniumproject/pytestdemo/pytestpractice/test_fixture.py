import pytest


@pytest.fixture()
def preriquisite():
    print("\npreriquisite satisfied")
    yield
    print("\ni'll be executed after preriquisite")

def test_testcases(preriquisite):
    print("\nrunning test case after checking preriquisite")

def test_conftest(conftestfixture):
    print("\nconftest: running test case after checking preriquisite")