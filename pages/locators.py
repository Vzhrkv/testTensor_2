from selenium.webdriver.common.by import By


class Locator:

    IMAGES_CAT = (By.LINK_TEXT, 'Картинки')
    FIRST_CAT = (By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0')
    FIRST_IMAGE_IN_SEARCH_TABLE = (By.CLASS_NAME, 'serp-item__link')
    NEXT_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_next')
    PREV_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_prev')
