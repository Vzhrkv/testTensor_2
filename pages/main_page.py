import time

from .base_page import BasePage
from .images_page import ImagesPage
from selenium.webdriver.common.by import By


class MainPage(BasePage):


    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.images_link = 'body > div.body__wrapper > div.container.rows > div.row.rows__row.rows__row_main > div > div.container.container__services.container__line > nav > div > ul > li:nth-child(6) > a'
        self.images_button = 'body > div.body__wrapper > div.container.rows > div.row.rows__row.rows__row_main > div > div.container.container__services.container__line > nav > div > ul > li:nth-child(6) > a'

    def get_image_element(self):
        return self.is_present(By.CSS_SELECTOR, self.images_link)

    def get_image_link(self):
        return self.get_image_element().get_dom_attribute('href')

    def get_image_button(self):
        return self.is_present(By.LINK_TEXT, 'Картинки')

    def go_image_category(self):
        element = self.get_image_button().click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return ImagesPage(self.driver, self.driver.current_url)



