from time import sleep

import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest
from page.app import App

class TestXueQiu:

    def setup(self):
        """
        实例化app类
        获取self.app.start().main()
        """
        self.topup = App().start().main().topup().creditcard()

    # @pytest.mark.parametrize("name", yaml.safe_load(open("../testdata_yaml/test_search.yaml",encoding="utf-8")))
    def test_creditcardflow(self):
        self.topup.creditcard()

