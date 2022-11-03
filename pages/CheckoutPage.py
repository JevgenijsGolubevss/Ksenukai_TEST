from datetime import time

from selenium.webdriver import Keys
from Resources.Locators import CheckoutPageLocators
from pages.BasePage import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_new_user_checkout_form(self, first_name, last_name, phone_number, city, street, postal_code):
        self.do_send_keys(CheckoutPageLocators.ADDRESS_FIRST_NAME, first_name)
        self.do_send_keys(CheckoutPageLocators.ADDRESS_LAST_NAME, last_name)
        self.do_send_keys(CheckoutPageLocators.ADDRESS_PHONE_NUMBER, phone_number)
        self.do_click(CheckoutPageLocators.ADDRESS_CITY_SELECTOR)
        self.do_send_keys(CheckoutPageLocators.ADDRESS_CITY, city)
        self.do_send_keys(CheckoutPageLocators.ADDRESS_CITY, Keys.ENTER)
        self.do_send_keys(CheckoutPageLocators.ADDRESS_STREET, street)
        self.do_click(CheckoutPageLocators.ADDRESS_POSTAL_CODE)
        self.do_send_keys(CheckoutPageLocators.ADDRESS_POSTAL_CODE, postal_code)

    def get_total_product_price(self):
        return self.get_element_text(CheckoutPageLocators.CHECKOUT_TOTAL_PRICE).text

    def proceed_checkout_shipping(self):
        return self.do_click(CheckoutPageLocators.CheckoutShippingButton)

    def get_buy_price(self):
        return self.get_element_text(CheckoutPageLocators.BUY_PRICE).text

    def get_checkout_shipping_heading(self):
        return self.get_element_text(CheckoutPageLocators.SHIPPING_TO_HOME_HEADING).text


