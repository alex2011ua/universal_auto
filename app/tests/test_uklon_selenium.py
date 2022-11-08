from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import pendulum
import time


headless = True

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
if headless:
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--no-sandbox")
    options.add_argument("--screen-size=1920,1080")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")
    options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options, port=9514)
week_number=None
sleep=1
headless=False
base_url="https://fleets.uklon.com.ua"

# login
driver.get(base_url + '/auth/login')
if sleep:
    time.sleep(sleep)

element = driver.find_element(By.ID,'login')
for c in os.environ["UKLON_NAME"]:
    element.send_keys(c)
    time.sleep(0.1)

element = driver.find_element(By.ID, "password")
element.send_keys('')
element.send_keys(os.environ["UKLON_PASSWORD"])


driver.find_element(By.XPATH, '//button[@data-cy="login-btn"]').click()

if sleep:
    time.sleep(sleep)

# end login
# download payments_order
actions = ActionChains(driver)
actions.move_by_offset(500, 500).perform()
url = f'{base_url}/workspace/orders'
driver.get(url)
if sleep:
   time.sleep(sleep)
driver.find_element(By.XPATH, '//upf-order-report-list-filters/form/mat-form-field[1]').click()
driver.find_element(By.XPATH, '//mat-option/span/div[text()=" Вибрати період "]').click()
e = driver.find_element(By.XPATH, '//input')
day = pendulum.now().start_of('day')  # yesterday
e.send_keys(day.format("YYYY.MM.DD") + Keys.TAB + day.format("YYYY.MM.DD"))
driver.find_element(By.XPATH, '//span[text()= " Застосувати "]').click()
time.sleep(sleep)
actions.click().perform()
driver.find_element(By.XPATH, '//span[text()="Експорт CSV"]').click()