import inspect
import json

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

_black_list = [
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH,
             "//android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Image[1]"),
            (By.XPATH, "//*[@content-desc='Skip']")
            # (By.XPATH, "//*[@text='Skip']")
        ]
def abc():
    for ele in _black_list:
        # print(ele)
        print(ele[1])


# def steps(name):
#
#     with open("../step/main.yaml", encoding="utf-8") as f:
#         steps = yaml.safe_load(f)[name]
#
#     print(steps)
#     # for key,value in steps.items():
#     #    print(key,value[0]["locator"])
#
#     for step in steps:
#         element = None
#         print(step["action"])
#         print(step["by"])
#         print(step["locator"])
#         # if "action" in step.keys():
#         #     action = step["action"]
#         #     # print(action)
#         #     element = self.find(step["by"], step["locator"])
# steps("topup")