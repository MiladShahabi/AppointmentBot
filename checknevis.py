# from selenium import webdriver
# from PIL import Image
# from telegram import Bot
# import io
# from typing import Final


# TELEGRAM_BOT_TOKEN : Final =''
# TELEGRAM_CHAT_ID : Final = ''

# # left = 
# # top =
# # right =
# # bottom =



# # Create a new instance of the Firefox driver
# driver = webdriver.Firefox()

# # Go to the webpage that you want to access
# driver.get("https://www.example.com")

# # Capture the screenshot
# driver.save_screenshot("screenshot.png")

# # Open the screenshot & crop
# img = Image.open("screenshot.png")
# cropped_img = img.crop((left, top, right, bottom))  # Replace with your own coordinates
# cropped_img.save("screenshot_cropped.png")

# # Telegram bot
# bot = Bot(token=TELEGRAM_BOT_TOKEN)  # Replace with your Telegram bot token

# # Send cropped screenshot
# with open('screenshot_cropped.png', 'rb') as photo:
#     bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=photo)  # Replace with the target chat ID

# # Close the browser window
# driver.quit()


# import time
# avrage = 0

# for i in range (10):
#     avrage += 1
#     print(avrage)
#     time.sleep(1)


# pdf_link = 'ams/fghh'
# newlink = 'https://otv.verwalt-berlin.de/' + pdf_link
# print(newlink)


# June = 'June'
# July = 'July '
# August = 'August'

# month = July 

# if not month == 'June':
#     if not month == 'July':
#         if not month == 'August':
#             print(month)
#             # raise



# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()
          
# firstname= 'ali'
# id_card = 'ggg'
# group_chat_id = '123456'

# def send_screenshot_to_telegram_channel(arg1, arg2, arg3):
#     print(arg1 , arg2, arg3)
#     return 22



# print(send_screenshot_to_telegram_channel(group_chat_id, 'xi-div-1', f'Status of auto reCaptcha solver {firstname}'))

# import sys
# import time
# import telebot
# from typing import Final

# # Initialize the bot with your bot token
# bot_token_status_gmt_bot: Final = "5889078485:AAEe7G8zffK0ZVVBt0gQBcmi_yWm_zjZ7Yg"
# bot_token_getmytermin: Final = "6114910026:AAGGPogroG1BvkHA3LOTab_0EzBqqi3JQYM"
# BOT_USERNAME: Final = '@Status_GMT_Bot'
# bot = telebot.TeleBot(bot_token_status_gmt_bot)

# ADMIN_USER_ID: Final = 5355774833  # Admin's user ID
# group_chat_id: Final = -1001636295549
# channel_chat_id: Final = -1001826497482
# USER_CHAT_ID: Final = 5686464021  # User's Chat ID



# def send_message_to_telegram(admin_chat_id, message):
#     # replace 'ADMIN_CHAT_ID' with the chat id of the admin
#     bot.send_message(admin_chat_id, message, parse_mode='Markdown')

# def send_message_to_user(user_chat_id_1, temp_message, bot_token):
#     bot = telebot.TeleBot(bot_token)
#     bot.send_message(user_chat_id_1, temp_message, parse_mode='None')    




# # {(i + 1) * 0.1}
# firstname = 'ali'
# lastname = 'babaei'

# find_month = ''
# find_day = ''

# def func2():
#     global find_month
#     global find_day

#     find_month = 'Agust'
#     find_day = '7'





# def func3(arg1, arg2):
        
#     global find_month
#     global find_day

#     if find_day == '1':
#         suffix = 'st'
#     elif find_day == '2':
#         suffix = 'nd'
#     elif find_day == '3':
#         suffix = 'rd'
#     else:
#         suffix = 'th'

#     pdf_link = 'https://otv.verwalt-berlin.de/ams/TerminBuchen/download/antrag/11c42235-d483-47fe-9984-656f17c02aaa'

#     inform_user_message = (f''' Dear {arg1} {arg2}, 
# Your appointment has been booked on ({find_month} {find_day}{suffix}) successfully, and the details of that have been sent to you via the official email of the Berlin Immigration Office. Please arrange the /payment of the 30 Euros fee within 24 hours otherwise your booking will be automatically canceled. 
# If you have any concerns, leave us a message by touching the /contact_us .
# Also you can still download your appointment booking PDF from below link: 

# {pdf_link}''')
    
    

#     message = 'test'
#     print(inform_user_message)


#     send_message_to_user(USER_CHAT_ID, inform_user_message, bot_token_getmytermin)
#     # send_message_to_user(ADMIN_USER_ID, inform_user_message, bot_token_getmytermin)



# time.sleep(3)
# func2()
# func3(firstname, lastname)







# prefered_start_day = 8
# prefered_end_day = 27

# date = '29'

# if not prefered_end_day >= int(date) >= prefered_start_day:
#     print(date)
# else:
#     print('date not find')






# import time
#     # pip install undetected-chromedriver 
# import undetected_chromedriver.v2 as uc 
 
# # Initializing driver 
# driver = uc.Chrome() 
 
# # Try accessing a website with antibot service 
# driver.get("https://nowsecure.nl")


# time.sleep(100)









# import undetected_chromedriver as uc

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time


# chrome_driver_path = "C:/SeleniumDrivers/chromedriver.exe" # windows


# # Replace this with the path to your html file
# FULL_PATH_TO_HTML_FILE = "C:/Users/Milad Shahabi/Desktop/AppointmentBot/url_page.html" # 'file:///Users/simplepineapple/html/url_page.html'

# def visit_website(browser):
#     browser.get(FULL_PATH_TO_HTML_FILE)
#     time.sleep(3)

#     links = browser.find_element(By.XPATH, "//a[@href]")
#     links.click()
#     time.sleep(10)

#     # Switch webdriver focus to new tab so that we can extract html
#     tab_names = browser.window_handles
#     if len(tab_names) > 1:
#         browser.switch_to.window(tab_names[1])

#     time.sleep(1)
#     html = browser.page_source
#     print(html)
#     print()
#     print()

#     if 'Charts' in html:
#         print('Success')
#     else:
#         print('Fail')

#     time.sleep(10)


# options = webdriver.ChromeOptions()







# # If options.headless = True, the website will not load
# # options.add_argument('--headless')
# options.add_argument("--window-size=1920,1080")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"')

# service_path = Service(executable_path=chrome_driver_path)
# browser = webdriver.Chrome(service=service_path, options=options)

# browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
#     "source": '''
#     Object.defineProperty(navigator, 'webdriver', {
#         get: () => undefined
#     });
#     Object.defineProperty(navigator, 'plugins', {
#             get: function() { return {"0":{"0":{}},"1":{"0":{}},"2":{"0":{},"1":{}}}; }
#     });
#     Object.defineProperty(navigator, 'languages', {
#         get: () => ["en-US", "en"]
#     });
#     Object.defineProperty(navigator, 'mimeTypes', {
#         get: function() { return {"0":{},"1":{},"2":{},"3":{}}; }
#     });

#     window.screenY=23;
#     window.screenTop=23;
#     window.outerWidth=1337;
#     window.outerHeight=825;
#     window.chrome =
#     {
#       app: {
#         isInstalled: false,
#       },
#       webstore: {
#         onInstallStageChanged: {},
#         onDownloadProgress: {},
#       },
#       runtime: {
#         PlatformOs: {
#           MAC: 'mac',
#           WIN: 'win',
#           ANDROID: 'android',
#           CROS: 'cros',
#           LINUX: 'linux',
#           OPENBSD: 'openbsd',
#         },
#         PlatformArch: {
#           ARM: 'arm',
#           X86_32: 'x86-32',
#           X86_64: 'x86-64',
#         },
#         PlatformNaclArch: {
#           ARM: 'arm',
#           X86_32: 'x86-32',
#           X86_64: 'x86-64',
#         },
#         RequestUpdateCheckStatus: {
#           THROTTLED: 'throttled',
#           NO_UPDATE: 'no_update',
#           UPDATE_AVAILABLE: 'update_available',
#         },
#         OnInstalledReason: {
#           INSTALL: 'install',
#           UPDATE: 'update',
#           CHROME_UPDATE: 'chrome_update',
#           SHARED_MODULE_UPDATE: 'shared_module_update',
#         },
#         OnRestartRequiredReason: {
#           APP_UPDATE: 'app_update',
#           OS_UPDATE: 'os_update',
#           PERIODIC: 'periodic',
#         },
#       },
#     };
#     window.navigator.chrome =
#     {
#       app: {
#         isInstalled: false,
#       },
#       webstore: {
#         onInstallStageChanged: {},
#         onDownloadProgress: {},
#       },
#       runtime: {
#         PlatformOs: {
#           MAC: 'mac',
#           WIN: 'win',
#           ANDROID: 'android',
#           CROS: 'cros',
#           LINUX: 'linux',
#           OPENBSD: 'openbsd',
#         },
#         PlatformArch: {
#           ARM: 'arm',
#           X86_32: 'x86-32',
#           X86_64: 'x86-64',
#         },
#         PlatformNaclArch: {
#           ARM: 'arm',
#           X86_32: 'x86-32',
#           X86_64: 'x86-64',
#         },
#         RequestUpdateCheckStatus: {
#           THROTTLED: 'throttled',
#           NO_UPDATE: 'no_update',
#           UPDATE_AVAILABLE: 'update_available',
#         },
#         OnInstalledReason: {
#           INSTALL: 'install',
#           UPDATE: 'update',
#           CHROME_UPDATE: 'chrome_update',
#           SHARED_MODULE_UPDATE: 'shared_module_update',
#         },
#         OnRestartRequiredReason: {
#           APP_UPDATE: 'app_update',
#           OS_UPDATE: 'os_update',
#           PERIODIC: 'periodic',
#         },
#       },
#     };
#     ['height', 'width'].forEach(property => {
#         const imageDescriptor = Object.getOwnPropertyDescriptor(HTMLImageElement.prototype, property);

#         // redefine the property with a patched descriptor
#         Object.defineProperty(HTMLImageElement.prototype, property, {
#             ...imageDescriptor,
#             get: function() {
#                 // return an arbitrary non-zero dimension if the image failed to load
#             if (this.complete && this.naturalHeight == 0) {
#                 return 20;
#             }
#                 return imageDescriptor.get.apply(this);
#             },
#         });
#     });

#     const getParameter = WebGLRenderingContext.getParameter;
#     WebGLRenderingContext.prototype.getParameter = function(parameter) {
#         if (parameter === 37445) {
#             return 'Intel Open Source Technology Center';
#         }
#         if (parameter === 37446) {
#             return 'Mesa DRI Intel(R) Ivybridge Mobile ';
#         }

#         return getParameter(parameter);
#     };

#     const elementDescriptor = Object.getOwnPropertyDescriptor(HTMLElement.prototype, 'offsetHeight');

#     Object.defineProperty(HTMLDivElement.prototype, 'offsetHeight', {
#         ...elementDescriptor,
#         get: function() {
#             if (this.id === 'modernizr') {
#             return 1;
#             }
#             return elementDescriptor.get.apply(this);
#         },
#     });
#     '''
# })

# visit_website(browser)

# browser.quit()




# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium_stealth import stealth

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument("--headless")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)


# driver = webdriver.Chrome(options=options, executable_path=r"C:/SeleniumDrivers/chromedriver.exe")

# stealth(driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
# )

# driver.get("https://bot.sannysoft.com/")

# print(driver.find_element(By.XPATH, "/html/body").text)

# driver.close()


# import time
# import random

# firstname ='ali'
# i = 0
# while True:
#         time.sleep(0.5)

#         random.seed()
#         #print(int(random.random()*10)+1)
#         random_value = random.randrange(2, 6)
#         print(random_value)

#         i += 1
#         if i == 24:
#             i = 0
#             bot_status_msg = (f"I'm still running please stop me so you can have more resources for other bots!\n++Container NAME is: ({firstname})")
#             print(bot_status_msg)


# import undetected_chromedriver 
# import time

# try:
#     driver = undetected_chromedriver.Chrome()
#     driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
#     time.sleep(20)

# except Exception as ex:
#         print(ex)
# finally:
#     #   driver.close()
#     #   driver.quit()
#     i=0


i = 11
b = True

if i > 10 or b == False:
    print('Success')




