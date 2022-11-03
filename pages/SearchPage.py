from Resources.Locators import SearchPageLocators
from pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_item_by_text(self, by_text):
        self.is_visible(SearchPageLocators.SEARCHED_PRODUCTS)
        self.do_click_by_text(by_text)
