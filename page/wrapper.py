from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

def handle_black(func):
    def wrapper(*args,**kwargs):
        from page.base_page import BasePage
        _black_list = [
            (By.XPATH, "//*[@content-desc='Skip']"),
            (By.XPATH, "//android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Image[1]"),

            # (By.XPATH, "//*[@text='Skip']")
        ]
        _max_num = 3
        _error_num = 0
        isinstance:BasePage = args[0]
        try:
            element = func(*args,**kwargs)
            _error_num = 0
            # isinstance._driver.implicitly_wait(5)
            return element
        except Exception as e:
            # isinstance._driver.implicitly_wait(2)
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for ele in _black_list:
                print(ele)
                elelist = isinstance._driver.find_elements(*ele)
                print(isinstance)
                print(elelist)
                if len(elelist) > 0:
                    elelist[0].click()
            return wrapper(*args, **kwargs)
        raise e
    return wrapper