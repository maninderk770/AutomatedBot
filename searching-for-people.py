from selenium import webdriver
import time

myemail = 'your email'
mypassword = 'your password'




chromedriver = webdriver.Chrome(executable_path = 'C:\chromedriver_win32\chromedriver.exe')


def login_linkedin(myemail, mypassword):

	url = 'https://www.linkedin.com/uas/login?goback=&trk=hb_signin'

	chromedriver.get(url)

	chromedriver.maximize_window()

	# print chromedriver.page_source

	email = chromedriver.find_element_by_xpath('//*[@id="session_key-login"]')
	email.send_keys(myemail)


	password = chromedriver.find_element_by_xpath('//*[@id="session_password-login"]')
	password.send_keys(mypassword)


	sign_in = chromedriver.find_element_by_xpath('//*[@id="btn-primary"]')
	sign_in.click()

	time.sleep(10)



login_linkedin( myemail, mypassword )

search_input = chromedriver.find_element_by_xpath('//*[@id="main-search-box"]')
search_input.send_keys('python')

search_button = chromedriver.find_element_by_xpath('//*[@id="global-search"]/fieldset/button')
search_button.click()

people_only = chromedriver.find_element_by_xpath('//*[@id="search-types"]/div/ul/li[2]/a')
people_only.click()

time.sleep(10)



chromedriver.quit()



