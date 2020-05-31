from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("\n*****Automated News Using Selenium*****\n")
print("Choose a Topic :")
str=input()
if str.endswith("News") or str.endswith("news"):
	pass
else:
	str = str + " News"

driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://google.com')

search_bar = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
search_bar.send_keys(str)
search_bar.send_keys(Keys.ENTER)
driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)
time.sleep(2)
search_news = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/a/h3')
search_news.click()


