from backend.tests.pages.base_page import BasePage
from backend.tests.locators.result_page_locators import ResultPageLocators as Locators


class ResultPage(BasePage):

    def get_result_info(self):
        result_name = self.element_is_visible(Locators.RESULT_NAME).text
        result_shop_name = self.element_is_visible(Locators.RESULT_SHOP_NAME).text
        result_price = self.element_is_visible(Locators.RESULT_PRICE).text
        result_weight = self.element_is_visible(Locators.RESULT_WEIGHT).text

        return result_name, result_shop_name, result_price, result_weight


