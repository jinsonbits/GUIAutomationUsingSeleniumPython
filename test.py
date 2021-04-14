import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome(executable_path="D:\MTECH-BITS-PILANI\seleniumautomation\drivers\chromedriver_win32\chromedriver.exe")

#driver.get('https://elearn.bits-pilani.ac.in/')
def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path="D:\MTECH-BITS-PILANI\seleniumautomation\drivers\chromedriver_win32\chromedriver.exe")
    self.vars = {}

def wait_for_window(driver, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = driver.window_handles
    wh_then = var1
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()

driver.get("https://elearn.bits-pilani.ac.in/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Login").click()
driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys("2020mt93149@wilp.bits-pilani.ac.in")
driver.find_element(By.ID, "pass").click()
driver.find_element(By.ID, "pass").send_keys("****")
driver.find_element(By.ID, "submitbtn").click()
driver.find_element(By.LINK_TEXT, "My Courses").click()
var1=driver.window_handles
#vars('window_handles') = driver.window_handles
driver.find_element(By.CSS_SELECTOR, "#heading6534 .btn").click()
var2 =wait_for_window(2000)
root = driver.current_window_handle
driver.switch_to.window(var1)
driver.find_element(By.CSS_SELECTOR, "#module-128339 .instancename").click()
driver.find_element(By.CSS_SELECTOR, ".no-overflow").click()
driver.find_element(By.ID, "action-menu-toggle-0").click()
driver.find_element(By.ID, "yui_3_17_2_1_1617119859366_129").click()
element = driver.find_element(By.ID, "nav_drpdwn")
actions = ActionChains(driver)
actions.move_to_element(element).perform(driver.find_element(By.ID, "nav_drpdwn").click()
element =driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()
driver.find_element(By.LINK_TEXT, "Log Out").click()
driver.close()
driver.switch_to.window(root)
driver.find_element(By.ID, "nav_drpdwn").click()
driver.find_element(By.LINK_TEXT, "Log Out").click()
driver.close()