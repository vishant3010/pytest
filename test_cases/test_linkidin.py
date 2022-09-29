from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
import pytest

path = r"C:\Users\VISHANT\Desktop\selenium\chromedriver.exe"

driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()
driver.implicitly_wait(5)

def test_main():
    driver.get("https://www.linkedin.com/home")

def test_signin():
    driver.find_element_by_xpath("//a[@class='nav__button-secondary btn-md btn-secondary-emphasis']").click()

def test_valid_login():
    driver.find_element_by_xpath("//input[@id='username']").send_keys("vishantkumar2012@gmail.com")
    driver.find_element_by_xpath("//input[@id='password']").send_keys("9045844228")
    driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()

def test_skip():
    driver.find_element_by_xpath("//button[normalize-space()='Skip']").click()


# pytest filename.py -s

# pytest --alluredir  ./report

# allure generate  <xml path> --clean



