import sys
import time
import telebot
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from anticaptchaofficial.recaptchav2proxyon  import *
from country_selector import id_selector
from termcolor import colored, cprint
from typing import Final
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

# Initialize the bot with your bot token
bot_token = "5889078485:AAEe7G8zffK0ZVVBt0gQBcmi_yWm_zjZ7Yg"
BOT_USERNAME: Final = '@Status_GMT_Bot'
bot = telebot.TeleBot(bot_token)

ADMIN_USER_ID: Final = 5355774833  # Admin's user ID
group_chat_id: Final = -1001636295549



#chrome_driver_path = "C:/SeleniumDrivers/chromedriver.exe" # windows
chrome_driver_path = "/usr/local/bin/chromedriver" # linux

# option = webdriver.ChromeOptions()
option = Options()
option.page_load_strategy = 'normal'
option.add_argument('--headless') # VPS Mode
option.add_argument('--disable-gpu')  # Last I checked this was necessary. # VPS Mode
option.add_argument('--no-sandbox') # VPS Mode
option.add_argument('--disable-dev-shm-usage') # VPS Mode
option.add_argument("--start-maximized")
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

browser = None
service_path = None

booking_time_offer_1 = '09:00'
booking_time_offer_2 = '09:30'

firstname = 'Soudeh'
lastname = 'JavadiMasoudian'
dob = '03.09.1985' # DD.MM.YYYY
email = 'soudeh.masoudian@gmail.com'
id_card_number = ''
citizenship = "Iran, Islamic Republic"
nr_applicants = 'one person'
with_family_live = 'yes'
family_citizenship = 'Iran, Islamic Republic'
residence_title = "Apply for a residence title"
category = "Family reasons"
request_type = "Residence permit for spouses, parents and children of foreign citizens (sect. 29-34)"




i = 0
is_loop = 'true'
final_status = 'true'


def error_handler(exctype, value, traceback):
    # Your error handling function
    # This function will be called whenever an error occurs

    # Print the error message
    logging.error(f"Error--A: {value}")

    # You can perform additional actions here, such as logging the error


# Register the error handler function
sys.excepthook = error_handler


def send_message_to_admin(admin_chat_id, message):
    # replace 'ADMIN_CHAT_ID' with the chat id of the admin
    bot.send_message(admin_chat_id, message, parse_mode='Markdown')



# Open Browser
def open_browser():
    global browser
    global service_path
    # terminal_text = colored('Open Browser function, executed', 'green', attrs=['bold'])
    # print(terminal_text)
    logging.info('Open Browser function, executed')
    service_path = Service(executable_path=chrome_driver_path)
    browser = webdriver.Chrome(service=service_path, options=option)
    #browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    browser.get("https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en")


def main_process():
    logging.info('Waiting for Book Appointment btn ...')
    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a[href="/ams/TerminBuchen/wizardng?sprachauswahl=en"]'),
                                         'Book Appointment'))
    browser.implicitly_wait(3)
    browser.find_element(By.CSS_SELECTOR, 'a[href="/ams/TerminBuchen/wizardng?sprachauswahl=en"]').click()
    logging.info('Book Appointment btn passed')

    # Mark checkbox and Next Buttom 
    browser.implicitly_wait(30)
    browser.find_element(By.ID, 'xi-cb-1').click()
    browser.implicitly_wait(10)
    browser.find_element(By.ID, 'applicationForm:managedForm:proceed').click()
    logging.info('CheckBox marked and the next buttom clicked')

    
# The information page related to specifying the nationality and type of application   
def nationality_selection(arg1, arg2, arg3, arg4):
    browser.implicitly_wait(30)
    element_dropdown1 = browser.find_element(By.ID, 'xi-sel-400')
    time.sleep(0.3)
    element_dropdown1.click()
    time.sleep(0.3)
    select1 = Select(element_dropdown1)
    # Iran, Islamic Republic
    # India
    select1.select_by_visible_text(arg1)
    logging.info(arg1)

    time.sleep(0.3)

    element_dropdown2 = browser.find_element(By.ID, 'xi-sel-422')
    time.sleep(0.3)
    element_dropdown2.click()
    time.sleep(0.3)
    select2 = Select(element_dropdown2)
    # one person
    # three people
    select2.select_by_visible_text(arg2)
    logging.info(arg2)

    time.sleep(0.3)
    
    element_dropdown3 = browser.find_element(By.ID, 'xi-sel-427')
    time.sleep(0.3)
    element_dropdown3.click()
    time.sleep(0.3)
    select3 = Select(element_dropdown3)
    # yes/no
    select3.select_by_visible_text(arg3)
    logging.info(arg3)

    time.sleep(0.3)
    
    if arg3 == 'yes':
        element_dropdown4 = browser.find_element(By.ID, 'xi-sel-428')
        time.sleep(0.3)
        element_dropdown4.click()
        time.sleep(0.3)
        select4 = Select(element_dropdown4)
        # Iran, Islamic Republic
        # India
        select4.select_by_visible_text(arg4)
        logging.info(arg4)
        time.sleep(0.3)

def select_type_of_residency(arg1, arg2, arg3):

    global is_loop
    global final_status
    is_loop_1 = 'true'
    try_count = 0
    id_array = ['','','']

    for i in range(3):
        id_array[i] = id_selector(citizenship, residence_title, category, request_type)[i]


    # Select type of residency (arg1)
    # Apply for a residence title
    # Extend a residence title
    apply_residence = browser.find_element(By.CLASS_NAME, id_array[0])
    browser.implicitly_wait(3)
    apply_residence.click()
    logging.info(arg1)
    time.sleep(0.3)
    # Select Category (arg2)
    # Family reasons
    # Economic activity
    browser.implicitly_wait(3)
    family_reasons = browser.find_element(By.CLASS_NAME, id_array[1])
    browser.implicitly_wait(3)
    family_reasons.click()
    logging.info(arg2)

    time.sleep(1)
    # Select request type (arg3)
    # Residence permit for spouses and children of skilled workers, students, trainees, scientists and teachers (sect. 29-32)
    # Residence permit for spouses, parents and children of foreign citizens (sect. 29-34)
    student = browser.find_element(By.ID, id_array[2])
    browser.implicitly_wait(3)
    student.click()
    logging.info(arg3)
    # browser.implicitly_wait(30)

    # WebDriverWait(browser, 60).until_not(
    #     EC.text_to_be_present_in_element((By.ID, 'messagesBox'), 'There are currently no dates available for the selected service! Please try again later.'))
           
    for i in range(60):
        time.sleep(1)
        loading_item = browser.find_element(By.CLASS_NAME, 'loading').get_attribute('outerHTML')
        is_loading = loading_item.split(';">')[0].split('opacity: ')[1]
        #logging.info(is_loading)
        if is_loading == '1':
            loading_time_1 = i*1
            logging.info(f"The Loading time was {loading_time_1} secounds")
            time.sleep(2)
            loading_item = browser.find_element(By.CLASS_NAME, 'loading').get_attribute('outerHTML')
            is_loading = loading_item.split(';">')[0].split('opacity: ')[1]
            if is_loading == '1':
                logging.info("I'm sure loading is finished")
                break 
        
    browser.implicitly_wait(3)
    condition = browser.find_element(By.ID, 'messagesBox')
    if condition.text == 'There is currently no information available for the selected service. Please try again later.':
        logging.info(condition.text)
        is_loop = 'false'
        final_status = 'false'
        raise ElementNotInteractableException
        

    if not condition.text == 'There are currently no dates available for the selected service! Please try again later.':
        logging.info('Dates available for the selected service!')
        browser.implicitly_wait(3)
        next_btn = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
        next_btn.click()
        logging.info('Next buttom Clicked')

    condition = browser.find_element(By.ID, 'messagesBox')
    if condition.text == 'There are currently no dates available for the selected service! Please try again later.':

        while is_loop_1 == 'true': 
            time.sleep(1)
            browser.implicitly_wait(3)
            apply_residence = browser.find_element(By.CLASS_NAME, id_array[0])
            browser.implicitly_wait(3)
            apply_residence.click()
            logging.info(arg1)
            time.sleep(0.3)

            browser.implicitly_wait(3)
            family_reasons = browser.find_element(By.CLASS_NAME, id_array[1])
            browser.implicitly_wait(3)
            family_reasons.click()
            logging.info(arg2)

            time.sleep(1)

            student = browser.find_element(By.ID, id_array[2])
            browser.implicitly_wait(3)
            student.click()
            logging.info(arg3)

            for i in range(60):
                time.sleep(1)
                loading_item = browser.find_element(By.CLASS_NAME, 'loading').get_attribute('outerHTML')
                is_loading = loading_item.split(';">')[0].split('opacity: ')[1]
                #logging.info(is_loading)
                if is_loading == '1':
                    loading_time_2 = i*1
                    logging.info(f"The Loading time was {loading_time_2} secounds")
                    time.sleep(2)
                    loading_item = browser.find_element(By.CLASS_NAME, 'loading').get_attribute('outerHTML')
                    is_loading = loading_item.split(';">')[0].split('opacity: ')[1]
                    if is_loading == '1':
                        logging.info("I'm sure loading is finished")
                        break 

            browser.implicitly_wait(3)
            condition = browser.find_element(By.ID, 'messagesBox')

            if not condition.text == 'There are currently no dates available for the selected service! Please try again later.':
                logging.info('Dates available for the selected service!')
                browser.implicitly_wait(3)
                next_btn = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
                next_btn.click()
                logging.info('Next buttom Clicked')
                is_loop_1 = 'false'

            if condition.text == 'There are currently no dates available for the selected service! Please try again later.':
                is_loop_1 = 'true'
                logging.info('loop continue')
                try_count += 1
                logging.info(f'Try Count:{try_count}')




def service_selection():
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "fieldset[id='xi-fs-2'] legend"), 'Appointment selection')
    )
    # terminal_text = colored('Service selection page is loaded completely', 'yellow', attrs=['reverse', 'bold'])
    # print(terminal_text)
    logging.info('*** Service selection page is loaded completely ***')


def recaptcha_solver():
    get_url = browser.current_url
    logging.info("The current url is:" + str(get_url))


    sitekey = browser.find_element(By.XPATH, '//*[@id="xi-div-4"]').get_attribute('outerHTML')
    sitekey_clean = sitekey.split('" data-xm-appendable')[0].split('data-sitekey="')[1]
    logging.info(sitekey_clean)

    solver = recaptchaV2Proxyon()
    solver.set_verbose(1)
    solver.set_key('67104f9c4d1f29804f41b9d37a30d3e7')
    solver.set_website_url(get_url)
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

   

    g_response = solver.solve_and_return_solution()
    if g_response != 0:
        logging.info("g_response" + g_response)
    else:
        logging.info("task finished with error" + solver.error_code)



    time.sleep(20)
    browser.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display-"";')
    time.sleep(1)
    browser.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", g_response)
    time.sleep(1)
    browser.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')
    time.sleep(1)
    # browser.find_element(By.XPATH, '//*[@id="recaptcha-demo-submit"]').click()


def date_time_selection(arg1, arg2):
    # time.sleep(2)
    global option
    try:
        browser.implicitly_wait(3)
        select_day = browser.find_element(By.XPATH, '//td[@data-handler="selectDay"]')
        select_month = browser.find_element(By.XPATH, '//*[@id="xi-div-2"]/div/div[1]/div/div/span')
        browser.implicitly_wait(3)
        logging.info(f'The selected date is {select_day.text} {select_month.text} day of the month')
        select_day.click() #in comment shod choon gharar nist automatic book beshe
    except NoSuchElementException:
        logging.info('We got to the date selection page, but unfortunately there are no dates to choose from.')
        browser.quit()
        open_browser()
        main_process()

    dropdown_menu_is_open = browser.find_element(By.XPATH,
                                                 '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/fieldset[1]/div[1]/select[1]')

    # try:
    for i in range(600):  # Create Time Delay for open the page complete
        if not (dropdown_menu_is_open.text == 'Please select'):
            logging.info(f'The (Time selection) part is loaded completely now. After {(i + 1) * 0.1} Second')
            break
        else:
            logging.info(i)
    time.sleep(0.1)

    dropdown_menu = Select(browser.find_element(By.ID, 'xi-sel-3'))
    for option in dropdown_menu.options:
        # print(option.text, option.get_attribute('value'))
        logging.info(option.text)
        if option.text == arg1:
            break
        elif option.text == arg2:
            break

    logging.info(f'Selected booking time is {option.text}')
    dropdown_menu.select_by_visible_text(option.text) # in comment shod choon gharar nist automatic book beshe


    get_url = browser.current_url
    user_data = (
    f'''
Firstname: ```{firstname}``` 

Lastname: ```{lastname}``` 

Date of birth: ```{dob}``` 

Email: ```{email}``` 

ID Card Number: ```{id_card_number}```'''
    )
    

    url = f'[Appointment is available | Click to Book]({get_url})'
    send_message_to_admin(group_chat_id, url)
    send_message_to_admin(group_chat_id, user_data)

    # time.sleep(60)
    # browser.implicitly_wait(3)
    # next_button = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
    # next_button.click()

    # Recaptcha
    recaptcha_solver()

def import_personal_data(arg1, arg2, arg3, arg4, arg5):
    # print('wait till 15 min')
    # time.sleep(15)
    # print('finished')
    WebDriverWait(browser, 360).until(EC.text_to_be_present_in_element((By.XPATH,
                                                                       '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/fieldset[1]/div[1]/div[1]/label[1]/p[1]'),
                                                                      'First name*'))
    # test_1 = browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/fieldset[1]/div[1]/div[1]/label[1]/p[1]')
    # print(f'avali', {test_1.text})
    logging.info('reCaptcha is Solved')
    browser.implicitly_wait(10)
    firstname = browser.find_element(By.ID, 'xi-tf-3')
    lastname = browser.find_element(By.ID, 'xi-tf-4')
    dob = browser.find_element(By.ID, 'xi-tf-5')
    email = browser.find_element(By.ID, 'xi-tf-6')
    # question_field_1 = browser.find_element(By.ID, 'xi-sel-2')
    ausweisnummer = browser.find_element(By.ID, 'xi-tf-21')

    firstname.send_keys(arg1)
    logging.info(arg1)
    lastname.send_keys(arg2)
    logging.info(arg2)
    dob.send_keys(arg3) # MM/DD/YYYY or DD.MM.YYYY
    logging.info(arg3)
    email.send_keys(arg4)
    logging.info(arg4)
    ausweisnummer.send_keys(arg5)
    logging.info(arg5)
    # element_dropdown = Select(browser.find_element(By.ID, 'xi-sel-2'))
    # element_dropdown.select_by_visible_text('no')
    time.sleep(10)
    browser.implicitly_wait(3)
    next_button = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
    next_button.click()

    # browser.implicitly_wait(50)
    # submit_button = browser.find_element(By.ID, 'summaryForm:proceed')
    # submit_button.click()






# # bot receives all updates
# @bot.message_handler(func=lambda m: True)
# def print_chat_id(message):
#     print(message.chat.id)
# bot.polling()


# Example usage

while is_loop == 'true':
    try:
        open_browser()
        main_process()
        nationality_selection(citizenship, nr_applicants, with_family_live, family_citizenship)
        select_type_of_residency(residence_title, category, request_type)
        service_selection()
        date_time_selection(booking_time_offer_1, booking_time_offer_2)
        is_loop = 'false'
        import_personal_data(firstname, lastname, dob, email, id_card_number)
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

if final_status == 'true': 
    logging.info('--Congratulations! your booking has been done successfully--')
else:
   logging.info('--We are out of hours and there are no appointments to book--') 
