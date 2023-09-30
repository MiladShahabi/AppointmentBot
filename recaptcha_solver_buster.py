from anticaptchaofficial.recaptchav2proxyon import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.keys import Keys
import pyautogui
import os
import sys
import requests, time

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("recaptcha_log.log"),
        logging.StreamHandler()
    ]
)



option = Options()
option.page_load_strategy = 'normal'
# option.add_argument('--headless') # VPS Mode
# option.add_argument('--disable-gpu')  # Last I checked this was necessary. # VPS Mode
# option.add_argument('--no-sandbox') # VPS Mode
option.add_argument('--disable-dev-shm-usage') # VPS Mode
option.add_argument("--start-maximized")
#option.add_argument("--window-size=4320,7680") # we use it only for screenshot 
#option.add_argument("--remote-debugging-port=9222")  # Use an arbitrary port number
option.add_experimental_option("detach", False)  # Keep the browser window open after exiting the script
option.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"')

# Removes navigator.webdriver flag

# For older ChromeDriver under version 113.0.3945.16
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)

# For ChromeDriver version 79.0.3945.16 or over
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("--disable-notifications")
option.add_argument("--disable-popup-blocking")

option.add_extension("./buster.crx")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

# Navigate to page
driver.get('www.google.com')
time.sleep(10)
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='reCAPTCHA']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
time.sleep(2)
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.ENTER)
actions.perform()
ActionBuilder(driver).clear_actions()
time.sleep(5)
driver.implicitly_wait(3)
next_button = driver.find_element(By.ID, 'applicationForm:managedForm:proceed')
next_button.click()

time.sleep(70)












#===================================================2Captcha==========================================================


# API_KEY = '4580ef0ddcb65d2bc68f14809b5d0b63'
# data_sitekey = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'
# page_url = 'https://google.com/recaptcha/api2/demo'

# def reacaptcha_solver():
#     logging.info('start')
#     driver.get(page_url)
#     u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={data_sitekey}&pageurl={page_url}&json=1&invisible=1"
#     r1 = requests.get(u1)
#     print(r1.json())
#     rid = r1.json().get('request')
#     u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
#     time.sleep(1)
#     while True:
#         r2 = requests.get(u2)
#         print(r2.json())
#         if r2.json().get("status") == 1:
#             form_token = r2.json().get("request")
#             break
#         time.sleep(3)
#     logging.info('solved')
#     write_token_js = f'document.getElementById("g-recaptcha-response").innerHTML="{form_token}";'
#     submit_js = 'document.getElementById("recaptcha-demo-form").submit();'
#     driver.execute_script(write_token_js)
#     time.sleep(3)
#     driver.execute_script(submit_js)
#     time.sleep(10)

# if __name__ == '__main__':
#     reacaptcha_solver()
# #==================================================================================================================================