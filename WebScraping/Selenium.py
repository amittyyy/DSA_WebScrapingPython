from selenium.webdriver import Edge
from selenium.webdriver.common.by import By

driver = Edge()
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
searchEmployer = driver.find_element_by_css_selector('#select2-SelectMain-container')
searchEmployer.click()