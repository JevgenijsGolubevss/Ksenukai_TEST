from Resources.Locators import HomePageLocators
from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_search_visible(self):
        return self.is_visible(HomePageLocators.SEARCH_PLACEHOLDER_INPUT)

    def do_search(self, item):
        self.do_send_keys(HomePageLocators.SEARCH_PLACEHOLDER_INPUT, item)
        self.do_click(HomePageLocators.SEARCH_BUTTON)


