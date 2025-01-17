from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def check_title_is(self, title: str):
        """Проверяет, что название товара равно `title`."""
        page_title = self.browser.find_element(By.TAG_NAME, "h2")
        assert page_title.text == title
