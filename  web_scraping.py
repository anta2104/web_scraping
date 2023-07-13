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
import os
driver = webdriver.Chrome()
# Đăng nhập
driver.get('https://www.cryptorefills.com/login')
select_field = driver.find_element(By.XPATH, '//*[@id="email"]')
select_field.send_keys('ha11031989@gmail.com')
select_field = driver.find_element(By.XPATH, '//*[@id="password"]')
select_field.send_keys('Ha112002')
# Đợi 15s để nhập catcha
time.sleep(15)

# Ấn vào danh sách QG
wait = WebDriverWait(driver, 10)
select_field  = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn.button-custom')))
select_field .click()

# select_field = driver.find_element(By.CLASS_NAME, 'btn.button-custom')
# select_field.click()
time.sleep(5)
list = ["Afghanistan"]
# Chọn QG
select_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/crypt-root/div/div/div/crypt-shop-page/div/crypt-shop-panel/section/div[2]/div[2]/crypt-countries-dropdown/div/a/span[3]')))
select_field.click()
select_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/crypt-root/div/div/div/crypt-shop-page/div/crypt-shop-panel/section/div[2]/div[2]/crypt-countries-dropdown/div/div/crypt-countries-select/div/ul/li[1]/a/div[2]/div')))
select_field.click()
time.sleep(1)
# Tìm thẻ div
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"brands-list__container.ng-star-inserted")))
my_div = driver.find_element(By.CLASS_NAME,"brands-list__container.ng-star-inserted")

# Tìm tất cả các thẻ li bên trong thẻ div đe 
my_lis = my_div.find_elements(By.TAG_NAME,"li")

# Lấy url trang hiện tại
start_url = driver.current_url

# Duyệt qua từng loại product
for i in range (0,len(my_lis)):

    # Lấy lại list các thẻ li 
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"brands-list__container.ng-star-inserted")))
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME,"li")))
    my_div_tmp = driver.find_element(By.CLASS_NAME,"brands-list__container.ng-star-inserted")
    my_lis_tmp = my_div_tmp.find_elements(By.TAG_NAME,"li")

    # chọn vào sản phẩm thứ i
    temp = my_lis_tmp[i].find_element(By.CLASS_NAME,"brand-item__image-container")
    item = temp.text
    temp.click()
    time.sleep(1)

    # Area
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
        # Chọn lọai tiền thứ m
        list_pricing_tmp[m].click()
        text_pricing =list_pricing_tmp[m].text


        # Lấy thông tin của item
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cart-products__field--product')))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cart-products__field--amount div:first-child')))
        value = driver.find_elements(By.CSS_SELECTOR, '.cart-products__field--product')
        prices = driver.find_elements(By.CSS_SELECTOR, '.cart-products__field--amount div:first-child')
        point = driver.find_element(By.CSS_SELECTOR,'.cart-products__field--points span:last-child')
        list_dict_item =[]
        # Lặp qua các phần tử trong cart để lấy thông tin
        for j in range (0,len(prices)):
            list_dict_item.append({
                                   "value" : value[j].text,
                                   "point_plus" : point.text,
                                   "price" : prices[j].text.split()[0]
                                  })

        # bấm vào list network 

        list_address_dict = []
        network_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[3]/p-dropdown/div/span")))
        network_element.click()

        # chọn network
        # div_ = driver.find_element(By.CLASS_NAME, "cart-content__coins.ng-star-inserted")
        div_ = driver.find_elements(By.CLASS_NAME, "cart-content__coins.ng-star-inserted")
        li_ = div_[1].find_elements(By.TAG_NAME, "li")
        rs = {}
        network_url = driver.current_url
        for n in range (0,len(li_)): 
            
            if n != 0 :
                pricing_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[2]/p-dropdown/div/span")))
                pricing_element.click()
                pricing_container = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[2]/p-dropdown/div/div[3]/div/ul")))
                wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.p-ripple.p-element.p-dropdown-item")))
                list_pricing_tmp_1 = pricing_container.find_elements(By.CSS_SELECTOR, "li.p-ripple.p-element.p-dropdown-item")
                list_pricing_tmp_1[m].click()


                network_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[3]/p-dropdown/div/span")))
                network_element.click()
                # chọn network
                wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"cart-content__coins.ng-star-inserted")))
                div_ = driver.find_elements(By.CLASS_NAME, "cart-content__coins.ng-star-inserted")
            list_network_tmp = div_[1].find_elements(By.TAG_NAME, "li")
            list_network_tmp[n].click()
            
            x = list_network_tmp[n].text
            time.sleep(1)
            proceed_to_checkout = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[4]/div/div/button")))
            proceed_to_checkout.click()
            copy_address = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-payment-page/div/div/div/div/crypt-payment-cart/div/div[2]/div/div[2]/div[3]/div[3]/div[2]/a")))
            copy_address.click()
            pyautogui.hotkey('ctrl', 'v')
            # Lưu văn bản đã paste vào biến tex
            # Lấy dữ liệu từ clipboard
            text = []
            text = pyperclip.paste()
            address_dict = {x:text}
            list_address_dict.append(address_dict)

            # rs={text_pricing : address_dict}
            # print(json.dumps(rs))
            driver.get(network_url)
            time.sleep(1)
        tmp_dict = {
            "wallet_address" : list_address_dict,
            "area_redeem": area_redeem,
            "delivery": delivery,
            "title": title,
            "country": country,
            "img": img,
            "type": type,
            "content": content,
            "description": decription,
            "items": list_dict_item
        }
        rs = {
            text_pricing : {
                 item : [tmp_dict] 
                }
        }
        data = []
        if os.stat("data.json").st_size != 0:
            with open('data.json', 'r') as f:
                data = json.load(f)
        data.append(rs)
        with open("data.json", "w") as f:
            json.dump(data, f)
        
        # Về trang chọn loại và ví
        driver.get(url = pricing_url)


    # Back về trang đầu       
    driver.get(url=start_url)



    
time.sleep(2)