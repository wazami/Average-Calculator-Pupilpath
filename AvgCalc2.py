##Average Calculator 2.0
from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

#OSIS = int(input("What is your OSIS number?: "))
#Password = str(raw_input("What is your password?: "))
driver = webdriver.Chrome("/Users/HNizami/Downloads/chromedriver")

def PupilPath(webdriver): 
	#login 
	driver.get("https://pupilpath.skedula.com//")
	driver.get("https://auth.ioeducation.com/users/sign_in")
	username_login_region = driver.find_element_by_id("user_username")
	username_login_region.send_keys("<INPUT YOUR OSIS>") 
	username_login_region.submit()
	time.sleep(1)
	password_login_region = driver.find_element_by_xpath(".//*[@id='user_password']")
	try: 
		password_login_region.send_keys("<INPUT YOUR PUPILPATH PASSWORD>") 
	except ElementNotVisibleException: 
		print("Element Not Visible Exception")
		pass
		#PupilPath() 
	password_submit = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[1]/div[2]/form/button[2]')
	password_submit.submit()
	driver.get("https://auth.ioeducation.com/auth/authorize?client_id=pupilpath_id&view=pupilpath")
	driver.get("https://pupilpath.skedula.com/auth/login/")
	driver.find_element_by_id("DBN_chzn").click()
	driver.find_element_by_id("DBN_chzn_o_3").click()
	driver.find_element_by_id("loginSKD").click()
	time.sleep(1)

def overall_average_calc(averages): 
	weighted_gpa = (sum(averages)) / (len(averages))
 	print(weighted_gpa)

def apBio(webdriver, averages):
	driver.find_element_by_xpath(".//*[@id='progress-card']/tbody/tr[8]/td[3]").click()
	time.sleep(5)

	#Gets the categories 
	try: 
		element1 = driver.find_element_by_xpath(".//*[@id='GradeBreakdown']/div[6]/table/tbody/tr[1]/td[1]").text
		category1 = []
		element2 = driver.find_element_by_xpath(".//*[@id='GradeBreakdown']/div[6]/table/tbody/tr[2]/td[1]").text
		category2 = []
		element3 = driver.find_element_by_xpath(".//*[@id='GradeBreakdown']/div[6]/table/tbody/tr[3]/td[1]").text
		category3 = []
		element4 = driver.find_element_by_xpath(".//*[@id='GradeBreakdown']/div[6]/table/tbody/tr[4]/td[1]").text
		category4 = []
	except NoSuchElementException:
		print("Element Not Found")

	#Get the weight of each category 
	try: 
		weighting1 = driver.find_element_by_xpath(".//*[@id='GradeBreakdown']/div[6]/table/tbody/tr[1]/td[2]").text.strip('%')
		weighting1 = int(weighting1) 
		weighting1 = weighting1 * 0.01 
		weighting2 = driver.find_element_by_xpath(".//*[@id='GradeBreakdown']/div[6]/table/tbody/tr[2]/td[2]").text.strip('%')
		weighting2 = int(weighting2) 
		weighting2 = weighting2 * 0.01 
		weighting3 = driver.find_element_by_xpath(".//*[@id='GradeBreakdown']/div[6]/table/tbody/tr[3]/td[2]").text.strip('%')
		weighting3 = int(weighting3) 
		weighting3 = weighting3 * 0.01 
		weighting4 = driver.find_element_by_xpath(".//*[@id='GradeBreakdown']/div[6]/table/tbody/tr[4]/td[2]").text.strip('%')
		weighting4 = int(weighting4) 
		weighting4 = weighting4 * 0.01 
	except NoSuchElementException:
		print("Element Not Found")

	#founds how many rows in the homework table there are 
	table1_rows = 1 
	while True:
		table1_rows = str(table1_rows)
		driver.find_element_by_xpath(".//*[@id='GradeBreakdown']/div[2]/table/tbody/tr[" + table1_rows + "]").text
		table1_rows = int(table1_rows)
		table1_rows += 1 
		if NoSuchElementException: 
			break

	#calculates how many total points you get. So lets say you have Homework weighted at 10%
	#and you got a 100 and a 90 on the two assignments. You take the average of the assignemnts (95)
	#and then multiply by .1 to get 9.5. That means you recieved 9.5 out of 10 possible Homework
	#points. 
	table1_grades = [] 
	counter = 1 
	for x in range(0, table1_rows): 
		counter = str(counter)
		grades = driver.find_element_by_xpath(".//*[@id='GradeBreakdown']/div[2]/table/tbody/tr[" + counter + "]/td[5]/span").text.strip("%")
		grades = int(grades) 
		table1_grades.append(grades)
		counter = int(counter) 
		counter += 1 
	table1_points = (sum(table1_grades) / len(table1_grades)) * weighting1 


	#find how many rows in Classwork 
	table2_rows = 1 
	while True:
		table2_rows = str(table2_rows)
		thing = driver.find_element_by_xpath(".//*[@id='GradeBreakdown']/div[3]/table/tbody/tr[" + table2_rows + "]").text
		#print(thing)
		if NoSuchElementException: 
			break
		else: 
			table2_rows = int(table2_rows)
			table2_rows += 1 
	#print(table2_rows)
	table2_rows = int(table2_rows)
	table2_grades = [] 
	counter = 1 
	for x in range(0, table2_rows): 
		counter = str(counter)
		grades = driver.find_element_by_xpath(".//*[@id='GradeBreakdown']/div[3]/table/tbody/tr/td[5]/span").text.strip("%")
		grades = int(grades) 
		table2_grades.append(grades)
		counter = int(counter) 
		counter += 1 
	table2_points = (sum(table2_grades) / len(table2_grades)) * weighting2


	#find how many rows in Exams 
	table3_rows = 1 
	while True:
		table3_rows = str(table3_rows)
		driver.find_element_by_xpath(".//*[@id='GradeBreakdown']/div[3]/table/tbody/tr[" + table3_rows + "]").text
		if NoSuchElementException: 
			break
		else: 
			table3_rows = int(table3_rows)
			table3_rows += 1 
	#print(table2_rows)
	table3_rows = int(table3_rows)
	table3_grades = [] 
	counter = 1 
	for x in range(0, table3_rows): 
		counter = str(counter)
		grades = driver.find_element_by_xpath(".//*[@id='GradeBreakdown']/div[4]/table/tbody/tr/td[5]/span").text.strip("%")
		grades = int(grades) 
		table3_grades.append(grades)
		counter = int(counter) 
		counter += 1 
	table3_points = (sum(table3_grades) / len(table3_grades)) * weighting3

	table4_rows = 1 
	while True:
		table4_rows = str(table4_rows)
		try: 
			driver.find_element_by_xpath(".//*[@id='GradeBreakdown']/div[3]/table/tbody/tr[" + table4_rows + "]").text
		except NoSuchElementException: 
			table4_points = 20 
			break
		else: 
			table4_rows = int(table4_rows)
			table4_rows += 1 
	overall_class_average = (table1_points + table2_points + table3_points + table4_points) * 1.1
	averages.append(overall_class_average)


def otherClasses(webdriver): 
	not_classes = ["PE and Health ", "Functional Codes ", "Guidance "]
	averages = []
	dashed_averages = []
	class_titles_iterated = 1  
	while True:
		class_titles_iterated = str(class_titles_iterated)
		try: 
			subject = driver.find_element_by_xpath(".//*[@id='progress-card']/tbody/tr[" + class_titles_iterated + "]/td[4]").text
			if subject not in not_classes: 
				class_name = driver.find_element_by_xpath(".//*[@id='progress-card']/tbody/tr[" + class_titles_iterated + "]/td[2]").text
				try: 
					if "AP" in class_name: 
						ap_class_grade = driver.find_element_by_xpath(".//*[@id='progress-card']/tbody/tr[" + class_titles_iterated + "]/td[5]/span").text
						if "-" in ap_class_grade: 
							dashed_averages.append(ap_class_grade)
							#apBio(driver, averages)
						else: 
							ap_class_grade = float(ap_class_grade)
							weighted_average = ap_class_grade * 1.1 
							averages.append(weighted_average)
					elif "SCHOLARS" in class_name: 
						scholars_class_grade = driver.find_element_by_xpath(".//*[@id='progress-card']/tbody/tr[" + class_titles_iterated + "]/td[5]/span").text
						if "-" in scholars_class_grade: 
							dashed_averages.append(scholars_class_grade)
						scholars_class_grade = float(scholars_class_grade)
						scholars_class_grade = scholars_class_grade * 1.05
						averages.append(scholars_class_grade)
					else: 
						class_grade = driver.find_element_by_xpath(".//*[@id='progress-card']/tbody/tr[" + class_titles_iterated + "]/td[5]/span").text
						if "-" in class_grade: 
							dashed_averages.append(class_grade)
						class_grade = float(class_grade)
						averages.append(class_grade)
				except NoSuchElementException: 
					inform_client = int(input("There is no grade for a class. Please give your best prediction of your grade: "))
					averages.append(inform_client)
			class_titles_iterated  = int(class_titles_iterated)
			class_titles_iterated  += 1 
		except NoSuchElementException: 
			class_titles_iterated  = int(class_titles_iterated)
			class_titles_iterated = class_titles_iterated - 1 
			break
	if len(dashed_averages) != 0: 
		apBio(driver, averages)
	print(averages)
	overall_average_calc(averages)




PupilPath(driver)
otherClasses(driver)