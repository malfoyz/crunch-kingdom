from backend.tests.pages.search_page import SearchPage


class TestSearchPage:

    #@pytest.mark.django_db
    def test_search(self, driver):
        search_page = SearchPage(driver, 'http://127.0.0.1:8000/')
        search_page.open()

        search_query = 'Торт Кубик Рубика'
        search_page.perform_search(search_query)

        result_page = search_page.get_result_page()
        result = result_page.get_result_info()

        assert search_query == result[0], f'Ожидаемое имя: {search_query}. Результат: {result[0]}'



