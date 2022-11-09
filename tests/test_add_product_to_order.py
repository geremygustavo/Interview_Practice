"""
These tests cover DuckDuckGo searches.
"""

from pages.saucedemo.saucedemo_login import SauceDemoLogin
from pages.saucedemo.saucedemo_products import Products
from pages.saucedemo.saucedemo_cart import Cart



def test_basic_gmail_login(browser):
  login_page = SauceDemoLogin(browser)
  products_page = Products(browser)
  cart = Cart(browser)
  
  USER = "standard_user"
  PWD = "secret_sauce"
  # Given the https://www.saucedemo.com/ home page is displayed
  login_page.load()

  # When the user login
  login_page.input_data_login_form(USER,PWD)
  # And user select add product to cart
  products_page.select_products()
  products_page.confirm_cart()
  # Then user validate product is part of cart
  assert 'Sauce Labs Bike Light' == cart.valid_product_in_cart()
  