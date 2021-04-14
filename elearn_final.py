#importing the required packages and modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException

#defining the class. The class contains 3 methods.
class TestElearn():
    #defining the 1st method under the class.
    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()
    #defining the 2nd method in the class
    def test_elearn(self):
        self.driver = webdriver.Chrome(executable_path="D:\MTECH-BITS-PILANI\seleniumautomation\drivers\chromedriver_win32\chromedriver.exe")
        self.vars = {}
        self.driver.get("https://elearn.bits-pilani.ac.in/")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("2020mt93149@wilp.bits-pilani.ac.in")
        self.driver.find_element(By.ID, "pass").click()
        self.driver.find_element(By.ID, "pass").send_keys("**********")
        self.driver.find_element(By.ID, "submitbtn").click()
        self.driver.find_element(By.LINK_TEXT, "My Courses").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, "#heading6534 .btn").click()
        self.vars["win2784"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win2784"])
        self.driver.find_element(By.ID, "section-0").click()
        self.driver.find_element(By.CSS_SELECTOR, "#module-128339 .instancename").click()
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(30)").click()
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(46)").click()
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(47) > span").click()
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(49)").click()
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(50)").click()
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(51)").click()
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(52)").click()
        self.driver.find_element(By.ID, "intro").click()
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(54)").click()
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(55)").click()
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(56)").click()
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(57)").click()
        time.sleep(5)
        self.driver.quit()

    #defining the 3rd method in the class.
    def test_flighsearch(self):
        self.driver=webdriver.Firefox(executable_path="D:\MTECH-BITS-PILANI\seleniumautomation\drivers\geckodriver-v0.29.0-win64\geckodriver.exe")
        self.driver.get("https://www.makemytrip.com/")
        time.sleep(7)
        try:
            self.driver.find_element(By.CSS_SELECTOR,".chFlights")
            self.driver.find_element(By.CSS_SELECTOR, ".lhUser").click()
            self.driver.find_element(By.CSS_SELECTOR, ".blackText > span:nth-child(2)").click()
            self.driver.find_element(By.CSS_SELECTOR,
                                     ".DayPicker-Month:nth-child(2) .DayPicker-Week:nth-child(3) > .DayPicker-Day:nth-child(2) p:nth-child(1)").click()
            element = self.driver.find_element(By.ID, "toCity")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click_and_hold().perform()
            element = self.driver.find_element(By.CSS_SELECTOR, ".react-autosuggest__input")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).release().perform()
            self.driver.find_element(By.CSS_SELECTOR, ".searchToCity").click()
            self.driver.find_element(By.CSS_SELECTOR, ".react-autosuggest__input").send_keys("mumbai")
            self.driver.find_element(By.CSS_SELECTOR, "#react-autowhatever-1-section-0-item-0 .font12").click()
            self.driver.find_element(By.CSS_SELECTOR, ".DayPicker-Day--selected p:nth-child(1)").click()
            self.driver.find_element(By.CSS_SELECTOR, ".primaryBtn").click()
            self.driver.find_element(By.CSS_SELECTOR, ".filtersOuter:nth-child(3) .makeFlex:nth-child(1) > .makeFlex .box").click()
            time.sleep(10)
            self.driver.quit()
        except NoSuchElementException:
           print(NoSuchElementException)

e=TestElearn()
e.test_elearn()
e.test_flighsearch()