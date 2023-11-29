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
bot_token_status_gmt_bot: Final = "5889078485:AAEe7G8zffK0ZVVBt0gQBcmi_yWm_zjZ7Yg"
bot_token_getmytermin: Final = "6114910026:AAGGPogroG1BvkHA3LOTab_0EzBqqi3JQYM"
BOT_USERNAME: Final = '@Status_GMT_Bot'
bot = telebot.TeleBot(bot_token_status_gmt_bot)

ADMIN_USER_ID: Final = 5355774833  # Admin's user ID
group_chat_id: Final = -1001636295549
channel_chat_id: Final = -1001826497482



chrome_driver_path = "C:/SeleniumDrivers/chromedriver.exe" # windows
#chrome_driver_path = "/usr/local/bin/chromedriver" # linux

# option = webdriver.ChromeOptions()
option = Options()
option.page_load_strategy = 'normal'
# option.add_argument('--headless') # VPS Mode
# option.add_argument('--disable-gpu')  # Last I checked this was necessary. # VPS Mode
# option.add_argument('--no-sandbox') # VPS Mode
# option.add_argument('--disable-dev-shm-usage') # VPS Mode
option.add_argument("--start-maximized")
# option.add_argument("--window-size=4320,7680") # we use it only for screenshot 
option.add_argument("--remote-debugging-port=9222")  # Use an arbitrary port number
option.add_experimental_option("detach", False)  # Keep the browser window open after exiting the script
option.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"')

# Removes navigator.webdriver flag

# For older ChromeDriver under version 113.0.3945.16
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)

# For ChromeDriver version 79.0.3945.16 or over
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("--disable-notifications")
option.add_argument("--disable-popup-blocking")
option.add_extension("./buster.crx")

browser = None
service_path = None

booking_time_offer_1 = '08:00'
booking_time_offer_2 = '12:30'

booking_month_1st = 'October'
booking_month_2nd = 'November'
booking_month_3rd = 'Decemeber'

prefered_start_day = 1 # September
prefered_end_day = 30 # September
prefered_day = 'on' # off/on

USER_CHAT_ID: Final = 5686464021  # User's Chat ID
firstname = 'Balaganesh'
lastname = 'Duraisamy'
dob = '09.10.1976' # DD.MM.YYYY
email = 'bagaindian@gmail.com'
citizenship = "India"
nr_applicants = 'one person'
with_family_live = 'no'
family_citizenship = 'None'
residence_title = "Extend a residence title"
currently_have_a_residence = 'yes' # If selected Extend this item should be set 'no'
id_card_number = '066160727'
category = "Economic activity"
request_type = "EU Blue Card / Blaue Karte EU (sect. 18b para. 2)"


find_month = ''
find_day = ''
i = 0
block_condition = 0
is_block = False
is_solvedCaptcha = False
is_loop = 'true'
final_status = False
emoji_check_mark = u'\U00002705'
emoji_thanks = u'\U0001F64F'
emoji_bot = u'\U0001F916'
at = u'\U00000040'
point_down = u'\U0001f447'


message_in_channel = (f'''{emoji_check_mark} Appointment available
---------------------------------------------------------------
Title: 
{request_type}
---------------------------------------------------------------
{emoji_bot} If you have difficulty booking an appointment, our Telegram bot is always there to make it easy for you!

Telegram bot link :
@GetMyTermin_Bot
---------------------------------------------------------------
Thank you for following us.''')





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
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a[href="/ams/TerminBuchen/wizardng?sprachauswahl=en"]'),
                                         'Book Appointment'))
    browser.implicitly_wait(3)
    browser.find_element(By.CSS_SELECTOR, 'a[href="/ams/TerminBuchen/wizardng?sprachauswahl=en"]').click()
    logging.info('Book Appointment btn passed')

    block_condition = 0 # Reset
    is_block = False # loop continue

    # Mark checkbox and Next Buttom 
    browser.implicitly_wait(30)
    browser.find_element(By.ID, 'xi-cb-1').click()
    browser.implicitly_wait(10)
    browser.find_element(By.ID, 'applicationForm:managedForm:proceed').click()
    logging.info('CheckBox marked and the next buttom clicked')
   
# The information page related to specifying the nationality and type of application   
def nationality_selection(arg1, arg2, arg3, arg4):
    browser.implicitly_wait(60)
    time.sleep(1)
    element_dropdown1 = browser.find_element(By.ID, 'xi-sel-400')
    time.sleep(1)
    element_dropdown1.click()
    time.sleep(1)
    select1 = Select(element_dropdown1)
    # Iran, Islamic Republic
    # India
    time.sleep(0.5)
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

    #============================================================== New Method ===========================================
    # click when Next buttom is ready
    logging.info('is_loading_start')
    for i in range(120):
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
    logging.info('is_loading_end')

    next_btn = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
    next_btn.click()
    logging.info('Next buttom Clicked')
    try:
        WebDriverWait(browser, 50).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "fieldset[id='xi-fs-2'] legend"), 'Appointment selection')
        )
    except:
        logging.info('There are currently no dates available for the selected service! Please try again later.')
        # raise NoSuchElementException
        count = 0
        date_not_availale = 'true'
        while date_not_availale == 'true':
            logging.info('is_loading_start_inloop')
            next_btn = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
            next_btn.click()
            logging.info('Next buttom Clicked')
            count += 1
            if count > 10:
                raise NoSuchElementException
            logging.info(f'try count: {count}')
            wait = WebDriverWait(browser, 60)
            wait.until_not(EC.visibility_of_element_located((By.CLASS_NAME, "loading")))
            logging.info('is_loading_end_inloop')
            try:
                WebDriverWait(browser, 5).until(
                    EC.text_to_be_present_in_element(
                        (By.XPATH, '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[1]/div[2]/div[1]/div[2]/div[8]/div[2]/div[2]/div[1]/fieldset[1]/legend[1]'), 'Information about the concern')
                )
            except:
                date_not_availale = 'false'
                logging.info('*** Exit Loop ***')

    #======================================================================================================================

def service_selection():
    WebDriverWait(browser, 60).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "fieldset[id='xi-fs-2'] legend"), 'Appointment selection')
    )
    # terminal_text = colored('Service selection page is loaded completely', 'yellow', attrs=['reverse', 'bold'])
    # print(terminal_text)
    logging.info('*** Service selection page is loaded completely ***')

def recaptcha_solver():
    #========================================================== Buster.CRX =========================================================
    WebDriverWait(browser, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='reCAPTCHA']")))
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
    time.sleep(2)
    actions = ActionChains(browser)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(5)

    is_checkmark = browser.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]').get_attribute('outerHTML')
    is_checkmark_clean = is_checkmark.split('" role="')[0].split('rc-anchor-checkbox')[1]
    browser.switch_to.default_content()  # Switch back to the main frame
    if is_checkmark_clean == ' recaptcha-checkbox-focused recaptcha-checkbox-checked':
        logging.info('reCaptcha has been solved by BUSTER')
    else:
        #========================================================== 2Captcha algorithms ================================================
        logging.info(send_screenshot_to_telegram_channel(group_chat_id, 'xi-div-1', f'Status of auto reCaptcha solver\n{firstname} {lastname}'))
        actions = ActionChains(browser)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(1)
        browser.switch_to.default_content()  # Switch back to the main frame

        API_KEY = '4580ef0ddcb65d2bc68f14809b5d0b63'
        page_url = browser.current_url
        logging.info("The current url is:" + str(page_url))
        sitekey = browser.find_element(By.XPATH, '//*[@id="xi-div-4"]').get_attribute('outerHTML')
        sitekey_clean = sitekey.split('" data-xm-appendable')[0].split('data-sitekey="')[1]
        logging.info(sitekey_clean)

        u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={sitekey_clean}&pageurl={page_url}&json=1&invisible=1"
        r1 = requests.get(u1)
        print(r1.json())
        rid = r1.json().get('request')
        u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
        time.sleep(1)
        while True:
            r2 = requests.get(u2)
            print(r2.json())
            if r2.json().get("status") == 1:
                form_token = r2.json().get("request")
                break
            time.sleep(3)
        logging.info('2Captcha solved')

        browser.execute_script('''
        var element = document.getElementById("g-recaptcha-response");
        var style = element.getAttribute("style");
        style = style.replace("display: none;", "/* display: none; */");
        element.setAttribute("style", style);
        ''')
        browser.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", form_token)
        browser.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')
        logging.info('reCaptcha has been solved by 2Captcha')

def date_time_selection(arg1, arg2, arg3, arg4, arg5, start, stop, arg8):
    # time.sleep(2)
    global option
    global find_day
    global find_month
    global is_solvedCaptcha
    global allow_channel_notifications

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
        if not arg8 == 'off':
            if not stop >= int(select_day.text) >= start:   
                logging.warning('-->>>The founded slot is not in range to the preferred selected dates<<<--')
                raise NoSuchElementException
        select_day.click() 
                
    except NoSuchElementException:
        logging.info('We got to the date selection page, but unfortunately there are no dates to choose from.')
        raise NoSuchElementException 
        # browser.quit()
        # open_browser()
        # main_process()

    dropdown_menu_is_open = browser.find_element(By.XPATH,
                                                 '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/fieldset[1]/div[1]/select[1]')

    # try:
    for i in range(600):  # Create Time Delay for open the page complete
        if not (dropdown_menu_is_open.text == 'Please select'):
            logging.info(f'The (Time selection) part is loaded completely now. /*_*_*/')
            break
        else:
            logging.info(i)
            if i == 500:
                logging.info('Time not available')
                raise ValueError
    # time.sleep(0.1)

    dropdown_menu = Select(browser.find_element(By.ID, 'xi-sel-3'))
    for option in dropdown_menu.options:
        # print(option.text, option.get_attribute('value'))
        logging.info(option.text)
        if option.text == arg1:
            break
        elif option.text == arg2:
            break

    logging.info(f'Selected booking time is {option.text}')
    dropdown_menu.select_by_visible_text(option.text)


#     get_url = browser.current_url
#     user_data = (
#     f'''
# Firstname: ```{firstname}``` 

# Lastname: ```{lastname}``` 

# Date of birth: ```{dob}``` 

# Email: ```{email}``` 

# ID Card Number: ```{id_card_number}```'''
#     )
    

#     url = f'[Appointment is available | Click to Book]({get_url})'
#     send_message_to_telegram(group_chat_id, url)
#     send_message_to_telegram(group_chat_id, user_data)
    if allow_channel_notifications == True:
        logging.info(send_screenshot_to_telegram_channel(channel_chat_id, 'xi-div-1', message_in_channel))

    # Recaptcha
    recaptcha_solver()

    browser.implicitly_wait(3)
    next_button = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
    next_button.click()

    is_solvedCaptcha = True

    # time.sleep(7)
    # browser.implicitly_wait(3)
    # messagebox = browser.find_element(By.ID, 'messagesBox')
    # logging.warning(messagebox.text)

def import_personal_data(arg1, arg2, arg3, arg4, arg5, arg6, arg7):  

    global find_day
    global find_month
    global final_status

    WebDriverWait(browser, 150).until(EC.text_to_be_present_in_element((By.XPATH,
                                                                       '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/fieldset[1]/div[1]/div[1]/label[1]/p[1]'),
                                                                      'First name*'))
    # test_1 = browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/fieldset[1]/div[1]/div[1]/label[1]/p[1]')
    # print(f'avali', {test_1.text})

    browser.implicitly_wait(10)
    firstname = browser.find_element(By.ID, 'xi-tf-3')
    lastname = browser.find_element(By.ID, 'xi-tf-4')
    dob = browser.find_element(By.ID, 'xi-tf-5')
    email = browser.find_element(By.ID, 'xi-tf-6')
    if arg6 == 'Apply for a residence title':
        element_dropdown = Select(browser.find_element(By.ID, 'xi-sel-2'))
        time.sleep(0.5)
        visa_numberr = browser.find_element(By.ID, 'xi-tf-7')    
    elif arg6 == 'Extend a residence title':
        ausweisnummer = browser.find_element(By.ID, 'xi-tf-21')

    firstname.send_keys(arg1)
    logging.info(arg1)
    lastname.send_keys(arg2)
    logging.info(arg2)
    dob.send_keys(arg3) # MM/DD/YYYY or DD.MM.YYYY
    logging.info(arg3)
    email.send_keys(arg4)
    logging.info(arg4)
    if arg6 == 'Apply for a residence title': 
        element_dropdown.select_by_visible_text(arg7)
        if arg7 == 'yes':
            visa_numberr.send_keys(arg5)
            logging.info(arg5)
        logging.info(arg7)
    elif arg6 == 'Extend a residence title':
        ausweisnummer.send_keys(arg5)
        logging.info(arg5)
    time.sleep(1)
    browser.implicitly_wait(3)
    next_button = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
    next_button.click()

    WebDriverWait(browser, 120).until(EC.text_to_be_present_in_element((By.XPATH,
                                                                       '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[2]/div[2]/div[1]/div[2]/div[1]/div[1]/fieldset[1]/legend[1]'),
                                                                      'Appointment booking - Please check your data'))
    browser.implicitly_wait(1)
    is_check_data_page = browser.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[2]/div[2]/div[1]/div[2]/div[1]/div[1]/fieldset[1]/legend[1]')
    logging.info(is_check_data_page.text)

    browser.implicitly_wait(50)
    submit_button = browser.find_element(By.ID, 'summaryForm:proceed')
    submit_button.click()
    logging.info('FINAL SUBMIT | clicked')
    final_status = True

    time.sleep(5)


    # Find the element by its class
    pdf_link = browser.find_element(By.CLASS_NAME, 'btnApplicationPdf').get_attribute('href')
    logging.info('PDF LINK ' + pdf_link)

    user_data = (
    f'''
Firstname: ```{arg1}``` 

Lastname: ```{arg2}```'''
    )
    

    url = f'[ PDF | Click to Download]({pdf_link})'
    send_message_to_telegram(group_chat_id, url)
    send_message_to_telegram(group_chat_id, user_data)
    logging.info('PDF link has been sent to Telegram group')

    if find_day == '1':
        suffix = 'st'
    elif find_day == '2':
        suffix = 'nd'
    elif find_day == '3':
        suffix = 'rd'
    else:
        suffix = 'th'

    inform_user_message = (f''' Dear {arg1} {arg2}, 
Your appointment has been booked on ({find_month} {find_day}{suffix}) successfully, and the details of that have been sent to you via the official email of the Berlin Immigration Office. Please arrange the /payment of the 30 Euros fee within 24 hours otherwise your booking will be automatically canceled. 
If you have any concerns, leave us a message by touching the /contact_us .
Also you can download your appointment booking PDF from below link: 

{pdf_link}''')

    logging.info(inform_user_message)

    send_message_to_user(USER_CHAT_ID, inform_user_message, bot_token_getmytermin)
    send_message_to_user(ADMIN_USER_ID, inform_user_message, bot_token_getmytermin)

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
        date_time_selection(booking_time_offer_1, booking_time_offer_2, booking_month_1st, booking_month_2nd, booking_month_3rd, prefered_start_day, prefered_end_day, prefered_day)
        is_loop = 'false'
        import_personal_data(firstname, lastname, dob, email, id_card_number, residence_title, currently_have_a_residence)
        is_loop = 'false'
    except Exception as e:
        # The error handler function will be automatically called here
        i += 1

        if is_solvedCaptcha:
            user_data_2 = (
    f'''
Faild attempt
Firstname: ```{firstname}```
Lastname: ```{lastname}```'''
    )
            logging.info(send_screenshot_to_telegram_channel(group_chat_id, 'main', user_data_2))
            is_solvedCaptchaError = False

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
You can transfer 50 euros through the following account information and also send the related screenshot to the @GetMyTermin_Admin Telegram ID to confirm your payment.
{point_down}{point_down}{point_down}
IBAN : BE16967465727274
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
