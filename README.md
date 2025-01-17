# **Selenium + Pytest: Тестирование интернет-магазина**

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)  
![Pytest](https://img.shields.io/badge/Pytest-%3E%3D8.0-orange.svg)  
![Selenium](https://img.shields.io/badge/Selenium-%3E%3D4.0-darkgreen.svg)

## **Описание**

Этот проект предназначен для автоматизированного тестирования интернет-магазина [Demoblaze](https://www.demoblaze.com) с использованием **Selenium** и **Pytest**.

## **Функциональность**

- Тестирование выбора категорий товаров "Мониторы"
- Проверка открытия страниц товаров

---

## **Установка и настройка**

### **1. Установка зависимостей**

```sh
git clone https://github.com/Pionicle/selenium-pytest-tests.git
cd selenium-pytest-tests
pip install -r requirements.txt
```

### **2. Установка WebDriver**

- Убедитесь, что установлен **Google Chrome**.
- Установите **chromedriver** (или используйте `webdriver-manager`).

```sh
pip install webdriver-manager
```

---

## **Запуск тестов**

### **1. Обычный запуск**

```sh
pytest -v -s
```

### **2. Запуск в `headless`-режиме**

```sh
pytest -v -s --headless
```

### **3. Запуск тестов с отчетом `Allure`**

```sh
pytest --alluredir=reports
allure serve reports
```

---

## **Структура проекта**

```
selenium-pytest-tests/
│── tests/
│   ├── test_products.py   # Тесты товаров
│   ├── test_checkout.py   # Тесты оформления заказа
│
│── pages/
│   ├── home_page.py       # Главная страница
│   ├── product_page.py    # Страница товара
│
│── conftest.py            # Фикстуры pytest
│── requirements.txt       # Зависимости проекта
│── README.md              # Описание проекта
```

---

## **Пример теста**

```python
def test_open_s6(homepage: HomePage, product_page: ProductPage):
    """Тест открытия страницы товара Samsung Galaxy S6."""
    homepage.open()
    homepage.click_galaxy_s6()
    product_page.check_title_is("Samsung galaxy s6")
```
