import pytest

@pytest.fixture()
def conftestfixture():
    print("\nfrom conftest: preriquisite satisfied")
    yield
    print("\nfrom conftext: i'll be executed after preriquisite")


@pytest.fixture(scope="class")
def setup():
    print("\nfrom setup: preriquisite satisfied")
    yield
    print("\nfrom setup: i'll be executed after preriquisite")

@pytest.fixture()
def test_data():
    print("test data")
    return ['sagar', 'kamthane']


@pytest.fixture(params=[['chrome', 'sagar', 'kamthane'], 'firefox', 'safari'])
def cross_browser(request):
    return request.param