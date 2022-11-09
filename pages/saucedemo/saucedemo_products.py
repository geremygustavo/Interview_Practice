"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By


class Products:
  
  # Locators

  ADD_CART_BUTTON  = (By.ID, 'add-to-cart-sauce-labs-bike-light')
  CART_ICON  = (By.CSS_SELECTOR, 'span.shopping_cart_badge')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def select_products(self):
    product = self.browser.find_element(*self.ADD_CART_BUTTON)
    product.click()
  
  def confirm_cart(self):
    search_input = self.browser.find_element(*self.CART_ICON)
    search_input.click()

