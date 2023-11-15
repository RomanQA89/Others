from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

service = ChromeService(executable_path=r'C:\Chrome-selenium\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://opensource-demo.orangehrmlive.com/')

WDW(driver, 5).until(EC.presence_of_element_located((By.NAME, 'username')))

driver.find_element(By.NAME, 'username').send_keys('Admin')
driver.find_element(By.NAME, 'password').send_keys('admin123')
driver.find_element(By.TAG_NAME, 'button').click()
try:
    WDW(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'oxd-userdropdown-name')))
    print('Логин удался')
except:
    print('Логин не удался')

driver.find_element(By.XPATH, '//a[@href="/web/index.php/pim/viewMyDetails"]').click()

WDW(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="yyyy-mm-dd"]')))

date = driver.find_elements(By.XPATH, '//input[@placeholder="yyyy-mm-dd"]')
sleep(1)
date[0].click()
for _ in range(10):
    date[0].send_keys(Keys.BACKSPACE)
date[0].send_keys('20-20-9999')

buttons = driver.find_elements(By.XPATH, '//button[@type="submit"]')
buttons[0].click()

err_msg = driver.find_element(By.XPATH, '//span[contains(@class, "oxd-input-field-error-message")]')
if err_msg.text == 'Should be a valid date in yyyy-mm-dd format':
    print('Валидация пройдена')

sleep(5)

driver.quit()
