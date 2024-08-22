from selenium.webdriver.common.by import By


class ResultPageLocators:
    RESULT_NAME = (By.CLASS_NAME, 'item__name')
    RESULT_SHOP_NAME = (By.CLASS_NAME, 'item__shop-name')
    RESULT_PRICE = (By.CLASS_NAME, 'item__price')
    RESULT_WEIGHT = (By.CLASS_NAME, 'item__weight')


