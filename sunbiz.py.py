from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
path_to_chromedriver = 'C:/Users/Suggu/Downloads/chromedriver_win32/chromedriver' 

file = open('sample.txt', 'r')
list_of_rows = file.read().split('\n')
Details=[]
for i in list_of_rows:
	print i
	browser = webdriver.Chrome(executable_path = path_to_chromedriver)
	url = 'http://search.sunbiz.org/Inquiry/CorporationSearch/ByName'
	browser.get(url)
	assert "Search for Corporations" in browser.title
	elem = browser.find_element_by_id("SearchTerm")
	elem.clear()
	elem.send_keys(i)
	elem.send_keys(Keys.RETURN)
	browser.find_element_by_css_selector('#search-results table tbody tr td a').click()
	try:
		entity_Name_detail=browser.find_element_by_css_selector('div.searchResultDetail div.detailSection p:nth-child(1)').text
	except:
		entity_Name_detail=""
	try:	
		principal_Address_detail=browser.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div[3]/span[2]/div').text
	except:	
		principal_Address_detail=""	
	try:
		mailing_Address_detail=browser.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div[4]/span[2]/div').text
	except:
		mailing_Address_detail=""	
	try:
		officer_detail=browser.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div[6]').text
	except:
		officer_detail=""
	print entity_Name_detail
	entity_Name_detail=str(entity_Name_detail)
	print principal_Address_detail
	principal_Address_detail=str(principal_Address_detail)
	print mailing_Address_detail
	mailing_Address_detail=str(mailing_Address_detail)
	print officer_detail
	officer_detail=str(officer_detail)
	Details.append({'entity_Name_detail':entity_Name_detail, 'principal_Address_detail':principal_Address_detail,'mailing_Address_detail':mailing_Address_detail, 'officer_details':officer_detail})
	writefile = open('ouput25.txt',"a")
	writefile.write(""" 1 - name of the entity - %s & %s\n2 - Principle Address \n%s\n3 - Mailing Address\n%s\n4 - Officer Detail\n%s
\n"""%(i,entity_Name_detail,principal_Address_detail,mailing_Address_detail,officer_detail))