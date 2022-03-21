import inspect
import json

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.wrapper import handle_black


class BasePage:
    """
    create BasePage class due to there is same __init__ function in each class
    create init function in BasePage, and let the other class inherit the BasePage class
    """

    _params = {}
    def __init__(self,driver:WebDriver = None):
        self._driver = driver

    @handle_black
    def finds(self,locator,value:str=None):
        element: list
        if isinstance(locator,tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator,value)
        return elements

    @handle_black
    def find(self,locator,value:str = None):
        element: WebDriver
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
            self._driver.find_element()
        else:
            element = self._driver.find_element(locator, value)
        return element

    @handle_black
    def find_text(self, locator, value: str = None):
        element: WebDriver
        if isinstance(locator, tuple):
            element_text = self._driver.find_element(*locator).text
            self._driver.find_element()
        else:
            element_text = self._driver.find_element(locator, value).text
        return element_text

    def steps(self,path):
        name = inspect.stack()[1].function
        print(name)
        with open(path,encoding="utf-8") as f:
            steps = yaml.safe_load(f)[name]
        raw = json.dumps(steps)
        print(raw)
        for key,value in self._params.items():
            # ${name} | name:123
            raw = raw.replace(f'${{{key}}}',value)
        steps = json.loads(raw)

        for step in steps:
            element = None
            if "action" in step.keys():
                action = step["action"]
                # print(action)
                element = self.find(step["by"], step["locator"])
                if "click" == action:
                    locator = (By.XPATH, step["locator"])
                    WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable(locator))
                    element.click()
                if "send" == action:
                    element.send_keys(step["value"])
                if "text" == action:
                    ele = element.text
                    return ele
                if "len>=0" == action:
                    return element
