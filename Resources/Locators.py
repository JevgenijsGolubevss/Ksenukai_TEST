from selenium.webdriver.common.by import By


class Common:
    LOGO = ".main-logo"


class HomePageLocators:
    SEARCH_PLACEHOLDER_INPUT = (By.CSS_SELECTOR, ".main-search-input:nth-child(2)")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".main-search__submit button")


class SearchPageLocators:
    SEARCHED_PRODUCTS = (By.CSS_SELECTOR, ".sn-product")


class ProductPageLocators:
    PRODUCT_HEADING = (By.CSS_SELECTOR, ".detailed-product-block h1")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, ".form-item input")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-price-details .price span")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_cart_btn")
    INCREASE_QUANTITY_BUTTON = (By.CSS_SELECTOR, "#inc-quantity")
    CART_DIALOG_WINDOW_TITLE = (By.CSS_SELECTOR, "#cart-popup-container .title-success")
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, "#cart-popup-container .main-button")


class CartPageLocators:
    CART_PAGE_TITLE = (By.CSS_SELECTOR, ".page-title")
    TOTAL_CART_PRICE = (By.CSS_SELECTOR, "#cart-full-total-price")
    PERFORM_PURCHASE_BUTTON = (By.CSS_SELECTOR, ".cart-totals-block .cart-main-button")
    NEW_USER_EMAIL_FIELD = (By.CSS_SELECTOR, "#new_user_guest #user_email")
    CONTINUE_NEW_USER_BUTTON = (By.CSS_SELECTOR, "#new_user_guest > div:nth-child(5) > input")


class CheckoutPageLocators:
    ADDRESS_FIRST_NAME = (By.CSS_SELECTOR, "#address_first_name")
    ADDRESS_LAST_NAME = (By.CSS_SELECTOR, "#address_last_name")
    ADDRESS_PHONE_NUMBER = (By.CSS_SELECTOR, "#address_phone_number")
    ADDRESS_CITY_SELECTOR = (By.CSS_SELECTOR, "#select2-address_city_id-container")
    ADDRESS_CITY = (By.CSS_SELECTOR, ".select2-search__field")
    ADDRESS_STREET = (By.CSS_SELECTOR, "#address_street")
    ADDRESS_POSTAL_CODE = (By.CSS_SELECTOR, "#address_postal_code")
    CHECKOUT_TOTAL_PRICE = (By.CSS_SELECTOR, ".checkout-order-summary-total__price")
    CheckoutShippingButton = (By.CSS_SELECTOR, ".checkout-controls button span")
    BUY_PRICE = (By.CSS_SELECTOR, ".price")
    SHIPPING_TO_HOME_HEADING = (By.CSS_SELECTOR, ".content-block-content h1")

