import time
from  selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())


# Functions


# This Function is for click
def XPATHc(path):
    wait = WebDriverWait(driver, 30)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, f'{path}')))
    element.click()
    return element

# This Function is for Send Keys , Example : '//*[@id="UserUsername"]' , 'Your Password'
def XPATHs(path , Keys):
    wait = WebDriverWait(driver, 30)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, f'{path}')))
    element.send_keys(Keys)
    return element

# This Function is for get data from xpath like text
def XPATHd(path):
    wait = WebDriverWait(driver, 30)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, f'{path}')))
    return element



# # Example :


# # Open the login page
# driver.get("https://www.example.com/login")

# # Example usage of XPATHs function to enter username and password
# XPATHs('//*[@id="username-input"]', 'example_username')  # Enter the username
# XPATHs('//*[@id="password-input"]', 'example_password')  # Enter the password


# # Example usage of XPATHc function to click on the login button
# XPATHc('//*[@id="login-button"]')  # Click the login button


# # Example usage of XPATHd function to retrieve and print the welcome message
# welcome_element = XPATHd('//*[@id="welcome-message"]')
# welcome_message = welcome_element.text
# print(welcome_message)


# START ;

driver.get("") # Here your website link





time.sleep(100)
