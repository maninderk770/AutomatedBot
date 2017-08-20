from selenium import webdriver
import time

chromedriver = webdriver.Chrome(executable_path = 'C:\chromedriver_win32\chromedriver.exe')

url = 'https://www.linkedin.com/uas/login?goback=&trk=hb_signin'

chromedriver.get(url)

# print chromedriver.page_source

email = chromedriver.find_element_by_xpath('//*[@id="session_key-login"]')
email.send_keys('email')


password = chromedriver.find_element_by_xpath('//*[@id="session_password-login"]')
password.send_keys('password')

time.sleep(5)

chromedriver.quit()