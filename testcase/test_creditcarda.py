from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest
from selenium.webdriver.common.by import By


class TestXueQiu:
    """
    改造1 pytest
    改造2 元素查找xpath
    改造3 将自动生成的find_element_by改造成find_element形式
    """
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.sinodynamic.tng.consumer.uat"
        caps["appActivity"] = "com.sinodynamic.tng.consumer.view.modern.versatile.VersatileActivity"
        caps["noReset"] = True
        caps["unicodeKeyboard"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        sleep(10)
        print("*****************************")
        print(self.driver.contexts)
        self.driver.find_element(By.XPATH,"//android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Image[1]").click()
        sleep(20)
        print("*****************************")
        # print(self.driver.window_handles)
        # self.driver.switch_to.context(self.driver.context[-1])
        print("*****************************")
        self.driver.find_element(By.XPATH,"//*[@content-desc='Top-Up']").click()
        print("*****************************")
        print(self.driver.contexts)
        # print(self.driver.window_handles)
        sleep(10)
        self.driver.find_element(By.XPATH, "//*[@content-desc='Skip']").click()
        print("*****************************")
        sleep(10)
        self.driver.find_element(By.XPATH,"//*[@resource-id='topup_index_button_listItem']//*[@content-desc='Credit Card']").click()
        print(self.driver.contexts)
        sleep(20)