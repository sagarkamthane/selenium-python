import pytest
from pytestpractice.BaseClass import LoggerBaseClass


@pytest.mark.usefixtures("test_data")
class TestDatafixture(LoggerBaseClass) :

    def test_testdata(self, test_data):
        log = self.test_logger_demo()
        log.info(test_data)
        log.info(test_data[0])
        log.info(test_data[1])
        #print(test_data, test_data[0], test_data[1])



        