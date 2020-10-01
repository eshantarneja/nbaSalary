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



# def scrapeDataByDraft():
# 	PATH = "/Users/eshantarneja/Documents/DataScience/storage/chromedriver" 
# 	draftYear=['2003','2004','2005']
# 	data=[]
# 	for year in draftYear:
# 		print("current draft year: ", year)
# 		driver = webdriver.Chrome(PATH)
# 		site ="https://www.spotrac.com/nba/contracts/sort-value/all-time/draft-year-"+year+"/limit-2000/"
# 		driver.get(site)
# 		try:
# 			main = WebDriverWait(driver,10).until(
# 				EC.presence_of_element_located((By.CLASS_NAME, "teams"))
# 				)
# 			rows = main.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
# 			for row in rows:
# 				cols = row.find_elements(By.TAG_NAME, "td")
# 				info=[]
# 				for col in cols:
# 					val=col.text
# 					print(val)
# 					info.append(val)
# 				info.append(year)
# 				data.append(info)

# 		finally:
# 			driver.quit()

# 	writeUrlsToCsv('salaryData.csv', data)

def scrapeData():
	PATH = "/Users/eshantarneja/Documents/DataScience/storage/chromedriver" 
	data=[]
	driver = webdriver.Chrome(PATH)
	site ="https://www.spotrac.com/nba/contracts/sort-value/all-time/limit-20000/"
	driver.get(site)
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

	writeUrlsToCsv('bigList.csv', data)

scrapeData()



