"""
This module contains gmail login page,
the page object for the gmail login page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SauceDemoLogin:

  # URL

  URL = 'https://www.saucedemo.com/'

  # Locators

  USER_INPUT = (By.ID, 'user-name')
  PWD_INPUT = (By.ID, 'password')
  LOGIN_BUTTON =  (By.ID, 'login-button') 
  # Initializer 

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)

  def input_data_login_form(self, user,pwd):
    user_input = self.browser.find_element(*self.USER_INPUT)
    user_input.send_keys(user)
    pwd_input = self.browser.find_element(*self.PWD_INPUT)
    pwd_input.send_keys(pwd + Keys.RETURN)