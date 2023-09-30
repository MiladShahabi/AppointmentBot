from anticaptchaofficial.recaptchav2proxyless import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://google.com/recaptcha/api2/demo"
page = driver.get(url)

sitekey = driver.find_element(By.XPATH, '//*[@id="recaptcha-demo"]').get_attribute('outerHTML')
sitekey_clean = sitekey.split('" data-callback')[0].split('data-sitekey="')[1]
print(sitekey_clean)

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key('67104f9c4d1f29804f41b9d37a30d3e7')
solver.set_website_url(url)
solver.set_website_key(sitekey_clean)

g_response = solver.solve_and_return_solution()
if g_response!= 0:
    print("g_response"+g_response)
else:
    print("task finished with error"+solver.error_code)

driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display-"";')
time.sleep(2)
driver.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", g_response)
time.sleep(2)
driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="recaptcha-demo-submit"]').click()

time.sleep(20)







# def recaptcha_solver():

#     get_url = browser.current_url
#     logging.info("The current url is:" + str(get_url))


#     sitekey = browser.find_element(By.XPATH, '//*[@id="xi-div-4"]').get_attribute('outerHTML')
#     sitekey_clean = sitekey.split('" data-xm-appendable')[0].split('data-sitekey="')[1]
#     logging.info(sitekey_clean)

#     solver = recaptchaV2Proxyless()
#     solver.set_verbose(1)
#     solver.set_key('67104f9c4d1f29804f41b9d37a30d3e7')
#     solver.set_website_url(get_url)
#     solver.set_website_key(sitekey_clean)
#     #set optional custom parameter which Google made for their search page Recaptcha v2
#     #solver.set_data_s('"data-s" token from Google Search results "protection"')

#     # DO NOT USE PURCHASED/RENTED PROXIES ON PROXY SERVICES!!!
#     # THEY WILL NOT WORK!
#     # USE ONLY PROXIES YOU INSTALL YOURSELF ON YOUR OWN SERVER OR FAST VPS
#     # USE PROPER PROXY SOFTWARE LIKE SQUID !
#     # INSTALLATION INSTRUCTIONS:
#     # https://anti-captcha.com/apidoc/articles/how-to-install-squid
#     # solver.set_proxy_address("91.107.220.223")
#     # solver.set_proxy_port(443)
#     # solver.set_proxy_login("mylogin")
#     # solver.set_proxy_password("mypassword")
#     # solver.set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
#     # solver.set_cookies("test=true")

#     g_response = solver.solve_and_return_solution()
#     if g_response != 0:
#         logging.info("g_response" + g_response)
#     else:
#         logging.info("task finished with error" + solver.error_code)

#     browser.execute_script('''
#     var element = document.getElementById("g-recaptcha-response");
#     var style = element.getAttribute("style");
#     style = style.replace("display: none;", "/* display: none; */");
#     element.setAttribute("style", style);
#     ''')
#     #browser.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')
#     #time.sleep(30)
#     browser.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", g_response)
#     #time.sleep(10)
#     browser.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')
#     #time.sleep(10)
#     # browser.find_ele-ment(By.XPATH, '//*[@id="recaptcha-demo-submit"]').click()

