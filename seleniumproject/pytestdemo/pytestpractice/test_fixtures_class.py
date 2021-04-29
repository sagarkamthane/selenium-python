import pytest

@pytest.mark.usefixtures("conftestfixture")
class TestFixtures:  # T in test should be in upper case(PascalCase)
    def test_case1(self):
        print("test case 1")

    def test_case2(self):
        print("test case 2")

    def test_case3(self):
        print("test case 3")

    def test_case4(self):
        print("test case 4")

@pytest.mark.usefixtures("setup") #scope = "class"
class TestFixturesScopeClass:  # T in test should be in upper case(PascalCase)
    def test_case1(self):
        print("test case 1")

    def test_case2(self):
        print("test case 2")

    def test_case3(self):
        print("test case 3")

    def test_case4(self):
        print("test case 4")

@pytest.mark.usefixtures("cross_browser")
def test_cross_browser(cross_browser):
    print(cross_browser)
