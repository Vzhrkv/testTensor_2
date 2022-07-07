from selenium.webdriver.common.by import By


from .base_page import BasePage
from .images_page import ImagesPage
from .locators import Locator


class MainPage(BasePage):


    def __init__(self, driver, url):
        super().__init__(driver, url)

    def get_image_element(self):
        return self.is_present(*Locator.IMAGES_CAT)

    def get_image_link(self):
        return self.get_image_element().get_dom_attribute('href')

    def get_image_button(self):
        return self.is_present(*Locator.IMAGES_CAT)

    def go_image_category(self):
        self.get_image_button().click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return ImagesPage(self.driver, self.driver.current_url)



