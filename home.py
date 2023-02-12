# Home: добавление комментария
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 300);")
product = driver.find_element_by_css_selector(".products li:nth-child(1)").click()
reviews_tab = driver.find_element_by_css_selector(".reviews_tab").click()
star_5 = driver.find_element_by_css_selector(".star-5").click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Eugenia")
email = driver.find_element_by_id("email")
email.send_keys("fatcatgenechka@mail.ru")
submit = driver.find_element_by_id("submit").click()
driver.quit()