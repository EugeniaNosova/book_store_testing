# Shop: отображение страницы товара
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
shop_menu = driver.find_element_by_id("menu-item-40").click()
html5 = driver.find_element_by_css_selector(".post-181").click()
html5label = driver.find_element_by_css_selector(".product_title")
html5label_text = html5label.text
assert "HTML5 Forms" in html5label_text
driver.quit()

# Shop: отображение страницы товара
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
shop_menu = driver.find_element_by_id("menu-item-40").click()
html_cat = driver.find_element_by_link_text("HTML").click()
items_count = driver.find_elements_by_css_selector(".product_cat-html")
if len(items_count) == 3:
    print("На странице 3 товара")
else:
    print("Ошибка. Количество товаров на странице: " + str(len(items_count)))
driver.quit()

# Shop: сортировка товаров
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
shop_menu = driver.find_element_by_id("menu-item-40").click()
orderby_def = driver.find_element_by_xpath('//option[@value="menu_order"]')
orderby_def_selected = orderby_def.get_attribute("selected")
if orderby_def_selected == "true":
    print("Сортировка по умолчанию")
else:
    print("Сортировка не совпадает")
orderby = driver.find_element_by_css_selector(".orderby")
orderby_select = Select(orderby)
orderby_select.select_by_value("price-desc")
orderby = driver.find_element_by_css_selector(".orderby")
orderby_high = driver.find_element_by_xpath('//option[@value="price-desc"]')
orderby_high_selected = orderby_high.get_attribute("selected")
if orderby_high_selected == "true":
    print("Сортировка по убыванию цены")
else:
    print("Сортировка не совпадает")
driver.quit()

# Shop: отображение, скидка товара
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
shop_menu = driver.find_element_by_id("menu-item-40").click()
android = driver.find_element_by_css_selector(".post-169").click()
oldprice = driver.find_element_by_xpath('//del/span[@class="woocommerce-Price-amount amount"]')
oldprice_text = oldprice.text
assert "600.00" in oldprice_text
newprice = driver.find_element_by_xpath('//ins/span[@class="woocommerce-Price-amount amount"]')
newprice_text = newprice.text
assert "450.00" in newprice_text
image = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")) )
image_clk = driver.find_element_by_css_selector(".images").click()
close = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")) )
close_clk = driver.find_element_by_css_selector(".pp_close").click()
driver.quit()

# Shop: проверка цены в корзине
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
shop_menu = driver.find_element_by_id("menu-item-40").click()
# В корзину добавляю единственную книгу не out of stock
addtocart = driver.find_element_by_xpath('//a[@data-product_id="165"]').click()
time.sleep(3)
cartitems = driver.find_element_by_css_selector(".cartcontents")
cartitems_text = cartitems.text
assert "1 Item" in cartitems_text
cartprice = driver.find_element_by_xpath('//span[@class="amount"]')
cartprice_text = cartprice.text
assert "₹350.00" in cartprice_text
gotocart = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0").click()
subtotal = WebDriverWait(driver, 5).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal"), "350.00"))
total = WebDriverWait(driver, 5).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total"), "357.00"))
driver.quit()

# Shop: работа в корзине
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
shop_menu = driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
# На сайте только одну книгу можно добавить в корзину, все тесты далее провожу только с ней
addtocart = driver.find_element_by_xpath('//a[@data-product_id="165"]').click()
time.sleep(3)
addtocart = driver.find_element_by_xpath('//a[@data-product_id="165"]').click()
gotocart = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0").click()
remove = driver.find_element_by_css_selector(".remove").click()
time.sleep(3)
undo = driver.find_element_by_link_text("Undo?").click()
quantity = driver.find_element_by_css_selector(".input-text.qty.text")
quantity.clear()
quantity.send_keys("3")
update = driver.find_element_by_xpath('//input[@name="update_cart"]').click()
quantitytotal = driver.find_element_by_css_selector(".input-text.qty.text")
quantity_check = quantitytotal.get_attribute("value")
assert "3" in quantity_check
time.sleep(3)
apply_coupon = driver.find_element_by_xpath('//input[@name="apply_coupon"]').click()
coupon_error = WebDriverWait(driver, 5).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error"), "Please enter a coupon code."))
driver.quit()

# Shop: покупка товара
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
shop_menu = driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
# В корзину добавляю единственную книгу не out of stock
addtocart = driver.find_element_by_xpath('//a[@data-product_id="165"]').click()
time.sleep(3)
gotocart = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0").click()
checkout = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")) )
checkout_click = driver.find_element_by_css_selector(".checkout-button").click()
billing = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-billing-fields"), "Billing Details"))
fname = driver.find_element_by_xpath('//input[@name="billing_first_name"]')
fname.send_keys("Eugenia")
lname = driver.find_element_by_xpath('//input[@name="billing_last_name"]')
lname.send_keys("Nosova")
email = driver.find_element_by_xpath('//input[@name="billing_email"]')
email.send_keys("fatcatgenechka@mail.ru")
phone = driver.find_element_by_xpath('//input[@name="billing_phone"]')
phone.send_keys("89152454750")
country = driver.find_element_by_css_selector(".select2-container.country_to_state.country_select").click()
country_input = driver.find_element_by_id("s2id_autogen1_search")
country_input.send_keys("Russia")
country_select = driver.find_element_by_css_selector(".select2-result-label").click()
street = driver.find_element_by_xpath('//input[@name="billing_address_1"]')
street.send_keys("Vesenniya")
city = driver.find_element_by_xpath('//input[@name="billing_city"]')
city.send_keys("Kolomna")
state = driver.find_element_by_xpath('//input[@name="billing_state"]')
state.send_keys("Moscow region")
postcode = driver.find_element_by_xpath('//input[@name="billing_postcode"]')
postcode.send_keys("140404")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
payment = driver.find_element_by_xpath('//input[@value="cheque"]').click()
place_order = driver.find_element_by_id("place_order").click()
thank_you = WebDriverWait(driver, 5).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
payment_method = WebDriverWait(driver, 5).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".shop_table.order_details"), "Check Payments"))
driver.quit()