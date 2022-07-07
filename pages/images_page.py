from .base_page import BasePage
from .locators import Locator

from selenium.webdriver.common.by import By


class ImagesPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.category = '//*[@class="PopularRequestList-Item PopularRequestList-Item_pos_0"]'
        self.search_text = '//*[@class="PopularRequestList-SearchText"]'
        self.image = 'serp-item__link'
        self.next_button = '.CircleButton_type_next'
        self.prev_button = '.CircleButton_type_prev'

    def get_to_images_category(self):
        images = self.driver.find_element(*Locator.FIRST_CAT)
        return images.click()

    def get_title(self):
        return self.driver.title.split(':')[0]

    def get_category_name(self):
        element = self.driver.find_element(*Locator.FIRST_CAT)
        return element.get_attribute('data-grid-text')

    def open_image(self):
        img = self.driver.find_elements(*Locator.FIRST_IMAGE_IN_SEARCH_TABLE)
        return img[0].click()

    def get_next(self):
        element = self.is_present(*Locator.NEXT_BUTTON)
        return element.click()

    def get_back(self):
        element = self.is_present(*Locator.PREV_BUTTON)
        return element.click()
