import pytest

@pytest.mark.smoke
def test_case1():
    msg = "hello"
    assert msg == 'hello', "message not same"

#to run a test case with with specific tag ex: @pytest.mark.smoke use py.test -m smoke  -v -s
