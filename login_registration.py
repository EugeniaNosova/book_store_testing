# Registration_login: регистрация аккаунта
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
account_menu = driver.find_element_by_id("menu-item-50").click()
email_reg = driver.find_element_by_id("reg_email")
email_reg.send_keys("fatcatgenechka@mail.ru")
pass_reg = driver.find_element_by_id("reg_password")
pass_reg.send_keys("Koshechka1997!")
register = driver.find_element_by_xpath('//input[@name="register"]').click()
driver.quit()

# Registration_login: логин в систему
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
account_menu2 = driver.find_element_by_id("menu-item-50").click()
username = driver.find_element_by_id("username")
username.send_keys("fatcatgenechka@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("Koshechka1997!")
login = driver.find_element_by_xpath('//input[@name="login"]').click()
driver.quit()