import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

BASE_URL = "https://www.chitai-gorod.ru"


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.ui
def test_add_to_cart(browser):
    browser.get(BASE_URL)

    # Указываем в строке поиска название книги
    find_a_book = browser.find_element(By.CSS_SELECTOR, 'input.header-search__input')
    find_a_book.send_keys('По волчьим следам')
    sleep(3)
    browser.find_element(By.CSS_SELECTOR, 'button.header-search__button').click()
    sleep(3)

    print('Книга найдена')

    # Открываем найденную книгу в результатах поиска
    open_the_book = browser.find_element(By.CSS_SELECTOR, 'img.product-picture__img')
    open_the_book.click()
    sleep(2)

    print('Открываем карточку книги...')

    # Добавляем книгу в корзину
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, 'button.product-offer-button')
    add_to_cart_button.click()
    sleep(2)
    print('Книга добавлена в корзину')

    # Переходим в корзину
    switch_to_cart = browser.find_element(By.CSS_SELECTOR, 'a.sticky-header__controls-item')
    switch_to_cart.click()
    sleep(5)
    print('Переходим в корзину...')

    # Добавляем второй экземпляр в корзину
    add_second_book = browser.find_element(By.CSS_SELECTOR, 'button.product-quantity__button--right')
    add_second_book.click()
    print('Добавляем второй экземпляр книги')
    sleep(5)

    # Очищаем корзину
    delete_item = browser.find_element(By.CSS_SELECTOR, 'button.cart-item__actions-button--delete')
    print('Очищаем коризну...')
    delete_item.click()
    sleep(3)
    print('Корзина очищена')

    empty_cart = browser.find_element(By.CSS_SELECTOR, '.item-removed__actions-button')
    is_empty = empty_cart.text
    assert is_empty == "ВЕРНУТЬ В КОРЗИНУ"
