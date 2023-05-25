from Screenshot import Screenshot
from Screenshot import Screenshot_Clipping
from selenium import webdriver

screenshot = Screenshot_Clipping.Screenshot()
screenshot.full_Screenshot(driver, save_path=r'.', image_name='python.png')


ob = Screenshot.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3/Selenium_Screenshot/tree/master/test"
driver.get(url)
img_url = ob.full_screenshot(driver, save_path=r'.', image_name='myimage.png', is_load_at_runtime=True,
                                          load_wait_time=3)
print(img_url)
driver.close()

driver.quit()