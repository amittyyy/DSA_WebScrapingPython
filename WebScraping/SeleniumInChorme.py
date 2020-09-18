from hashlib import new

from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('E:/Python/LearningPaython3/WebScraping/Drivers/chromedriver.exe')
# driver.get("http://google.com")
# time.sleep(10)
# driver.quit()


driver.get('https://dev-login.accountantsoffice.com/login?firmCode=&returnurl=https://dev.accountantsoffice.com/Aocommon/account/login')

#Input Cred In Text Fields
firmCodeField = driver.find_element_by_css_selector('#FirmCode').send_keys('ultimate59')
# firmCodeField.send_keys('ultimate59')
userNameField = driver.find_element_by_css_selector('#UserName')
userNameField.clear()
userNameField.send_keys('amitt')

passwordField = driver.find_element_by_css_selector('#Password')
passwordField.clear()
passwordField.send_keys('Simae@678')

# #Click Login Button
userNameField.submit()

driver.find_element_by_xpath('//*[@id="pageContent"]/div/div/div[1]/div[1]/a[4]').click()
# clickPayroll = driver.find_element(by=By.XPATH, value="//a[@href='/AoCommon/Home/Launch/payroll']")
# clickPayroll.click()
# Client Text Search #select2-SelectMain-container
driver.find_element_by_css_selector('#select2-SelectMain-container').click()

searchClient = driver.find_element_by_css_selector('body > span > span > span.select2-search.select2-search--dropdown > input')
searchClient.send_keys('Amanda allstates')


driver.find_element_by_link_text('#select2-SelectMain-results').click()



