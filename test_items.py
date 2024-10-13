import time

from selenium.webdriver.common.by import By


def test_button_add_product_in_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    text = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket').text
    assert len(text) > 0, 'Not button add basket'
