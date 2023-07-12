import json
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait

# Mở trình duyệt và đăng nhập vào trang web
driver = webdriver.Chrome()
driver.get('https://www.cryptorefills.com/login')
select_field = driver.find_element(By.XPATH, '//*[@id="email"]')
select_field.send_keys('nhattantr2002@gmail.com')
select_field = driver.find_element(By.XPATH, '//*[@id="password"]')
select_field.send_keys('nhattan2002@123H')
time.sleep(15)

# Lưu danh sách các cookie vào một file JSON
# driver.delete_all_cookies()
# with open('cookies.json', 'r') as f:
#     cookies = json.load(f)
# for cookie in cookies:
#     driver.add_cookie(cookie)
# driver.get('https://www.cryptorefills.com')
# Sử dụng các cookie đã lưu để đăng nhập vào trang web
# Tài khoản : ha11031989@gmail.com
# pass : Ha112002