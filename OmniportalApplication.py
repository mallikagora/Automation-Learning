import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://devomni.annalect.com/login")

email = driver.execute_script("return document.querySelector('#portal-login > portal-login').shadowRoot.querySelector('#username')")
email.send_keys("adminqa.test@annalect.com")
time.sleep(10)

driver.execute_script("return document.querySelector('#portal-login > portal-login').shadowRoot.querySelector('#eid-login-btn')").click()
time.sleep(6)
password = driver.execute_script("return document.querySelector('#portal-login > portal-login').shadowRoot.querySelector('omni-style > div > div.login-form-container > form > div.password > portal-password').shadowRoot.querySelector('#password')")
password.send_keys("4`>7s`^w2XeE}|")
driver.implicitly_wait(6)

driver.execute_script("return document.querySelector('#portal-login > portal-login').shadowRoot.querySelector('omni-style > div > div.login-form-container > form > div.login-btn-container')").click()
time.sleep(50)


Alltools = driver.execute_script("return document.querySelector('#outlet > portal-app-container').shadowRoot.querySelector('#nav-background > portal-nav-menu').shadowRoot.querySelector('omni-style > omni-nav-menu').shadowRoot.querySelector('#All-Tools > omni-tooltip > div:nth-child(1) > a')")
Alltools.click()
time.sleep(10)
act = ActionChains(driver)
act.move_to_element(Alltools).perform()
url = driver.current_url
driver.get_screenshot_as_file("url + .png")
#driver.get_screenshot_as_file("All tools.png")
time.sleep(20)

currentTab = driver.current_window_handle
for tab in driver.window_handles:
    if not (tab == currentTab):
        driver.switch_to.window(tab)
currentTab = driver.execute_script("return document.querySelector('#outlet > portal-app-container').shadowRoot.querySelector('#nav-background > portal-nav-menu').shadowRoot.querySelector('omni-style > omni-nav-menu').shadowRoot.querySelector('#Campaigns > omni-tooltip > div:nth-child(1) > a > omni-icon').shadowRoot.querySelector('div > svg')")
currentTab.click()
time.sleep(10)
url = driver.current_url
driver.get_screenshot_as_file("url + .png")
time.sleep(20)

currentTab = driver.current_window_handle
for tab in driver.window_handles:
    if not (tab == currentTab):
        driver.switch_to.window(tab)
currentTab = driver.execute_script("return document.querySelector('#outlet > portal-app-container').shadowRoot.querySelector('#nav-background > portal-nav-menu').shadowRoot.querySelector('omni-style > omni-nav-menu').shadowRoot.querySelector('#Reports > omni-tooltip > div:nth-child(1) > a')")
currentTab.click()
time.sleep(10)
url = driver.current_url
driver.get_screenshot_as_file("url + .png")
#driver.get_screenshot_as_file("Reports.png")
time.sleep(10)

currentTab = driver.current_window_handle
for tab in driver.window_handles:
    if not (tab == currentTab):
        driver.switch_to.window(tab)
currentTab = driver.execute_script("return document.querySelector('#outlet > portal-app-container').shadowRoot.querySelector('#header-right > portal-user-selection-menu').shadowRoot.querySelector('omni-style > div > div.dropdown-trigger > portal-user-button').shadowRoot.querySelector('omni-style > button')")
currentTab.click()
time.sleep(20)

driver.execute_script("document.querySelector('#outlet > portal-app-container').shadowRoot.querySelector('#header-right > portal-user-selection-menu').shadowRoot.querySelector('omni-style > div > div.dropdown-menu > div > a:nth-child(12) > div > p')")
time.sleep(20)
act = ActionChains(driver)
act.click_and_hold().perform()
driver.quit()

