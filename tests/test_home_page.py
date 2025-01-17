from pages.home_page import HomePage


def test_to_monitors(homepage: HomePage):
    """Тест открытия категории товаров 'Мониторы'."""
    homepage.open()
    homepage.click_monitors()
    homepage.check_products_count(2)
