import sys
import time
import telebot
import random
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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from anticaptchaofficial.recaptchav2proxyless import *
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
bot_token_status_gmt_bot: Final = "5889078485:AAEe7G8zffK0ZVVBt0gQBcmi_yWm_zjZ7Yg"
bot_token_getmytermin: Final = "6114910026:AAGGPogroG1BvkHA3LOTab_0EzBqqi3JQYM"
BOT_USERNAME: Final = '@Status_GMT_Bot'
bot = telebot.TeleBot(bot_token_status_gmt_bot)

ADMIN_USER_ID: Final = 5355774833  # Admin's user ID
group_chat_id: Final = -1001636295549
channel_chat_id: Final = -1001826497482



#chrome_driver_path = "C:/SeleniumDrivers/chromedriver.exe" # windows
chrome_driver_path = "/usr/local/bin/chromedriver" # linux

# option = webdriver.ChromeOptions()
option = Options()
option.page_load_strategy = 'normal'
option.add_argument('--headless') # VPS Mode
option.add_argument('--disable-gpu')  # Last I checked this was necessary. # VPS Mode
option.add_argument('--no-sandbox') # VPS Mode
option.add_argument('--disable-dev-shm-usage') # VPS Mode
# option.add_argument("--start-maximized")
# option.add_argument("--window-size=4320,7680") # we use it only for screenshot 
#option.add_argument("--remote-debugging-port=9222")  # Use an arbitrary port number
option.add_experimental_option("detach", False)  # Keep the browser window open after exiting the script
option.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"')

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

booking_time_offer_1 = '08:30'
booking_time_offer_2 = '14:00'

booking_month_1st = 'December'
booking_month_2nd = 'December'
booking_month_3rd = 'January'

prefered_start_day = 1 # November
prefered_end_day = 30 # November
prefered_day = 'on' # off/on

USER_CHAT_ID: Final = 1112294786  # User's Chat ID
firstname = 'Harshit'
lastname = 'Kumar'
dob = '28.03.1997' # DD.MM.YYYY
process_number = '213062'
change_number = '6da8'



i = 0
is_loop = 'true'
block_condition = 0
is_block = False
is_solvedCaptcha = False
final_status = False
emoji_check_mark = u'\U00002705'
emoji_thanks = u'\U0001F64F'
emoji_bot = u'\U0001F916'
at = u'\U00000040'
point_down = u'\U0001f447'



def error_handler(exctype, value, traceback):
    # Your error handling function
    # This function will be called whenever an error occurs

    # Print the error message
    logging.error(f"Error--A: {value}")

    # You can perform additional actions here, such as logging the error
# Register the error handler function
sys.excepthook = error_handler

def send_message_to_telegram(admin_chat_id, message):
    # replace 'ADMIN_CHAT_ID' with the chat id of the admin
    bot.send_message(admin_chat_id, message, parse_mode='Markdown')

def send_message_to_user(user_chat_id_1, temp_message, bot_token):
    bot = telebot.TeleBot(bot_token)
    bot.send_message(user_chat_id_1, temp_message, parse_mode='None')    

def send_screenshot_to_telegram_channel(chat_id, snapshot_area, text):
    # Identify the element to screenshot by its ID (you can use XPATH, CSS selectors, etc.)
    snapshot_area = browser.find_element(By.ID, snapshot_area)  # Replace 'element-id' with the id of your element
    # Screenshot the element
    snapshot_area.screenshot('screenshot.png')
    with open('screenshot.png', 'rb') as photo:
        bot.send_photo(chat_id, photo)

    bot.send_message(chat_id, text)
        
    return "Screenshot sent!"

# Open Browser
def open_browser():
    global browser
    global service_path
    global is_block
    global block_condition

    block_condition += 1
    if block_condition > 3:
        is_block = True
    # terminal_text = colored('Open Browser function, executed', 'green', attrs=['bold'])
    # print(terminal_text)
    logging.info('Open Browser function, executed')
    service_path = Service(executable_path=chrome_driver_path)
    browser = webdriver.Chrome(service=service_path, options=option)
    #browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    browser.get("https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en")

def main_process():
    global is_block
    global block_condition

    logging.info('Waiting for Book Appointment btn ...')
    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a[href="/ams/TerminAendern/wizardng?sprachauswahl=en"]'), 
                                         'Change Appointment'))
    browser.implicitly_wait(3)
    browser.find_element(By.CSS_SELECTOR, 'a[href="/ams/TerminAendern/wizardng?sprachauswahl=en"]').click()
    logging.info('Change Appointment btn passed')

    block_condition = 0 # Reset
    is_block = False # loop continue

    #======================================================================================================================

def service_selection():
    WebDriverWait(browser, 60).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#xi-fs-22 > legend"), 'Personal and appointment details') 
    )
    # terminal_text = colored('Service selection page is loaded completely', 'yellow', attrs=['reverse', 'bold'])
    # print(terminal_text)
    logging.info('*** Personal and appointment details page loded compeletly ***')

def import_personal_data(arg1, arg2, arg3, arg4, arg5):  

    global find_day
    global find_month

    WebDriverWait(browser, 60).until(EC.text_to_be_present_in_element((By.XPATH,
                                                                       '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[1]/div[2]/div[1]/div[2]/div[6]/div[1]/div[2]/div[1]/fieldset[1]/div[1]/div[1]/label[1]/p[1]'),
                                                                      'First name*'))
    # test_1 = browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/fieldset[1]/div[1]/div[1]/label[1]/p[1]')
    # print(f'avali', {test_1.text})

    browser.implicitly_wait(10)
    firstname = browser.find_element(By.ID, 'xi-tf-948')
    lastname = browser.find_element(By.ID, 'xi-tf-949')
    dob = browser.find_element(By.ID, 'xi-tf-950')
    process_number = browser.find_element(By.ID, 'xi-tf-951')
    change_number = browser.find_element(By.ID, 'xi-tf-972')    
    

    firstname.send_keys(arg1)
    logging.info(arg1)
    lastname.send_keys(arg2)
    logging.info(arg2)
    dob.send_keys(arg3) # MM/DD/YYYY or DD.MM.YYYY
    logging.info(arg3)
    process_number.send_keys(arg4)
    logging.info(arg4)
    change_number.send_keys(arg5)
    logging.info(arg5)

    time.sleep(1)
    browser.implicitly_wait(3)
    next_button = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
    next_button.click()


def is_load_date_selection_page():
    WebDriverWait(browser, 60).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#xi-fs-2 > legend"), 'Appointment selection') 
    )
    # terminal_text = colored('Service selection page is loaded completely', 'yellow', attrs=['reverse', 'bold'])
    # print(terminal_text)
    logging.info('*** Appointment selection page loded compeletly ***')

def date_time_selection(arg1, arg2, arg3, arg4, arg5, start, stop, arg8, arg9, arg10):
    # time.sleep(2)
    global option
    global is_solvedCaptcha
    global final_status

    try:
        browser.implicitly_wait(3)
        select_day = browser.find_element(By.XPATH, '//td[@data-handler="selectDay"]')
        select_month = browser.find_element(By.XPATH, '//*[@id="xi-div-2"]/div/div[1]/div/div/span')
        browser.implicitly_wait(3)
        logging.info(f'The selected date is {select_day.text} {select_month.text} day of the month')
        find_day = select_day.text
        find_month = select_month.text

        if not select_month.text == arg3:
            logging.info(f"The month of {arg3} was not found in the findings")
            if not select_month.text == arg4:
                logging.info(f"The month of {arg4} was not found in the findings")
                if not select_month.text == arg5:
                    logging.info(f"The month of {arg5} was not found in the findings")
                    logging.info('++The available date is not in the selected months++')
                    raise NoSuchElementException 
        if not arg8 == 'select':
            if not stop >= int(select_day.text) >= start:   
                logging.warning('-->>>The founded slot is not in range to the preferred selected dates<<<--')
                raise NoSuchElementException
        time.sleep(3)
        browser.find_element(By.XPATH, '//td[@data-handler="selectDay"]').click() 
        #time.sleep(10)
    except NoSuchElementException:
        logging.info('We got to the date selection page, but unfortunately there are no dates to choose from.')
        raise NoSuchElementException 
        # browser.quit()
        # open_browser()
        # main_process()

    # try:
    for i in range(600):  # Create Time Delay for open the page complete
        browser.implicitly_wait(3)
        dropdown_menu_is_open = browser.find_element(By.XPATH,
                                                    '/html/body/div[2]/div[2]/div[4]/div[2]/form/div[2]/div/div[2]/div/div[2]/div[4]/div[1]/fieldset/div/select/option')
        if not (dropdown_menu_is_open.text == 'Please select'):
            logging.info('The (Time selection) part is loaded completely now.')
            break
        else:
            logging.info(i)
            if i == 500:
                logging.info('Time not available')
                raise ValueError
    # time.sleep(0.1)

    dropdown_menu = Select(browser.find_element(By.ID, 'xi-sel-5'))
    for option in dropdown_menu.options:
        # print(option.text, option.get_attribute('value'))
        logging.info(option.text)
        if option.text == arg1:
            break
        elif option.text == arg2:
            break

    logging.info(f'Selected booking time is {option.text}')
    dropdown_menu.select_by_visible_text(option.text)
    

    browser.implicitly_wait(3)
    next_button = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
    next_button.click()

    WebDriverWait(browser, 120).until(EC.text_to_be_present_in_element((By.XPATH,
                                                                       '/html/body/div[2]/div[2]/div[4]/div[2]/form[2]/div[2]/div/div[2]/div/div[1]/fieldset/legend'),
                                                                      'Appointment changing - Please check your data'))
    browser.implicitly_wait(1)
    is_check_data_page = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[4]/div[2]/form[2]/div[2]/div/div[2]/div/div[1]/fieldset/legend')
    logging.info(is_check_data_page.text)

    browser.implicitly_wait(100)
    submit_button = browser.find_element(By.ID, 'summaryForm:proceed')
    submit_button.click()
    logging.info('FINAL SUBMIT | clicked')
    final_status = True

    time.sleep(5)


    if find_day == '1':
        suffix = 'st'
    elif find_day == '2':
        suffix = 'nd'
    elif find_day == '3':
        suffix = 'rd'
    else:
        suffix = 'th'

    # Find the element by its class
    pdf_link = browser.find_element(By.CLASS_NAME, 'btnApplicationPdf').get_attribute('href')
    logging.info('PDF LINK ' + pdf_link)

    user_data = (
    f'''
Firstname: {arg9} 
Lastname: {arg10}

Date of Appointment has been changed to ({find_month} {find_day}{suffix})'''
    )
    

    url = f'[ PDF | Click to Download]({pdf_link})'
    send_message_to_telegram(group_chat_id, url)
    send_message_to_telegram(group_chat_id, user_data)
    logging.info('PDF link has been sent to Telegram group')


    inform_user_message = (f''' Dear {arg9} {arg10}, 
Your appointment date has been changed to ({find_month} {find_day}{suffix}) successfully, and the details of that have been sent to you via the official email of the Berlin Immigration Office. Please arrange the /payment of the 50 Euros fee within 24 hours otherwise your booking will be automatically canceled. 
If you have already paid, please ignore the payment request part.
Also you can download your appointment booking PDF from below link: 

{pdf_link}''')

    logging.info(inform_user_message)

    send_message_to_user(USER_CHAT_ID, inform_user_message, bot_token_getmytermin)
    send_message_to_user(ADMIN_USER_ID, inform_user_message, bot_token_getmytermin)


while is_loop == 'true':
    try:
        open_browser()
        main_process()
        service_selection()
        import_personal_data(firstname, lastname, dob, process_number, change_number) 
        is_load_date_selection_page()
        date_time_selection(booking_time_offer_1, booking_time_offer_2, booking_month_1st, booking_month_2nd, booking_month_3rd, prefered_start_day, prefered_end_day, prefered_day, firstname, lastname)
        is_loop = 'false'
    except Exception as e:
        # The error handler function will be automatically called here
        i += 1

        # logging.info(send_screenshot_to_telegram_channel(group_chat_id, 'main', 'Unsuccessful try'))

        # print(f"Unfortunately the Date is unavailable\nRepeated", {i}, "times")
        logging.warning('Unfortunately the Date is unavailable')
        logging.info(f'{i} attempts')
        if i > 800 or is_block == True:
            is_loop = 'false'
            bot_status_msg = (f'The Bot is out of service ({firstname})')
            logging.info(bot_status_msg)
            bot.send_message(group_chat_id, bot_status_msg)
        # Repeated", {i}, "times"
        # logging.error('Something bad happened')
        # is_loop = 'false'
        browser.quit()
        pass  # Or you can choose to handle the error further if needed

if final_status == True: 
    final_status = False
    only_once = True
    logging.info('--Congratulations! your booking has been done successfully--')

    i = 0
    random.seed()
    random_value = random.randrange(2, 5)

    while True:
        time.sleep(15) # each step is 15 second
        i += 1
        if i == random_value:
            if only_once == True:
                payment_request_msg = (f'''Hi {firstname} {lastname},                     
You can transfer the 50 euro fee for changing the date through the following account information and also send the related screenshot to the @GetMyTermin_Admin Telegram ID to confirm your payment.
{point_down}{point_down}{point_down}
IBAN : LT703250013955496479
Account Holder Name : GetMyTermin''')
                send_message_to_user(USER_CHAT_ID, payment_request_msg, bot_token_getmytermin)
                send_message_to_user(ADMIN_USER_ID, payment_request_msg, bot_token_getmytermin)
                only_once = False

        if i == 240: # 240 step is equal to 1 minute -> 240x15=3600
            i = 0
            bot_status_msg = (f"I'm still running please stop me so you can have more resources for other bots!\n++TASK NAME is: ({firstname})")
            logging.info(bot_status_msg)
            bot.send_message(group_chat_id, bot_status_msg)



else:
   logging.info('--We are out of hours and there are no appointments to book--') 
