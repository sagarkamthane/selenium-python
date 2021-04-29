import pytest
from _pytest import fixtures

from pytestpractice.BaseClass import LoggerBaseClass

@pytest.mark.usefixtures("test_data")
class TestLoggerUse(LoggerBaseClass):  #inherited LoggerBaseClass from BaseClass

    def test_case_one(self, test_data):
        log1 = self.test_logger_demo()
        log1.info(test_data)
        log1.info(test_data[0])
        log1.info(test_data[1])

