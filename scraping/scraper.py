from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import csv
import pandas as pd
import traceback


def writeUrlsToCsv(csvName, urls):
	print("Writing to csv: ", csvName)
	with open(csvName,'w') as result_file:
		wr = csv.writer(result_file, dialect='excel')
		for url in urls:
			wr.writerow(url)

PATH = "/Users/eshantarneja/Documents/DataScience/storage/chromedriver" 


driver = webdriver.Chrome(PATH)
site="https://www.spotrac.com/nba/contracts/sort-value/all-time/free-agent-2009/limit-100/"
driver.get(site)
data=[]
try:
	main = WebDriverWait(driver,10).until(
		EC.presence_of_element_located((By.CLASS_NAME, "teams"))
		)
	rows = main.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
	for row in rows:
		cols = row.find_elements(By.TAG_NAME, "td")
		info=[]
		for col in cols:
			val=col.text
			print(val)
			info.append(val)
		data.append(info)

finally:
	driver.quit()





writeUrlsToCsv('test.csv', data)



