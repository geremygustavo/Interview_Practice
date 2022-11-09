"""
This module contains gmail login page,
the page object for the gmail login page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Checkout:



  # Locators
  FIRST_NAME__INPUT = (By.ID, 'first-name')
  LAST_NAME__INPUT = (By.ID, 'last-name')
  CODE_INPUT = (By.ID, 'postal-code')
  CONTINUE_BUTTON =  (By.ID, 'continue') 
    # Initializer 

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)

  def confirm_checkout_information(self, first_name,last_name,code):
    first_name_input = self.browser.find_element(*self.FIRST_NAME__INPUT)
    first_name_input.send_keys(first_name)
    last_name_input = self.browser.find_element(*self.LAST_NAME__INPUT)
    last_name_input.send_keys(last_name )
    code_input = self.browser.find_element(*self.CODE_INPUT)
    code_input.send_keys(code )
    send_continue_button = self.browser.find_element(*self.CONTINUE_BUTTON)
    send_continue_button.click()