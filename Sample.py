from selenium import webdriver
from pyshadow.main import Shadow
import time

# from Screenshot import Screenshot_clipping

class assingment:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.shadow = Shadow(self.driver)

    def app_omni(self):
        self.driver.get("https://devomni.annalect.com/")

    def login(self):
        username = self.shadow.find_element("#username")
        singIn_btn = self.shadow.find_element("#eid-login-btn")
        password = self.shadow.find_element("#password")

        username.send_keys(self.username)
        singIn_btn.click()
        time.sleep(1)
        password.send_keys(self.password)
        singIn_btn.click()
        time.sleep(20)

    def workspace(self):
        parent = self.shadow.find_element("portal-app-container")
        parent1 = self.shadow.find_element(parent, "portal-nav-menu")
        parent2 = self.shadow.find_element(parent1, "omni-nav-menu")
        parent3 = self.shadow.find_element(parent2, "a[class='menu-item nav-button  is-active ']")
        page_url = self.driver.current_url
        current_page = "my-workspace"
        class_ = " is_active"
        result = current_page in page_url
        classes = self.shadow.get_attribute(parent3, "class")
        result2 = class_ in classes
        print(result, " and ", result2)

    def all_tools(self):
        parent = self.shadow.find_element("portal-app-container")
        parent1 = self.shadow.find_element(parent, "portal-nav-menu")
        parent2 = self.shadow.find_element(parent1, "omni-nav-menu")
        parent3 = self.shadow.find_element(parent2,
                                                    " omni-style:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > div:nth-child(1) > portal-all-tools:nth-child(1) > li:nth-child(1) > omni-tooltip:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
        parent3.click()
        url1 = self.driver.current_url
        self.driver.get_screenshot_as_png()
        self.driver.save_screenshot(url1 + ".png")

    def campaign(self):
        parent = self.shadow.find_element("portal-app-container")
        parent1 = self.shadow.find_element(parent, "portal-nav-menu")
        parent2 = self.shadow.find_element(parent1, "omni-nav-menu")
        parent3_home_btn = self.shadow.find_element(parent2, "omni-style:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > omni-tooltip:nth-child(1) > div:nth-child(1) > a:nth-child(1)")

        time.sleep(5)
        url2 = self.driver.current_url
        self.driver.get_screenshot_as_file(url2 + ".png")
        self.driver.save_screenshot(url2 + ".png")

    def reports(self):
        parent = self.shadow.find_element("portal-app-container")
        parent1 = self.shadow.find_element(parent, "portal-nav-menu")
        parent2 = self.shadow.find_element(parent1, "omni-nav-menu")
        parent3 = self.shadow.find_element(parent2,
                                                    " omni-style:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(4) > omni-tooltip:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
        parent3.click()
        time.sleep(5)
        url3 = self.driver.current_url
        self.driver.get_screenshot_as_file(url3 + ".png")
        self.driver.save_screenshot(url3 + ".png")

    def signOut(self):
        parent = self.shadow.find_element("portal-app-container")
        parent2 = self.shadow.find_element(parent, "portal-user-selection-menu")
        AdminQA = self.shadow.find_element(parent2, ".button.is-text.is-rounded.is-capitalized.is-size-3.has-text-weight-normal")
        AdminQA.click()
        time.sleep(5)
        signOut_dropdown = self.shadow.find_element(parent2, "omni-style:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(12) > div:nth-child(1) > p:nth-child(2)")
        signOut_dropdown.click()
        time.sleep(10)


omni = assingment("adminqa.test@annalect.com", "4`>7s`^w2XeE}|")
omni.app_omni()
omni.login()
omni.workspace()
omni.all_tools()
omni.campaign()
omni.reports()
omni.signOut()
