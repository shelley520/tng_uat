from time import sleep
from selenium.webdriver.common.by import By
import yaml
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.topupmenu import TopUpMenu


class TopUp(BasePage):

    def creditcard(self):
        self.steps("../step/topup.yaml")

