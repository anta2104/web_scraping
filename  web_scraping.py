from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
import pyperclip
import json
driver = webdriver.Chrome()
# Đăng nhập
driver.get('https://www.cryptorefills.com/login')
select_field = driver.find_element(By.XPATH, '//*[@id="email"]')
select_field.send_keys('ha11031989@gmail.com')
select_field = driver.find_element(By.XPATH, '//*[@id="password"]')
select_field.send_keys('Ha112002')
time.sleep(15)

wait = WebDriverWait(driver, 10)
select_field  = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn.button-custom')))
select_field .click()


# select_field = driver.find_element(By.CLASS_NAME, 'btn.button-custom')
# select_field.click()
time.sleep(5)
list = ["Afghanistan"]
select_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/crypt-root/div/div/div/crypt-shop-page/div/crypt-shop-panel/section/div[2]/div[2]/crypt-countries-dropdown/div/a/span[3]')))
select_field.click()
select_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/crypt-root/div/div/div/crypt-shop-page/div/crypt-shop-panel/section/div[2]/div[2]/crypt-countries-dropdown/div/div/crypt-countries-select/div/ul/li[1]/a/div[2]/div')))
select_field.click()
# Tìm thẻ div
time.sleep(2)
my_div = driver.find_element(By.CLASS_NAME,"brands-list__container.ng-star-inserted")

# Tìm tất cả các thẻ li bên trong thẻ div
my_lis = my_div.find_elements(By.TAG_NAME,"li")
start_url = driver.current_url

for i in range (0,len(my_lis)):
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"brands-list__container.ng-star-inserted")))
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"li")))
    my_div_tmp = driver.find_element(By.CLASS_NAME,"brands-list__container.ng-star-inserted")
    my_lis_tmp = my_div_tmp.find_elements(By.TAG_NAME,"li")
    temp = my_lis_tmp[i].find_element(By.CLASS_NAME,"brand-item__image-container")
    temp.click()
    time.sleep(1)
    area_redeem_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[3]")))
    area_redeem = area_redeem_element.text

    # delivery
    delivery_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[2]")))
    delivery = delivery_element.text
    
    # title
    title_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[1]/div[1]/div/div[2]/h1")))
    title = title_element.text
    
    # img
    img_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[1]/div[1]/div/div[1]/div/img")))
    img = img_element.get_attribute("src")
    
    # country name 
    country = list[0]
    
    # type 
    type_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/ol/li[3]/a/span")))
    type = type_element.text
    
    # content
    content_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[1]/div[2]/div/div[2]/div")))
    content = content_element.text
    
    # desciption
    check_description_element = driver.find_elements(By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[1]/div[2]/div/div[2]/p-accordion/div/p-accordiontab[1]/div/div[1]/a/h2")
    if check_description_element:
        decription_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[1]/div[2]/div/div[2]/p-accordion/div/p-accordiontab[1]/div/div[2]/div/div/p")))
        decription = decription_element.text


    # <--Add to cart-->  
    add_to_cart_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[2]/div[2]/crypt-product-dynamic-preview/div/div[3]/button")))
    add_to_cart_element.click()
    
    # bấm vào list định giá 
    pricing_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[2]/p-dropdown/div/span")))
    pricing_element.click()
    # Lấy danh sách các loại tiền
    pricing_container = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[2]/p-dropdown/div/div[3]/div/ul")))
    list_pricing = pricing_container.find_elements(By.CSS_SELECTOR, "li.p-ripple.p-element.p-dropdown-item")
    
    # Lấy url trang thanh toán
    pricing_url = driver.current_url

    # Duyệt từng loại tiền
    for m in range (0,len(list_pricing)): 

        # Nếu không phải loại đầu thì click lại để lấy dại danh sách
        if m != 0 :    
            pricing_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[2]/p-dropdown/div/span")))
            pricing_element.click()
            pricing_container = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[2]/p-dropdown/div/div[3]/div/ul")))
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.p-ripple.p-element.p-dropdown-item")))
        list_pricing_tmp = pricing_container.find_elements(By.CSS_SELECTOR, "li.p-ripple.p-element.p-dropdown-item")
        print(len(list_pricing_tmp))
        # Chọn lọi tiền thứ
        list_pricing_tmp[m].click()
        text_pricing =list_pricing_tmp[m].text

        # pricing_element
        # bấm vào list network 
        network_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[3]/p-dropdown/div/span")))
        network_element.click()

        # chọn network
        # div_ = driver.find_element(By.CLASS_NAME, "cart-content__coins.ng-star-inserted")
        div_ = driver.find_elements(By.CLASS_NAME, "cart-content__coins.ng-star-inserted")
        li_ = div_[1].find_elements(By.TAG_NAME, "li")
        network_url = driver.current_url
        for n in range (0,len(li_)): 
            
            if n != 0 :
                pricing_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[2]/p-dropdown/div/span")))
                pricing_element.click()
                pricing_container = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[2]/p-dropdown/div/div[3]/div/ul")))
                wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.p-ripple.p-element.p-dropdown-item")))
                list_pricing_tmp_1 = pricing_container.find_elements(By.CSS_SELECTOR, "li.p-ripple.p-element.p-dropdown-item")
                print(len(list_pricing_tmp))
                list_pricing_tmp_1[m].click()


                network_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[3]/p-dropdown/div/span")))
                network_element.click()
                # chọn network
                wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"cart-content__coins.ng-star-inserted")))
                div_ = driver.find_elements(By.CLASS_NAME, "cart-content__coins.ng-star-inserted")
            list_network_tmp = div_[1].find_elements(By.TAG_NAME, "li")
            list_network_tmp[n].click()
            x = list_network_tmp[n].text
            time.sleep(2)
            proceed_to_checkout = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[4]/div/div/button")))
            proceed_to_checkout.click()
            copy_address = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-payment-page/div/div/div/div/crypt-payment-cart/div/div[2]/div/div[2]/div[3]/div[3]/div[2]/a")))
            copy_address.click()
            pyautogui.hotkey('ctrl', 'v')
            # Lưu văn bản đã paste vào biến tex
            # Lấy dữ liệu từ clipboard
            text = []
            text = pyperclip.paste()
            address_dict = {x: text}

            rs = rs + {text_pricing : address_dict}
            print(json.dumps(rs))
            driver.get(network_url)
            time.sleep(1)
        
        driver.get(url = pricing_url)


    
    # return_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[1]/a")))
    # return_element.click()        
    # driver.get(url=start_url)


    
    # return_button = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[1]/a")))
    # return_button.click()

    
time.sleep(2)