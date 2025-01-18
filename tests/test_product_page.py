from pages.home_page import HomePage
from pages.product_page import ProductPage
import allure


@allure.feature("Open product")
@allure.story("clickability")
def test_open_s6(homepage: HomePage, product_page: ProductPage):
    """Тест открытия страницы товара Samsung Galaxy S6."""
    homepage.open()
    homepage.click_galaxy_s6()
    product_page.check_title_is("Samsung galaxy s6")
