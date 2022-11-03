from Config.config import TestData
from Resources import UserData
from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.ProductPage import ProductPage
from pages.SearchPage import SearchPage
from pages.CheckoutPage import CheckoutPage
from tests.test_BasePage import Test_Base_Page
import util.utilFunctions


class Test_Home(Test_Base_Page):

    def test_001_get_iphone_in_cart(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_search(TestData.IPHONE)
        self.searchPage = SearchPage(self.driver)
        self.searchPage.click_on_item_by_text(TestData.IPHONE)
        self.productPage = ProductPage(self.driver)
        actual_title = self.productPage.get_product_title()
        assert actual_title == TestData.IPHONE
        actual_value = self.productPage.get_product_quantity()
        assert actual_value == TestData.PRODUCT_DEFAULT_QUANTITY
        product_price = self.productPage.get_product_price()
        float_product_price = util.utilFunctions.convert_currency_to_float(product_price)
        self.productPage.set_product_quantity()
        self.productPage.add_product_to_cart()
        actual_title = self.productPage.get_cart_dialog_window_title()
        assert actual_title == TestData.PRODUCT_ADDED_TO_CART_TITLE
        self.productPage.assert_button_and_click(TestData.GO_TO_CART_BUTTON)
        self.cartPage = CartPage(self.driver)
        actual_title = self.cartPage.get_cart_title()
        assert actual_title == TestData.CART_TITLE
        total_price = self.cartPage.get_total_cart_price()
        float_total_price = util.utilFunctions.convert_currency_to_float(total_price)
        assert float_total_price == float_product_price*TestData.PRODUCT_QUANTITY
        self.cartPage.scroll_to_element_on_page()
        self.cartPage.assert_button_and_click(TestData.PERFORM_PURCHASE_BUTTON)
        random_value = util.utilFunctions.get_random_value()+UserData.UserData['Email']
        self.cartPage.set_user_email(random_value)
        self.cartPage.new_user_checkout_proceed(TestData.NEW_USER_PROCEED_CHECKOUT_BUTTON)
        self.checkoutPage = CheckoutPage(self.driver)
        self.checkoutPage.fill_new_user_checkout_form(
            UserData.UserData['Name'],
            UserData.UserData['Surname'],
            UserData.UserData['Phone'],
            UserData.UserData['City'],
            UserData.UserData['Address'],
            UserData.UserData['Postal code'])
        for i in range(2):
            actual_price = self.checkoutPage.get_total_product_price()
            actual_price_float = util.utilFunctions.convert_currency_to_float(actual_price)
            assert actual_price_float == int(TestData.DELIVERY_PRICE)+int(float_total_price)
            self.checkoutPage.proceed_checkout_shipping()
        title = self.checkoutPage.get_checkout_shipping_heading()
        assert title == TestData.SHIPPING_HOME_HEADING





