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

chrome_driver_path = "C:/SeleniumDrivers/chromedriver.exe"

# option = webdriver.ChromeOptions()
option = Options()
option.page_load_strategy = 'normal'
option.add_argument("--start-maximized")
option.add_argument("--remote-debugging-port=9222")  # Use an arbitrary port number
option.add_experimental_option("detach", True)  # Keep the browser window open after exiting the script
option.add_argument(
    '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 '
    'Safari/537.36"')

# Removes navigator.webdriver flag

# For older ChromeDriver under version 113.0.3945.16
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)

# For ChromeDriver version 79.0.3945.16 or over
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("--disable-notifications")
option.add_argument("--disable-popup-blocking")

global browser
global service_path

booking_time_offer_1 = '10:00'
booking_time_offer_2 = '10:30'


# Open Browser
def open_browser():
    global browser
    global service_path
    service_path = Service(executable_path=chrome_driver_path)
    browser = webdriver.Chrome(service=service_path, options=option)
    browser.get("https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en")


def main_process():
    loop_condition = 'true'
    while loop_condition == 'true':
        try:
            browser.implicitly_wait(20)
            book_appointment_btn = browser.find_element(By.CSS_SELECTOR,
                                                        'a[href="/ams/TerminBuchen/wizardng?sprachauswahl=en"]')
            book_appointment_btn.click()
            loop_condition = 'false'  # Exit the while Loop
        except NoSuchElementException or TimeoutException or ElementNotInteractableException:
            print('We have some error on First page and will be retry again!')
            browser.quit()
            open_browser()
            main_process()
            pass

    loop_condition = 'true'  # Reset Loop Condition

    try:
        browser.implicitly_wait(60)
        checkbox_mark = browser.find_element(By.ID, 'xi-cb-1')
        checkbox_mark.click()
        browser.implicitly_wait(10)
        next_btn = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
        next_btn.click()
    except NoSuchElementException:
        print('We have some error on Second page and will be retry again!')
        browser.quit()
        open_browser()
        main_process()
        pass

    try:
        browser.implicitly_wait(60)
        element_dropdown1 = browser.find_element(By.ID, 'xi-sel-400')
        time.sleep(0.5)
        element_dropdown1.click()
        time.sleep(0.5)
        select1 = Select(element_dropdown1)
        select1.select_by_visible_text('Iran, Islamic Republic')
        print('part-1-point-1')

        time.sleep(0.5)

        element_dropdown2 = browser.find_element(By.ID, 'xi-sel-422')
        time.sleep(0.5)
        element_dropdown2.click()
        time.sleep(0.5)
        select2 = Select(element_dropdown2)
        select2.select_by_visible_text('one person')

        time.sleep(0.5)

        element_dropdown3 = browser.find_element(By.ID, 'xi-sel-427')
        time.sleep(0.5)
        element_dropdown3.click()
        time.sleep(0.5)
        select3 = Select(element_dropdown3)
        select3.select_by_visible_text('yes')

        time.sleep(0.5)

        element_dropdown4 = browser.find_element(By.ID, 'xi-sel-428')
        time.sleep(0.5)
        element_dropdown4.click()
        time.sleep(0.5)
        select4 = Select(element_dropdown4)
        select4.select_by_visible_text('Iran, Islamic Republic')

        time.sleep(1)

        apply_residence = browser.find_element(By.CLASS_NAME, 'kachel-439-0-1')
        browser.implicitly_wait(3)
        apply_residence.click()
        browser.implicitly_wait(3)
        family_reasons = browser.find_element(By.CLASS_NAME, 'accordion-439-0-1-4')
        browser.implicitly_wait(3)
        family_reasons.click()

        time.sleep(1)
        # SERVICEWAHL_EN439-0-1-4-327471
        # SERVICEWAHL_EN439-0-1-4-305289
        student = browser.find_element(By.ID, 'SERVICEWAHL_EN439-0-1-4-327471')
        browser.implicitly_wait(3)
        student.click()
        # browser.implicitly_wait(30)

        time.sleep(20)

        browser.implicitly_wait(20)
        next_btn = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
        browser.implicitly_wait(3)
        next_btn.click()


    except NoSuchElementException:
        print('We have some error on Service selection page (PART-1) and will be retry again!')
        browser.quit()
        open_browser()
        main_process()
        pass


def service_selection():
    for i in range(100):
        time.sleep(25)
        try:
            WebDriverWait(browser, 3).until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, "fieldset[id='xi-fs-2'] legend"), 'Appointment selection')
            )
            print("Service selection page is available")
            
        except TimeoutException:
            # try: #First we check if we entered the official error page
            #     WebDriverWait(browser, 32).until(EC.text_to_be_present_in_element((By.ID, 'mainForm'), 'Error '))
            #     print('A general error occurred on the site.\nBack to landing page and start again.')
            #     browser.quit()
            #     open_browser() 
            #     main_process()
            #     pass
            # except TimeoutException:
            print(f"Unfortunately the Date is unavailable\nRepeated", {i + 1}, "times")
            # browser.implicitly_wait(10)
            # next_button = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
            # next_button.click()
            time.sleep(1)
            browser.quit()
            time.sleep(1)
            open_browser()
            time.sleep(1)
            main_process()
            pass
        # time.sleep(30)
        # browser.implicitly_wait(3)
        # is_next_page = browser.find_element(By.CSS_SELECTOR, "fieldset[id='xi-fs-2'] legend")
        # print({is_next_page.text})
        # if (is_next_page.text == 'Appointment selection'):
        #     print("Service selection page is available")
        # else:
        #     print(f"Unfortunately the Date is unavailable\nRepeated", {i + 1}, "times")
        #     browser.quit()
        #     open_browser()
        #     main_process()

def date_time_selection():
    # time.sleep(2)
    global option
    try:
        browser.implicitly_wait(3)
        select_date = browser.find_element(By.XPATH, '//td[@data-handler="selectDay"]')
        browser.implicitly_wait(3)
        print(f'The selected date is {select_date.text} day of the month')
        select_date.click()
    except NoSuchElementException:
        print('We got to the date selection page, but unfortunately there are no dates to choose from.')
        browser.quit()
        open_browser()
        main_process()

    dropdown_menu_is_open = browser.find_element(By.XPATH,
                                               '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/fieldset[1]/div[1]/select[1]')

    # try:
    for i in range(600):  # Create Time Delay for open the page complete
        if not (dropdown_menu_is_open.text == 'Please select'):
            print("The (Time selection) part is loaded completely now.", " ", "After", {(i+1) * 0.1}, "Second")
            break
        else:
            print(i)
    time.sleep(0.1)

    dropdown_menu = Select(browser.find_element(By.ID, 'xi-sel-3'))
    for option in dropdown_menu.options:
        print(option.text, option.get_attribute('value'))
        if option.text == booking_time_offer_1 or booking_time_offer_2:
            break

    print('Booking time has been selected and everything is ok\nGo a head')
    dropdown_menu.select_by_visible_text(option.text)
    browser.implicitly_wait(3)
    next_button = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
    next_button.click()


def import_personal_data():
    try:
        WebDriverWait(browser, 60).until(EC.text_to_be_present_in_element((By.XPATH,
                                                                           '/html[1]/body[1]/div[2]/div[2]/div[4]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/fieldset[1]/div[1]/div[1]/label[1]/p[1]'),
                                                                          'First name*'))
    except TimeoutException:
        browser.quit()
        open_browser()
        main_process()

    browser.implicitly_wait(10)
    firstname = browser.find_element(By.ID, 'xi-tf-3')
    lastname = browser.find_element(By.ID, 'xi-tf-4')
    dob = browser.find_element(By.ID, 'xi-tf-5')
    email = browser.find_element(By.ID, 'xi-tf-6')
    question_field_1 = browser.find_element(By.ID, 'xi-sel-2')

    firstname.send_keys('Milad')
    lastname.send_keys('Shahabifard')
    dob.send_keys('11.04.1989')
    email.send_keys('milad.shahabifard.20@gmail.com')
    element_dropdown = Select(browser.find_element(By.ID, 'xi-sel-2'))
    element_dropdown.select_by_visible_text('no')
    browser.implicitly_wait(3)
    next_button = browser.find_element(By.ID, 'applicationForm:managedForm:proceed')
    next_button.click()

    browser.implicitly_wait(50)
    submit_button = browser.find_element(By.ID, 'summaryForm:proceed')
    submit_button.click()


open_browser()
main_process()
service_selection()
date_time_selection()
import_personal_data()

print('--Congratulations! your booking has been done successfully--')
