"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By


class Cart:
  
  # Locators

  CART_PRODUCT  = (By.CSS_SELECTOR, 'div.inventory_item_name')
  CHECKOUT_BUTTON = (By.ID, 'checkout')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def valid_product_in_cart(self):
    product= self.browser.find_element(*self.CART_PRODUCT)
    title = product.text
    return title
  
  def confirm_cart_checkout(self):
    send_cart_button = self.browser.find_element(*self.CHECKOUT_BUTTON)
    send_cart_button.click()
  

