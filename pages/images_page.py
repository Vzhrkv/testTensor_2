from .base_page import BasePage

from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class ImagesPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.category = '//*[@class="PopularRequestList-Item PopularRequestList-Item_pos_0"]'
        self.search_text = '//*[@class="PopularRequestList-SearchText"]'
        self.image = 'serp-item__link'
        self.next_button = '.CircleButton_type_next'
        self.prev_button = '.CircleButton_type_prev'

    def get_to_images_category(self):
        images = self.driver.find_element(By.XPATH, self.category)
        return images.click()

    def get_title(self):
        return self.driver.title.split(':')[0]

    def get_category_name(self):
        element = self.driver.find_element(By.XPATH, self.category)
        return element.get_attribute('data-grid-text')

    def open_image(self):
        img = self.driver.find_elements(By.CLASS_NAME, self.image)
        return img[0].click()

    def get_next(self):
        element = self.is_present(By.CSS_SELECTOR, self.next_button)
        return element.click()

    def get_back(self):
        element = self.is_present(By.CSS_SELECTOR, self.prev_button)
        return element.click()
