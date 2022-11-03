from Resources.Locators import CartPageLocators
from pages.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_title(self):
        return self.get_element_text(CartPageLocators.CART_PAGE_TITLE).text

    def get_total_cart_price(self):
        return self.get_element_text(CartPageLocators.TOTAL_CART_PRICE).text

    def scroll_to_element_on_page(self):
        self.scroll_into_view(CartPageLocators.PERFORM_PURCHASE_BUTTON)

    def assert_button_and_click(self, text):
        locator = CartPageLocators.PERFORM_PURCHASE_BUTTON
        element = self.get_element_text(locator).get_attribute("value")
        assert element == text
        self.do_click(locator)

    def set_user_email(self, text):
        self.do_click(CartPageLocators.NEW_USER_EMAIL_FIELD)
        self.do_send_keys(CartPageLocators.NEW_USER_EMAIL_FIELD, text)

    def new_user_checkout_proceed(self, text):
        locator = CartPageLocators.CONTINUE_NEW_USER_BUTTON
        element = self.get_element_text(locator).get_attribute("value")
        assert element == text
        self.do_click(locator)


