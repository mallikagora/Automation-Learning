import time
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://devomni.annalect.com/login")
driver.maximize_window()
time.sleep(5)


username=driver.execute_script("return document.querySelector('#portal-login > portal-login').shadowRoot.querySelector('#username')")
username.send_keys("adminqa.test@annalect.com")

#driver.execute_script("document.querySelector('#portal-login > portal-login').shadowRoot.querySelector('#username')").send_keys("adminqa.test@annalect.com")

time.sleep(5)

sign=driver.execute_script("return document.querySelector('#portal-login > portal-login').shadowRoot.querySelector('#eid-login-btn')")
sign.click()
time.sleep(5)

password=driver.execute_script("return document.querySelector('#portal-login > portal-login').shadowRoot.querySelector('omni-style > div > div.login-form-container > form > div.password > portal-password').shadowRoot.querySelector('#password')")
password.send_keys("4`>7s`^w2XeE}|")
time.sleep(5)

sign=driver.execute_script("return document.querySelector('#portal-login > portal-login').shadowRoot.querySelector('#eid-login-btn')")
sign.click()
time.sleep(25)

alltools=driver.execute_script("return document.querySelector('#outlet > portal-app-container').shadowRoot.querySelector('#nav-background > portal-nav-menu').shadowRoot.querySelector('omni-style > omni-nav-menu').shadowRoot.querySelector('#All-Tools > omni-tooltip > div:nth-child(1) > a > omni-icon').shadowRoot.querySelector('div > svg > path')")
alltools.click()
time.sleep(10)

icp=driver.execute_script("return document.querySelector('#outlet > portal-app-container').shadowRoot.querySelector('#nav-background > portal-nav-menu').shadowRoot.querySelector('omni-style > omni-nav-menu').shadowRoot.querySelector('#top-section > ul:nth-child(1) > div:nth-child(1) > portal-all-tools').shadowRoot.querySelector('#dropdown-menu > div > div > div:nth-child(2) > a:nth-child(10) > p')")
icp.click()
time.sleep(10)

iframe=driver.execute_script('return document.querySelector("#outlet > portal-app-container").shadowRoot.querySelector("omni-app-layout > portal-iframe-container").shadowRoot.querySelector("omni-style > portal-iframe-element").shadowRoot.querySelector("iframe")')
driver.switch_to.frame(iframe)
# create=driver.execute_script('return document.querySelector("body > omni-app-container").shadowRoot.querySelector("omni-style > omni-context-provider > omni-app-layout > content > main > planning-tools > landing-page").shadowRoot.querySelector("omni-style > div > button")')
# create.click()
Select = driver.execute_script('return document.querySelector("body > omni-app-container").shadowRoot.querySelector("omni-style > omni-context-provider > omni-app-layout > content > main > planning-tools > landing-page").shadowRoot.querySelector("#landing-page").shadowRoot.querySelector("omni-style > div:nth-child(1) > div.dropdown > div.dropdown-trigger > button")')
Select.click()
Search = driver.find_element(By.ID, "search")
Search.click()
time.sleep(10)