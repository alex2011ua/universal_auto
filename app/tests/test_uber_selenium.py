from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import os
import pendulum
import time


headless = False

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


def login_form( id, button, selector):
    element = driver.find_element(By.ID, id)
    element.send_keys(os.environ["UBER_NAME"])
    driver.find_element(selector, button).click()
    driver.get_screenshot_as_file('UBER_NAME.png')
    
def force_opt_form():
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'alt-PHONE-OTP')))
        el = driver.find_element(By.ID, 'alt-PHONE-OTP').click()
    except Exception as e:
        print(str(e))
        pass

def password_form( id, button, selector):
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, id)))
        el = driver.find_element(By.ID, id).send_keys(os.environ["UBER_PASSWORD"])
        driver.find_element(selector, button).click()
        driver.get_screenshot_as_file('UBER_PASSWORD.png')
    except Exception as e:
        print(str(e))

current_date = pendulum.now()
def start_of_week():
    return current_date.start_of('week')

def end_of_week():
        return current_date.end_of('week')

def payments_order_file_name():
    start = start_of_week()
    end = end_of_week()
    sd, sy, sm = start.strftime("%d"), start.strftime("%Y"), start.strftime("%m")
    ed, ey, em = end.strftime("%d"), end.strftime("%Y"), end.strftime("%m")
    return f'{sy}{sm}{sd}-{ey}{em}{ed}-payments_driver-___.csv'

def generate_payments_order():
    driver.get(f"{base_url}/orgs/49dffc54-e8d9-47bd-a1e5-52ce16241cb6/reports")
    if sleep:
        time.sleep(sleep)
    driver.get_screenshot_as_file('generate_payments_order.png')
    menu = '//div[@data-testid="report-type-dropdown"]/div/div'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, menu)))
    driver.find_element(By.XPATH, menu).click()   
    try:
        xpath = '//ul/li/div[text()[contains(.,"Payments Driver")]]'
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
        driver.find_element(By.XPATH, xpath).click()
    except Exception:
        xpath = '//ul/li/div[text()[contains(.,"Payments driver")]]'
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
        driver.find_element(By.XPATH, xpath).click()
    start = driver.find_element(By.XPATH, '(//input[@aria-describedby="datepicker--screenreader--message--input"])[1]')
    start.send_keys(Keys.NULL)
    driver.find_element(By.XPATH, f'//div[@aria-roledescription="button"]/div[text()={start_of_week().strftime("%-d")}]').click()
    end = driver.find_element(By.XPATH, '(//input[@aria-describedby="datepicker--screenreader--message--input"])[2]')
    end.send_keys(Keys.NULL)
    driver.find_element(By.XPATH, f'//div[@aria-roledescription="button"]/div[text()="{end_of_week().strftime("%-d")}"]').click()
    driver.find_element(By.XPATH, '//button[@data-testid="generate-report-button"]').click()

    return f'{payments_order_file_name()}'

def download_payments_order():
    if os.path.exists(f'{payments_order_file_name()}'):
        print('Report already downloaded')
        return 
    generate_payments_order()
    download_button = '(//div[@data-testid="payment-reporting-table-row"]/div/div/div/div/button)[1]'
    try:
        in_progress_text = '//div[1][@data-testid="payment-reporting-table-row"]/div/div/div/div[text()[contains(.,"In progress")]]'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, in_progress_text)))
        WebDriverWait(driver, 300).until_not(EC.presence_of_element_located((By.XPATH, in_progress_text)))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, download_button)))
    except Exception as e:
        print(str(e))
        pass 
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, download_button))
# login
link = "https://auth.uber.com/login/"
driver.get(link)
login_form('PHONE_NUMBER_or_EMAIL_ADDRESS', 'forward-button', By.ID)  
force_opt_form()
time.sleep(20)
password_form('PASSWORD', 'forward-button', By.ID)
if sleep:
    time.sleep(sleep)



driver.get(f"{base_url}/orgs/49dffc54-e8d9-47bd-a1e5-52ce16241cb6/reports")
if sleep:
    time.sleep(sleep)
driver.get_screenshot_as_file('generate_payments_order.png')
menu = '//div[@data-testid="report-type-dropdown"]/div/div'
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, menu)))
driver.find_element(By.XPATH, menu).click()
try:
    xpath = '//ul/li/div[text()[contains(.,"Payments Driver")]]'
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
    driver.find_element(By.XPATH, xpath).click()
except Exception:
    xpath = '//ul/li/div[text()[contains(.,"Payments driver")]]'
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
    driver.find_element(By.XPATH, xpath).click()
driver.find_element(By.XPATH, '(//input[@aria-describedby="datepicker--screenreader--message--input"])[1]')

driver.find_element(By.XPATH, f'//div[@aria-roledescription="button"]/div[text()={start_of_week().strftime("%-d")}]').click()
current_date = pendulum.now().start_of('week').subtract(days=3)
end = driver.find_element(By.XPATH, '(//input[@aria-describedby="datepicker--screenreader--message--input"])[2]')
end.send_keys(Keys.NULL)
driver.find_element(By.XPATH, f'//div[@aria-roledescription="button"]/div[text()="{end_of_week().strftime("%-d")}"]').click()
driver.find_element(By.XPATH, '//button[@data-testid="generate-report-button"]').click()


download_button = '(//div[@data-testid="payment-reporting-table-row"]/div/div/div/div/button)[1]'
try:
    in_progress_text = '//div[1][@data-testid="payment-reporting-table-row"]/div/div/div/div[text()[contains(.,"In progress")]]'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, in_progress_text)))
    WebDriverWait(driver, 300).until_not(EC.presence_of_element_located((By.XPATH, in_progress_text)))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, download_button)))
except Exception as e:
    logger.error(str(e))
    pass
driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, download_button))


day = pendulum.now().subtract(days=1)


driver.find_element(By.XPATH,'(//input[@aria-describedby="datepicker--screenreader--message--input"])[1]').click()

date_by_def = pendulum.now().start_of('week').subtract(days=7)
if date_by_def.month - day.month == -1:  # if month of day is different from month of last week Monday
    driver.find_element(By.XPATH, f'//button[@aria-label="Next month."]').click()
elif date_by_def.month - day.month > 0:
    for _ in range(date_by_def.month - day.month):
        driver.find_element(By.XPATH, f'//button[@aria-label="Previous month."]').click()
        time.sleep(1)
driver.find_element(By.XPATH, f'//div[@aria-roledescription="button"]/div[text()={day.strftime("%-d")}]').click()
driver.find_element(By.XPATH,'(//input[@aria-describedby="datepicker--screenreader--message--input"])[2]').click()
end.send_keys(Keys.NULL)
driver.find_element(By.XPATH,f'//div[@aria-roledescription="button"]/div[text()="{day.strftime("%-d")}"]').click()


    
