import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.topup import TopUp


class Main(BasePage):

    def topup(self):
        self.steps("../step/main.yaml")
        return TopUp(self._driver)
