from selenium import webdriver
import openpyxl
import pytest

path = r"C:\Users\VISHANT\Desktop\selenium\chromedriver.exe"

driver = webdriver.Chrome(executable_path= path)



def data_genration():
    l=[["vishant", "kumar"],["anuj", "khokher"],["amit", "tyagi"]]
    return l

@pytest.mark.parametrize("data", data_genration())

def test_valid(data):
    driver.maximize_window()
    driver.get("https://www.rigvedtech.com/contact-us/")

    driver.find_element_by_xpath("//input[@id='wpforms-2036-field_2']").send_keys(data[0])
    driver.find_element_by_xpath("//input[@id='wpforms-2036-field_2-last']").send_keys(data[1])