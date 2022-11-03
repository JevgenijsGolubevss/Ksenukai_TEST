from Resources.Locators import ProductPageLocators
from pages.BasePage import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_product_title(self):
        return self.get_element_text(ProductPageLocators.PRODUCT_HEADING).text

    def get_product_quantity(self):
        return self.get_element_text(ProductPageLocators.PRODUCT_QUANTITY).get_attribute("value")

    def get_product_price(self):
        return self.get_element_text(ProductPageLocators.PRODUCT_PRICE).text

    def set_product_quantity(self):
        return self.do_click(ProductPageLocators.INCREASE_QUANTITY_BUTTON)

    def add_product_to_cart(self):
        return self.do_click(ProductPageLocators.ADD_TO_CART_BUTTON)

    def get_cart_dialog_window_title(self):
        return self.get_element_text(ProductPageLocators.CART_DIALOG_WINDOW_TITLE).text

    def assert_button_and_click(self, text):
        locator = ProductPageLocators.GO_TO_CART_BUTTON
        element = self.get_element_text(locator).text
        assert element == text
        self.do_click(locator)
