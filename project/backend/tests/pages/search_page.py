from backend.tests.pages.base_page import BasePage
from backend.tests.pages.result_page import ResultPage
from backend.tests.components import SearchComponent


class SearchPage(BasePage):

    def get_search_component(self):
        return SearchComponent(self.driver, self.url)

    def perform_search(self, search_query):
        search_component = self.get_search_component()
        search_component.fill_search_and_submit(search_query)

    def get_result_page(self):
        return ResultPage(self.driver, self.url)



