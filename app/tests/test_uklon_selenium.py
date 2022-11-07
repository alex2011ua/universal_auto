from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pendulum
import time
options = Options()
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": os.getcwd(),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing_for_trusted_sources_enabled": False,
    "safebrowsing.enabled": False
})
options.add_argument("--disable-infobars")
options.add_argument("--enable-file-cookies")
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options, port=9514)
week_number=None
sleep=3
headless=False
base_url="https://fleets.uklon.com.ua"
day = pendulum.now().start_of('day').subtract(days=1)  # yesterday
# login
driver.get(base_url + '/auth/login')
if sleep:
    time.sleep(sleep)
driver.get_screenshot_as_file(f'new_uklon1.png')
element = driver.find_element(By.ID,'login')
element.send_keys('5')
for c in os.environ["UKLON_NAME"]:
    element.send_keys(c)
    time.sleep(0.1)

driver.get_screenshot_as_file(f'new_uklon2.png')

element = driver.find_element(By.ID, "password")
element.send_keys('')
element.send_keys(os.environ["UKLON_PASSWORD"])
driver.get_screenshot_as_file(f'new_uklon3.png')

driver.find_element(By.XPATH, '//button[@data-cy="login-btn"]').click()
driver.get_screenshot_as_file(f'new_uklon4.png')
if sleep:
    time.sleep(sleep)
driver.get_screenshot_as_file(f'new_uklon5.png')
# end login
# download payments_order

url = f'{base_url}/workspace/orders'
driver.get(url)
if sleep:
    time.sleep(sleep)

driver.find_element(By.XPATH, '//upf-order-report-list-filters/form/mat-form-field[1]').click()
driver.get_screenshot_as_file(f'new_uklon6.png')
driver.find_element(By.XPATH, '//mat-option/span/div[text()=" Вибрати період "]').click()
driver.get_screenshot_as_file(f'new_uklon7.png')
e = driver.find_element(By.XPATH, '//input')
e.send_keys(day.format("DD.MM.YYYY") + Keys.TAB + day.format("DD.MM.YYYY"))
driver.find_element(By.XPATH, '//span[text()= " Застосувати "]').click()



driver.find_element(By.XPATH, '//span[text()="Експорт CSV"]').click()
driver.get_screenshot_as_file(f'new_uklon8.png')