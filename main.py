import webbrowser, pyautogui
import time, os 
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
# print(dir(os.path))
file = os.path.join(os.path.dirname(os.getcwd()),'index.txt')


url_1  = 'www.gmail.com'
url_2  = 'www.google.com'
pwd = None
email = None

class mailConnect:
	def __init__(self):
		# self.url = 'www.gmail.com'
		self.open = False
		self.moveX = 1344/2
		self.moveY = 744/2
	def passwd(self,pwd):
		time.sleep(4)
		pyautogui.typewrite(f'{pwd}\n', interval=.2)
		return 
	def mail(self, email):
		pyautogui.click(x=self.moveX, y=self.moveY)
		pyautogui.typewrite(f'{email}\n', interval=.2)
		# time.sleep(5)
		return True
	def valid_url(self):
		# if webbrowser.get('windows-default').open_new_tab(self.url) == False:
		return True
	def open_tab(self,url):
		webbrowser.open_new_tab(url)
		time.sleep(7)
		return True
	def close_tab(self):
		return
conn = mailConnect()

d =[ x for x in open(file, 'r') ]
start = True
if start: 
	conn.open_tab(url_1)
	conn.mail(d[0])
	conn.passwd(d[1])
	conn.open_tab(url_2)
#browser= webdriver.Chrome()
#Refreshes the web page
# browser.refresh()
