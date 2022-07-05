from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """Base class for base actions"""

    def __init__(self, driver, url='https://yandex.ru/'):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10, 1)

    def is_present(self, by_what, value) -> WebElement:
        """function for find element on page"""
        return self.wait.until(EC.presence_of_element_located((by_what, value)))

    def is_clickable(self, by_what, value) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable((by_what, value)))

    def are_visible(self, by_what, value) -> WebElement:
        return self.wait.until(EC.visibility_of_all_elements_located((by_what, value)))

    def go_to_site(self) -> WebElement:
        return self.driver.get(self.url)

    def get_to_category(self, by_what, value):
        element = self.is_present(by_what, value)
        return element.click()

    def get_url(self):
        return self.driver.current_url

    def press_key(self, element, keys):
        return element.send_keys(keys)