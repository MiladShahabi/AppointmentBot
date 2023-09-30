from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import telebot
import time



request_type = "Residence permit for spouses, parents and children of foreign citizens (sect. 29-34)"
emoji_check_mark = u'\U00002705'
emoji_thanks = u'\U0001F64F'
emoji_bot = u'\U0001F916'
at = u'\U00000040'

# Now send it to Telegram
TOKEN = '5796108934:AAFH4J0IFNo5eGSiiyhqsh7oB93UHaY3iUY'  # Replace with your Bot's token
CHANNEL_ID = '5355774833'  # Replace with your Channel ID or chat_id

bot = telebot.TeleBot(TOKEN)

def send_message_to_admin(admin_chat_id, message):
    # replace 'ADMIN_CHAT_ID' with the chat id of the admin
    bot.send_message(admin_chat_id, message)




# Create a new instance of the Chrome driver
option = Options()
option.page_load_strategy = 'normal'
option.add_argument("--start-maximized")
option.add_argument("--window-size=4320,7680")
option.add_argument('--headless') # VPS Mode
# option.add_argument('--disable-gpu')  # Last I checked this was necessary. # VPS Mode
# option.add_argument('--no-sandbox') # VPS Mode
option.add_argument('--disable-dev-shm-usage') # VPS Mode
#option.add_argument("--remote-debugging-port=9123")  # Use an arbitrary port number
option.add_experimental_option("detach", True)  # Keep the browser window open after exiting the script
option.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"')

# Removes navigator.webdriver flag

# For older ChromeDriver under version 113.0.3945.16
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)

# For ChromeDriver version 79.0.3945.16 or over
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("--disable-notifications")
option.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome(options=option, executable_path='C:/SeleniumDrivers/chromedriver.exe')  # Replace with the path to your chromedriver

# Go to the website
driver.get('https://otv.verwalt-berlin.de/ams/TerminBuchen')  # Replace with your website


time.sleep(5)
# Identify the element to screenshot by its ID (you can use XPATH, CSS selectors, etc.)
element = driver.find_element(By.ID, 'main')  # Replace 'element-id' with the id of your element
# Screenshot the element
element.screenshot('element.png')


driver.quit()


with open('element.png', 'rb') as photo:
    bot.send_photo(CHANNEL_ID, photo)


text = (f'''{emoji_check_mark} Appointment available
---------------------------------------------------------------
Title: {request_type}
---------------------------------------------------------------
{emoji_bot} If you have difficulty booking an appointment, our Telegram bot is always there to make it easy for you!

Telegram bot link :
@GetMyTermin_Bot
---------------------------------------------------------------
Thank you for following us.''')

send_message_to_admin(CHANNEL_ID, text)

print("Screenshot sent!")
