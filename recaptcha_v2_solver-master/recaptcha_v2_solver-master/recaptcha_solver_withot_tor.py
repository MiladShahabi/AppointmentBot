# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 10:01:10 2020

@author: OHyic
"""

# system libraries
import os
import sys
import urllib
import pydub
import speech_recognition as sr
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
from datetime import datetime
import requests
import json
import stem.process
from stem import Signal
from stem.control import Controller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# custom patch libraries
from patch import download_latest_chromedriver, webdriver_folder_name


chrome_driver_path = "C:/SeleniumDrivers/chromedriver.exe" # windows



def delay(waiting_time=5):
    driver.implicitly_wait(waiting_time)

# def create_tor_proxy(socks_port,control_port):
#     TOR_PATH = os.path.normpath(os.getcwd()+"\\tor\\tor.exe")
#     try:
#         tor_process = stem.process.launch_tor_with_config(
#           config = {
#             'SocksPort': str(socks_port),
#             'ControlPort' : str(control_port),
#             'MaxCircuitDirtiness' : '300',
#           },
#           init_msg_handler = lambda line: print(line) if re.search('Bootstrapped', line) else False,
#           tor_cmd = TOR_PATH
#         )
#         print("[INFO] Tor connection created.")
#     except:
#         tor_process = None
#         print("[INFO] Using existing tor connection.")
    
#     return tor_process

# def renew_ip(control_port):
#     print("[INFO] Renewing TOR ip address.")
#     with Controller.from_port(port=control_port) as controller:
#         controller.authenticate()
#         controller.signal(Signal.NEWNYM)
#         controller.close()
#     print("[INFO] IP address has been renewed! Better luck next try~")  
    
if __name__ == "__main__":
    # SOCKS_PORT = 41293
    # CONTROL_PORT = 41294

    USER_AGENT_LIST = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.1',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/116.0',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.3',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
                    ]
    # activate_tor = False
    tor_process = None
    user_agent = random.choice(USER_AGENT_LIST)
    # if activate_tor:
    #     print('[INFO] TOR has been activated. Using this option will change your IP address every 60 secs.')
    #     print('[INFO] Depending on your luck you might still see: Your Computer or Network May Be Sending Automated Queries.')
    #     tor_process = create_tor_proxy(SOCKS_PORT,CONTROL_PORT)
    #     PROXIES = {
    #         "http": f"socks5://127.0.0.1:{SOCKS_PORT}",
    #         "https": f"socks5://127.0.0.1:{SOCKS_PORT}"
    #     }
    #     response = requests.get("http://ip-api.com/json/", proxies=PROXIES)
    # else:
    #     response = requests.get("http://ip-api.com/json/")
    # result = json.loads(response.content)
    # print('[INFO] IP Address [%s]: %s %s'%(datetime.now().strftime("%d-%m-%Y %H:%M:%S"), result["query"], result["country"]))
    
    # download latest chromedriver, please ensure that your chrome is up to date
    while True:
        try:
            # create chrome driver
            chrome_options = webdriver.ChromeOptions()
            path_to_chromedriver = os.path.normpath(
                os.path.join(os.getcwd(), webdriver_folder_name, "chromedriver.exe")
            )
            # if activate_tor:
            #     chrome_options.add_argument(f"--proxy-server=socks5://127.0.0.1:{SOCKS_PORT}")
            chrome_options.add_argument('--headless') # VPS Mode
            chrome_options.add_argument('--disable-gpu')  # Last I checked this was necessary. # VPS Mode
            chrome_options.add_argument('--no-sandbox') # VPS Mode
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False) 

            chrome_options.add_argument(f"user-agent={user_agent}")
            service_path = Service(executable_path=path_to_chromedriver)
            driver = webdriver.Chrome(service=service_path, options=chrome_options)
            # chrome_driver_path
            # path_to_chromedriver

            delay()
            # go to website
            driver.get("https://www.google.com/recaptcha/api2/demo")

            break
        except Exception:
            # patch chromedriver if not available or outdated
            try:
                driver
            except NameError:
                is_patched = download_latest_chromedriver()
            else:
                is_patched = download_latest_chromedriver(
                    driver.capabilities["version"]
                )
            if not is_patched:
                sys.exit(
                    "[ERR] Please update the chromedriver.exe in the webdriver folder according to your chrome version:"
                    "https://chromedriver.chromium.org/downloads"
                )
    
    # main program
    # auto locate recaptcha frames
    try:
        delay()

        WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='reCAPTCHA']")))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
        # switch to recaptcha audio challenge frame
        driver.switch_to.default_content()
        # click on audio challenge
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='recaptcha challenge expires in two minutes']")))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))).click()

        # get the mp3 audio file
        delay()
        src = driver.find_element(By.ID, "audio-source").get_attribute("src")
        print(f"[INFO] Audio src: {src}")
    
        path_to_mp3 = os.path.normpath(os.path.join(os.getcwd(), "sample.mp3"))
        path_to_wav = os.path.normpath(os.path.join(os.getcwd(), "sample.wav"))
    
        # download the mp3 audio file from the source
        urllib.request.urlretrieve(src, path_to_mp3)
    except:
        # if ip is blocked.. renew tor ip
        print("[INFO] IP address has been blocked for recaptcha.")
        # if activate_tor:
        #     renew_ip(CONTROL_PORT)
        # sys.exit()    

    # load downloaded mp3 audio file as .wav
    try:
        sound = pydub.AudioSegment.from_mp3(path_to_mp3)
        sound.export(path_to_wav, format="wav")
        sample_audio = sr.AudioFile(path_to_wav)
    except Exception:
        sys.exit(
            "[ERR] Please run program as administrator or download ffmpeg manually, "
            "https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/"
        )

    # translate audio to text with google voice recognition
    delay()
    r = sr.Recognizer()
    with sample_audio as source:
        audio = r.record(source)
    key = r.recognize_google(audio)
    print(f"[INFO] Recaptcha Passcode: {key}")

    # key in results and submit
    delay()
    driver.find_element(By.ID, "audio-response").send_keys(key.lower())
    driver.find_element(By.ID, "audio-response").send_keys(Keys.ENTER)
    time.sleep(5)
    driver.switch_to.default_content()
    time.sleep(5)
    driver.find_element(By.ID, "recaptcha-demo-submit").click()
    if (tor_process):
        tor_process.kill()
    