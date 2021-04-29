
import inspect
import logging


import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def wait(self, css):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))


    def select_option(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)

    def logger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        file = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file.setFormatter(formatter)
        logger.addHandler(file)
        logger.setLevel(logging.DEBUG)
        # used to set level, if level if info logs below info will be printed, by default it's set to warning
        # below order needs to be followed strictly
        # log.debug('debug statement')
        # log.info('information statement')
        # log.warning('warning')
        # log.error('error')
        # log.critical('critical error')
        return logger