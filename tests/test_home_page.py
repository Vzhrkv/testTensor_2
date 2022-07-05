import time
import pytest

from pages.main_page import MainPage


@pytest.mark.usefixtures('setup')
class TestHomePage:

    def test_image_page(self):
        url1 = 'https://yandex.ru/'
        main_page = MainPage(self.driver, url=url1)
        image_page = main_page.go_image_category()
        assert main_page.get_url() == 'https://yandex.ru/images/?utm_source=main_stripe_big', 'Link not same'

        first_cat_name = image_page.get_category_name()
        time.sleep(1)
        image_page.get_to_images_category()
        time.sleep(5)
        assert image_page.get_title() == first_cat_name, 'Name and search not equal'
        time.sleep(1)

        images_url = image_page.get_url()
        image_page.open_image()
        time.sleep(1)
        opened_image_url = image_page.get_url()
        assert images_url != opened_image_url, 'Picture not opened'


        image_page.get_next()
        time.sleep(5)

        opened_image_url_2 = image_page.get_url()
        assert opened_image_url != opened_image_url_2, 'Same pictures, nothing changed'

        image_page.get_back()
        time.sleep(5)

        assert opened_image_url == image_page.get_url(), 'Not same pictures'