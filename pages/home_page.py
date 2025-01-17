from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.products = []

    def open(self):
        """Открывает главную страницу."""
        self.browser.get("https://www.demoblaze.com/index.html")

    def click_galaxy_s6(self):
        """Кликает по ссылке Samsung Galaxy S6."""
        galaxy_s6 = self.browser.find_element(
            By.XPATH, '//a[text()="Samsung galaxy s6"]'
        )
        galaxy_s6.click()

    def click_monitors(self):
        """Выбирает категорию 'Мониторы' и ждет загрузки товаров."""
        monitor_link = self.browser.find_element(
            By.XPATH, "//a[@onclick=\"byCat('monitor')\"]"
        )

        old_products = self.browser.find_elements(By.CSS_SELECTOR, ".card.h-100")
        old_product = old_products[0] if old_products else None

        monitor_link.click()
        wait = WebDriverWait(self.browser, 5)

        if old_product:
            wait.until(EC.staleness_of(old_product))

        wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card.h-100"))
        )

        self.products = self.browser.find_elements(By.CSS_SELECTOR, ".card")

    def check_products_count(self, count: int):
        """Проверяет, что количество товаров равно `count`."""
        assert len(self.products) == count
