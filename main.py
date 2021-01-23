from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

facebook_id = ''
facebook_password = ''

chrome_drive_path = "G:\Some useful Sofwares\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.get("https://tinder.com")
time.sleep(5)
login_x_path = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button'
driver.find_element_by_xpath(login_x_path).click()
time.sleep(3)
try:
    driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
except NoSuchElementException:
    driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/button').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
time.sleep(2)
tinder_page = driver.window_handles[0]
fb_page_login = driver.window_handles[1]
driver.switch_to.window(fb_page_login)

driver.find_element_by_xpath('//*[@id="email"]').send_keys(facebook_id)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(facebook_password)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(Keys.ENTER)
try:
    driver.find_element_by_xpath('//*[@id="u_0_4"]/div[2]/div[1]/div[1]/button').click()
except NoSuchElementException:
    pass
driver.switch_to.window(tinder_page)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]').click()

time.sleep(3)
driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
like = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button'

for _ in range(50):
    time.sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/button[2]/span').click()
    except NoSuchElementException:
        pass
    time.sleep(2)
    driver.find_element_by_xpath(like).click()
    time.sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]').click()
    except NoSuchElementException:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click()
    except NoSuchElementException:
        pass