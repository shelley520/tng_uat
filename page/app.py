# import pytest
import yaml
from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    """
    inherit BasePage class
    """

    # @pytest.mark.parametrize
    def start(self):
        """
        添加if else 判断；若不存在driver，添加driver参数，若driver存在，self._driver.launch_app()启动app
        :return: self实例，这样test case才能用串联模式：self.main = self.app.start().main()
        """

        if self._driver == None:
            caps = dict()
            value = yaml.safe_load(open("../data/config.yaml"))
            caps["platformName"] = value['caps']['platformName']
            caps["deviceName"] = value['caps']['deviceName']
            caps["appPackage"] = value['caps']['appPackage']
            caps["appActivity"] = value['caps']['appActivity']
            caps["noReset"] = value['caps']['noReset']
            #中文字输入
            caps["unicodeKeyboard"] =value['caps']['unicodeKeyboard']

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)

        return self

    def restart(self):
        pass

    def stop(self):
        self._driver.quit()

    def main(self) -> Main:
        """
        :return: Main类，类添加driver属性
        """
        return Main(self._driver)