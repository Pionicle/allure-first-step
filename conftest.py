from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pytest import Parser, FixtureRequest
import pytest

from pages.home_page import HomePage
from pages.product_page import ProductPage


def pytest_addoption(parser: Parser):
    """Добавляем кастомные аргументы для pytest"""
    parser.addoption("--headless", action="store_true", help="Запуск в режиме headless")


@pytest.fixture(scope="session")
def browser(request: FixtureRequest):
    """Создаем браузер."""
    options = Options()

    if request.config.getoption("--headless"):
        options.add_argument("--headless")

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(5)

    yield browser
    browser.close()


@pytest.fixture()
def homepage(browser: WebDriver) -> HomePage:
    """Фикстура для главной страницы."""
    homepage = HomePage(browser)
    return homepage


@pytest.fixture()
def product_page(browser: WebDriver) -> ProductPage:
    """Фикстура для главной страницы."""
    product_page = ProductPage(browser)
    return product_page
