from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ImagesPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.category = '//*[@class="PopularRequestList-Item PopularRequestList-Item_pos_0"]'
        self.search_text = '//*[@class="PopularRequestList-SearchText"]'
        self.image = 'serp-item__link'
        self.next_button = '/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[4]/i'
        self.back_button = '/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[4]/i'

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

    def press_next_button(self):
        element = self.driver.find_element(By.XPATH, self.next_button)
        return element.send_keys(Keys.ARROW_RIGHT)

    def press_back_button(self):
        element = self.driver.find_element(By.XPATH, self.back_button)
        return element.click(Keys.ARROW_LEFT)