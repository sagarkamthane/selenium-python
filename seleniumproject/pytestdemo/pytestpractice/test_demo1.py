#any pytestdemo file should start with test_ or end with _test
#pytestdemo method should start with test
#any test should be wrapped in function only
import pytest


@pytest.mark.smoke # py.test -m smoke : skips test case taged with smoke
@pytest.mark.skip #skips the test case
def test_case1():
    print("Hello")

@pytest.mark.xfail #runs the testcase but reports as xfail if test case execution fails, doesn't stop the execution
def test_case2():
    print("good morning")
    assert False


