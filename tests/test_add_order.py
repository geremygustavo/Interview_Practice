"""
These tests cover DuckDuckGo searches.
"""

from pages.saucedemo.saucedemo_login import SauceDemoLogin
from pages.saucedemo.saucedemo_products import Products
from pages.saucedemo.saucedemo_cart import Cart
from pages.saucedemo.saucedemo_checkout import Checkout
from pages.saucedemo.saucedemo_checkout_overview import CheckoutOverview



def test_basic_gmail_login(browser):
  login_page = SauceDemoLogin(browser)
  products_page = Products(browser)
  cart = Cart(browser)
  checkout = Checkout(browser)
  checkout_overview = CheckoutOverview(browser)
  
  USER = "standard_user"
  PWD = "secret_sauce"
  
  # Given the https://www.saucedemo.com/ home page is displayed
  login_page.load()

  # When the user login
  login_page.input_data_login_form(USER,PWD)
  # And Add Product in th cart
  products_page.select_products()
  products_page.confirm_cart()
  # Then valid Product added in the cart
  assert 'Sauce Labs Bike Light' == cart.valid_product_in_cart()
  
  # And the user confirm checkout
  cart.confirm_cart_checkout()
  
  # And the user confirm checkout Information
  FNAME = "standard_user"
  LNAME = "secret_sauce"
  CODE = "secret_sauce"
  checkout.confirm_checkout_information(FNAME,LNAME,CODE)
  
  # Then user validate that product is part of checkout overview
  assert 'Sauce Labs Bike Light' == checkout_overview.valid_product_in_checkout()
  
  # Then user validate that order is completed
  checkout_overview.confirm_checkout()
  assert 'CHECKOUT: COMPLETE!' == checkout_overview.get_title()
  