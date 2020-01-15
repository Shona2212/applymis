import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import unicodecsv as csv
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os

from date_picker import date_req

def apply_table():

	date = date_req()

	apply_sheet = "Applies_"+date+".csv"
	#apply_data = pd.read_csv("apply_tod.csv")
	#numb_apply = apply_data[apply_data.FlowName=='107_applyTypeCountTracing']

	#sheet_apply = numb_apply.drop(['FlowName'], axis = 1)

	# path setting
    	driverpath = '/home/shona/Documents/chromedriver'
    	download_dir = '/home/shona/Downloads/Projects'


	# browser options
    	#chrome_options = Options()
    	#chrome_options.add_argument("--headless")
    	driver = webdriver.Chrome(executable_path=driverpath)
    	#enable_download_in_headless_chrome(driver, download_dir)


	# running browser
    	#driver = webdriver.Chrome(driverpath)
    	driver.get('http://centraldashboard.infoedge.com/app/kibana#/dashboard/organic-crawled-applies-views')

	time.sleep(20)

	
	# query input on search
    	elem = driver.find_element_by_xpath("//a[./pretty-duration]")
	elem.click()
	print("------Duration Button click------")
    	time.sleep(20)

	elem2 = driver.find_element_by_xpath("//a[.='quick']")
	elem2.click()
	print("------Quick Relative Button click------")
	time.sleep(10)

	elem3 = driver.find_element_by_xpath("//a[.='Yesterday']")
	elem3.click()
	print("------Yesterday Button click------")
	time.sleep(100)


	elem4 = driver.find_element_by_xpath("//div[./div/span[contains(@title,'crawled-company-job-wise-applies-and-jdviews')]]//a[contains(.,'Formatted ')]")
	elem4.click()
	print("------Download Button click------")
	time.sleep(15)

	print("------Downloaded Sheet------")

	time.sleep(5)

	driver.close()

	os.rename('/home/shona/Downloads/crawled-company-job-wise-applies-and-jdviews.csv', '/home/shona/Downloads/'+apply_sheet)

	sheet_apply = pd.read_csv("/home/shona/Downloads/"+apply_sheet)

	print sheet_apply.head(5)

	return sheet_apply


if __name__=='__main__':
	apply_table()
