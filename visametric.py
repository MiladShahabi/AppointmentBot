import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from anticaptchaofficial.recaptchav2proxyless import *
from termcolor import colored, cprint
from selenium_stealth import stealth
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

chrome_driver_path = "C:/SeleniumDrivers/chromedriver.exe"

# option = webdriver.ChromeOptions()
option = Options()
option.page_load_strategy = 'normal'
option.add_argument("--start-maximized")
#option.add_argument("--remote-debugging-port=9222")  # Use an arbitrary port number
# option.add_experimental_option("detach", True)  # Keep the browser window open after exiting the script
# option.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"')

# Removes navigator.webdriver flag

# For older ChromeDriver under version 113.0.3945.16
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)

# For ChromeDriver version 79.0.3945.16 or over
# option.add_argument('--disable-blink-features=AutomationControlled')
# option.add_argument("--disable-notifications")
# option.add_argument("--disable-popup-blocking")

global browser
global service_path

booking_time_offer_1 = '09:00'
booking_time_offer_2 = '12:00'

counrty_field_one = 'India'
counrty_field_two = 'India'

citizenship = 'India'
nr_applicants = 'three people'
where_live = 'yes'
family_citizenship = 'India'

i = 0


def error_handler(exctype, value, traceback):
    # Your error handling function
    # This function will be called whenever an error occurs

    # Print the error message
    logging.error(f"Error--A: {value}")

    # You can perform additional actions here, such as logging the error


# Register the error handler function
sys.excepthook = error_handler


# Open Browser
def open_browser():
    global browser
    global service_path
    # terminal_text = colored('Open Browser function, executed', 'green', attrs=['bold'])
    # print(terminal_text)
    logging.info('Open Browser function, executed')
    service_path = Service(executable_path=chrome_driver_path)
    browser = webdriver.Chrome(service=service_path, options=option)

    stealth(browser,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
    browser.get("https://www.visametric.com/iran/Germany/en/p/book-your-appointment")


# def main_process():


#     # WebDriverWait(browser, 20).until(
#     #     EC.text_to_be_present_in_element((By.CLASS_NAME, 'fancybox-close')))
#     # browser.find_element(By.CLASS_NAME, 'fancybox-close').click()



#     logging.info('Waiting for Book Appointment btn ...')
#     WebDriverWait(browser, 60).until(
#         EC.text_to_be_present_in_element((By.CLASS_NAME, 'p.btn-service:nth-child(9) > span:nth-child(1) > a:nth-child(1)'),
#                                          'مراحل انتصاب'))
#     browser.implicitly_wait(3)
#     browser.find_element(By.CLASS_NAME, 'fancybox-item fancybox-close').click()
#     logging.info('Book Appointment btn passed')

#     # CheckBox Mark and Next Buttom 

#     browser.implicitly_wait(30)
#     checkbox_mark = browser.find_element(By.ID, 'xi-cb-1')
#     checkbox_mark.click()
#     browser.implicitly_wait(10)
#     next_btn = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
#     next_btn.click()
#     logging.info('CheckBox marked and the next buttom clicked')

#     # The information page related to specifying the nationality and type of application   


# def nationality_selection(arg1, arg2, arg3, arg4):
#     browser.implicitly_wait(30)
#     element_dropdown1 = browser.find_element(By.ID, 'xi-sel-400')
#     time.sleep(0.3)
#     element_dropdown1.click()
#     time.sleep(0.3)
#     select1 = Select(element_dropdown1)
#     # Iran, Islamic Republic
#     # India
#     select1.select_by_visible_text(arg1)
#     logging.info(arg1)

#     time.sleep(0.3)

#     element_dropdown2 = browser.find_element(By.ID, 'xi-sel-422')
#     time.sleep(0.3)
#     element_dropdown2.click()
#     time.sleep(0.3)
#     select2 = Select(element_dropdown2)
#     # one person
#     # three people
#     select2.select_by_visible_text(arg2)
#     logging.info(arg2)

#     time.sleep(0.3)

#     element_dropdown3 = browser.find_element(By.ID, 'xi-sel-427')
#     time.sleep(0.3)
#     element_dropdown3.click()
#     time.sleep(0.3)
#     select3 = Select(element_dropdown3)
#     # yes/no
#     select3.select_by_visible_text(arg3)
#     logging.info(arg3)

#     time.sleep(0.3)

#     element_dropdown4 = browser.find_element(By.ID, 'xi-sel-428')
#     time.sleep(0.3)
#     element_dropdown4.click()
#     time.sleep(0.3)
#     select4 = Select(element_dropdown4)
#     # Iran, Islamic Republic
#     # India
#     select4.select_by_visible_text(arg4)
#     logging.info(arg4)
#     time.sleep(0.3)


# def select_type_of_residency(arg1, arg2, arg3):
#     # Select type of residency
#     # 'kachel-439-0-1'  ---> Apply for a residence title
#     # 'kachel-436-0-2'  ---> Extend a residence title
#     apply_residence = browser.find_element(By.CLASS_NAME, arg1)
#     browser.implicitly_wait(3)
#     apply_residence.click()
#     logging.info('Extend a residence title')
#     time.sleep(0.3)
#     # accordion-439-0-1-4 ---> Family reasons
#     # accordion-436-0-2-1 ---> Economic activity
#     browser.implicitly_wait(3)
#     family_reasons = browser.find_element(By.CLASS_NAME, arg2)
#     browser.implicitly_wait(3)
#     family_reasons.click()
#     logging.info('Economic activity')

#     time.sleep(1)
#     # SERVICEWAHL_EN439-0-1-4-327471 ---> Residence permit for spouses and children of skilled workers, students, trainees, scientists and teachers (sect. 29-32)
#     # SERVICEWAHL_EN439-0-1-4-305289 ---> Residence permit for spouses, parents and children of foreign citizens (sect. 29-34)
#     # SERVICEWAHL_EN436-0-2-1-329328 swati
#     student = browser.find_element(By.ID, arg3)
#     browser.implicitly_wait(3)
#     student.click()
#     logging.info('18b, para 1 - has been selected')
#     # browser.implicitly_wait(30)

#     time.sleep(15)

#     browser.implicitly_wait(3)
#     next_btn = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
#     next_btn.click()
#     logging.info('Next buttom Clicked')


# def service_selection():
#     WebDriverWait(browser, 15).until(
#         EC.text_to_be_present_in_element(
#             (By.CSS_SELECTOR, "fieldset[id='xi-fs-2'] legend"), 'Appointment selection')
#     )
#     # terminal_text = colored('Service selection page is loaded completely', 'yellow', attrs=['reverse', 'bold'])
#     # print(terminal_text)
#     logging.info('*** Service selection page is loaded completely ***')


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

#     g_response = solver.solve_and_return_solution()
#     if g_response != 0:
#         logging.info("g_response" + g_response)
#     else:
#         logging.info("task finished with error" + solver.error_code)

#     browser.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display-"";')
#     # time.sleep(0.1)
#     browser.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", g_response)
#     # time.sleep(0.1)
#     browser.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')
#     # time.sleep(0.1)
#     # browser.find_element(By.XPATH, '//*[@id="recaptcha-demo-submit"]').click()


# def date_time_selection():
#     # time.sleep(2)
#     global option
#     try:
#         browser.implicitly_wait(3)
#         select_day = browser.find_element(By.XPATH, '//td[@data-handler="selectDay"]')
#         select_month = browser.find_element(By.XPATH, '//*[@id="xi-div-2"]/div/div[1]/div/div/span')
#         browser.implicitly_wait(3)
#         logging.info(f'The selected date is {select_day.text} {select_month.text} day of the month')
#         select_day.click()
#     except NoSuchElementException:
#         logging.info('We got to the date selection page, but unfortunately there are no dates to choose from.')
#         browser.quit()
#         open_browser()
#         main_process()

#     dropdown_menu_is_open = browser.find_element(By.XPATH,
#                                                  '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/fieldset[1]/div[1]/select[1]')

#     # try:
#     for i in range(600):  # Create Time Delay for open the page complete
#         if not (dropdown_menu_is_open.text == 'Please select'):
#             logging.info(f'The (Time selection) part is loaded completely now. After {(i + 1) * 0.1} Second')
#             break
#         else:
#             logging.info(i)
#     time.sleep(0.1)

#     dropdown_menu = Select(browser.find_element(By.ID, 'xi-sel-3'))
#     for option in dropdown_menu.options:
#         # print(option.text, option.get_attribute('value'))
#         logging.info(option.text)
#         if option.text == booking_time_offer_1:
#             break
#         elif option.text == booking_time_offer_2:
#             break

#     logging.info(f'Selected booking time is {option.text}')
#     dropdown_menu.select_by_visible_text(option.text)

#     # Recaptcha
#     recaptcha_solver()

#     browser.implicitly_wait(3)
#     next_button = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
#     next_button.click()


# def import_personal_data():
#     # print('wait till 15 min')
#     # time.sleep(15)
#     # print('finished')
#     WebDriverWait(browser, 60).until(EC.text_to_be_present_in_element((By.XPATH,
#                                                                        '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/fieldset[1]/div[1]/div[1]/label[1]/p[1]'),
#                                                                       'First name*'))
#     # test_1 = browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/fieldset[1]/div[1]/div[1]/label[1]/p[1]')
#     # print(f'avali', {test_1.text})

#     browser.implicitly_wait(10)
#     firstname = browser.find_element(By.ID, 'xi-tf-3')
#     lastname = browser.find_element(By.ID, 'xi-tf-4')
#     dob = browser.find_element(By.ID, 'xi-tf-5')
#     email = browser.find_element(By.ID, 'xi-tf-6')
#     # question_field_1 = browser.find_element(By.ID, 'xi-sel-2')
#     # ausweisnummer = browser.find_element(By.ID, '')

#     firstname.send_keys('Swati')
#     lastname.send_keys('Jeevan')
#     dob.send_keys('23.07.1987')
#     email.send_keys('swatim234@gmail.com')
#     # ausweisnummer.send_keys('YX45HJS4')
#     element_dropdown = Select(browser.find_element(By.ID, 'xi-sel-2'))
#     element_dropdown.select_by_visible_text('no')
#     time.sleep(1)
#     browser.implicitly_wait(3)
#     next_button = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
#     next_button.click()

#     browser.implicitly_wait(50)
#     submit_button = browser.find_element(By.ID, 'summaryForm:proceed')
#     submit_button.click()


# Example usage
is_loop = 'true'
while is_loop == 'true':
    try:
        open_browser()
        # main_process()
        # nationality_selection(citizenship, nr_applicants, where_live, family_citizenship)
        # service_selection()
        # date_time_selection()
        # import_personal_data()
        is_loop = 'false'
    except Exception as e:
        # The error handler function will be automatically called here
        i += 1
        # print(f"Unfortunately the Date is unavailable\nRepeated", {i}, "times")
        logging.warning('Unfortunately the Date is unavailable')
        logging.info(f'{i} attempts')
        # Repeated", {i}, "times"
        # logging.error('Something bad happened')
        # is_loop = 'false'
        browser.quit()
        pass  # Or you can choose to handle the error further if needed

logging.info('--Congratulations! your booking has been done successfully--')
