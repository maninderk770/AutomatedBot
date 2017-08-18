from selenium import webdriver
import time

chromedriver = webdriver.Chrome(executable_path = 'C:\chromedriver_win32\chromedriver.exe')

url = 'https://www.linkedin.com/uas/login?goback=&trk=hb_signin'

chromedriver.get(url)

print chromedriver.page_source

chromedriver.quit()