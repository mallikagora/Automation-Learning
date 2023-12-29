from selenium import webdriver
from pyshadow.main import Shadow
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
shadow=Shadow(driver)
driver.maximize_window()

driver.get("https://devomni.annalect.com/")

email = driver.execute_script("return document.querySelector('#portal-login > portal-login').shadowRoot.querySelector('#username')")
email.send_keys("adminqa.test@annalect.com")
time.sleep(10)

driver.execute_script("return document.querySelector('#portal-login > portal-login').shadowRoot.querySelector('#eid-login-btn')").click()
time.sleep(6)
password = driver.execute_script("return document.querySelector('#portal-login > portal-login').shadowRoot.querySelector('omni-style > div > div.login-form-container > form > div.password > portal-password').shadowRoot.querySelector('#password')")
password.send_keys("4`>7s`^w2XeE}|")
driver.implicitly_wait(6)

driver.execute_script("document.querySelector('#portal-login > portal-login').shadowRoot.querySelector('#eid-login-btn').click()")
time.sleep(10)

profile=driver.execute_script("return document.querySelector('#outlet > portal-app-container').shadowRoot.querySelector('#header-right > portal-user-selection-menu').shadowRoot.querySelector('omni-style > div > div.dropdown-trigger > portal-user-button').shadowRoot.querySelector('omni-style > button')")
profile.click()
time.sleep(5)

pencil=driver.execute_script("return document.querySelector('#outlet > portal-app-container').shadowRoot.querySelector('#header-right > portal-user-selection-menu').shadowRoot.querySelector('#profile-actions > omni-tooltip:nth-child(1) > button > omni-icon').shadowRoot.querySelector('div')")
pencil.click()
time.sleep(5)

agency=driver.execute_script('return document.querySelector("#outlet > portal-app-container > dummy > user-profile-view").shadowRoot.querySelector("#agency-detail > span").innerText')
print(agency)

requiredtext="Annalect India"

if agency == requiredtext:
    print("True")
else:
    print("False")
time.sleep(10)