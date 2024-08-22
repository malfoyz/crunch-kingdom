from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """Метод ожидает, пока текущий элемент (locator) не будет виден на странице."""
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        """Метод ожидает, пока все нужные элементы (locator) не будут видны на странице."""
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

