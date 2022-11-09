"""
This module contains gmail login page,
the page object for the gmail login page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CheckoutOverview:



  # Locators
  CHECKOUT_PRODUCT  = (By.CSS_SELECTOR, 'div.inventory_item_name') 
  CHECKOUT_TITLE = (By.CSS_SELECTOR, 'span.title') 
  FINISH_BUTTON =  (By.ID, 'finish') 
    # Initializer 
  
  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)

  def valid_product_in_checkout(self):
    product= self.browser.find_element(*self.CHECKOUT_PRODUCT)
    title = product.text
    return title
  
  def confirm_checkout(self):
    send_finish_button = self.browser.find_element(*self.FINISH_BUTTON)
    send_finish_button.click()

  def get_title(self):
    checkout_title= self.browser.find_element(*self.CHECKOUT_TITLE)
    title = checkout_title.text
    return title