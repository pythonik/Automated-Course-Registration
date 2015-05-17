#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

USER_CREDENTIAL = {
	'id': "",
	'pin': ""
}
TERM = "Summer 2015"
SUBJECT = "Computer Science"
COURSE = "2080"
SECTION = ""
TARGET = ""


def select_term(driver):
	term_select_elem = driver.find_element_by_id("term_input_id")
	Select(term_select_elem).select_by_visible_text(TERM)
	submit = driver.find_element_by_xpath("//input[@value='Submit']")
	submit.click()

def select_subject(driver):
	term_select_elem = driver.find_element_by_id("subj_id")
	Select(term_select_elem).select_by_visible_text(SUBJECT)
	search = driver.find_element_by_xpath("//input[@value='Course Search']")
	search.click()

def select_course(driver):
	courses = driver.find_elements_by_tag_name("tr")
	found = False
	for course in courses:
		if found:
			break
		for elem in course.find_elements_by_tag_name('td'):
			if elem.text == COURSE:
				found = True
				btn = course.find_element_by_xpath("//input[@value='View Sections']")
				btn.click()
				break



def automation(driver):
	driver.get(TARGET)
	username = driver.find_element_by_id("UserID")
	pin = driver.find_element_by_name("PIN")
	username.send_keys(USER_CREDENTIAL['id'])
	pin.send_keys(USER_CREDENTIAL['pin'])
	login_button = driver.find_element_by_xpath("//input[@value='Login']")
	login_button.click()
	enrolment_link = driver.find_element_by_link_text('Enrolment & Academic Records')
	enrolment = ActionChains(driver).move_to_element(enrolment_link).click()
	enrolment.perform()
	registration_link = driver.find_element_by_link_text('Registration and Exams')
	enrolment = ActionChains(driver).move_to_element(registration_link).click()
	enrolment.perform()
	lookup_link = driver.find_element_by_link_text('Look Up Classes')
	lookup = ActionChains(driver).move_to_element(lookup_link).click()
	lookup.perform()
	select_term(driver)
	select_subject(driver)
	select_course(driver)
	#driver.close()

if __name__ == '__main__':
	driver = webdriver.Firefox()
	try:
		automation(driver)
	except Exception, e:
		print e
		driver.close()