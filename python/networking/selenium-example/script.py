import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#enter the link to the website you want to automate login.
website_link="https://secure.etecsa.net:8443/"
#enter your login username
username="aalayo2015@nauta.com.cu"
#enter your login password
password="Melquisedec12*"

#enter the element for username input field
element_for_username="username"
#enter the element for password input field
element_for_password="password"
#enter the element for submit button
element_for_submit="Enviar"

browser = webdriver.Chrome()	#for macOS users[for others use chrome vis chromedriver]
browser.get((website_link))	

try:
	username_element = browser.find_element_by_name(element_for_username)
	username_element.send_keys(username)		
	password_element  = browser.find_element_by_name(element_for_password)
	password_element.send_keys(password)
	signInButton = browser.find_element_by_name(element_for_submit)
	signInButton.click()
	
	#### to quit the browser uncomment the following lines ####
	# time.sleep(3)
	# browser.quit()
	# time.sleep(1)
	# browserExe = "Safari"
	# os.system("pkill "+browserExe)
except Exception:
	#### This exception occurs if the element are not found in the webpage.
	print("Some error occured :(")

	#### to quit the browser uncomment the following lines ####
	# browser.quit()
	# browserExe = "Safari"
	# os.system("pkill "+browserExe)


