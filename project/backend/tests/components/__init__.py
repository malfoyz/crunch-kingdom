from backend.tests.pages.base_page import BasePage
from backend.tests.locators.search_component_locators import SearchComponentLocators as Locators


class SearchComponent(BasePage):
    def fill_search_and_submit(self, search_query):
        search = self.element_is_visible(Locators.SEARCH)
        search.send_keys(search_query)
        search.submit()