from anticaptchaofficial.recaptchav2proxyon import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import sys



option = Options()
# option.add_argument('--headless') # VPS Mode
# option.add_argument('--disable-gpu')  # Last I checked this was necessary. # VPS Mode
# option.add_argument('--no-sandbox') # VPS Mode
option.add_argument("--start-maximized")
#option.add_argument("--remote-debugging-port=9222")  # Use an arbitrary port number
option.add_experimental_option("detach", False)  # Keep the browser window open after exiting the script
option.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

url = "https://google.com/recaptcha/api2/demo"
page = driver.get(url)

sitekey = driver.find_element(By.XPATH, '//*[@id="recaptcha-demo"]').get_attribute('outerHTML')
sitekey_clean = sitekey.split('" data-callback')[0].split('data-sitekey="')[1]
print(sitekey_clean)

solver = recaptchaV2Proxyon()
solver.set_verbose(1)
solver.set_key('67104f9c4d1f29804f41b9d37a30d3e7')
solver.set_website_url(url)
solver.set_website_key(sitekey_clean)
#set optional custom parameter which Google made for their search page Recaptcha v2
#solver.set_data_s('"data-s" token from Google Search results "protection"')

# DO NOT USE PURCHASED/RENTED PROXIES ON PROXY SERVICES!!!
# THEY WILL NOT WORK!
# USE ONLY PROXIES YOU INSTALL YOURSELF ON YOUR OWN SERVER OR FAST VPS
# USE PROPER PROXY SOFTWARE LIKE SQUID !
# INSTALLATION INSTRUCTIONS:
# https://anti-captcha.com/apidoc/articles/how-to-install-squid
solver.set_proxy_address("91.107.220.223")
solver.set_proxy_port(443)
solver.set_proxy_login("mylogin")
solver.set_proxy_password("mypassword")
solver.set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
solver.set_cookies("test=true")

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)


g_response = solver.solve_and_return_solution()
if g_response!= 0:
    print("g_response"+g_response)
else:
    print("task finished with error"+solver.error_code)

driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')
time.sleep(10)
driver.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", g_response)
time.sleep(10)
driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="recaptcha-demo-submit"]').click()

time.sleep(60)

driver.implicitly_wait(3)
message = driver.find_element(By.CLASS_NAME, 'recaptcha-success')
print(message.text)

time.sleep(20)