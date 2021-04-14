#importing the required packages and modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#defining the class. The class contains 2 methods.
class TestElearn():
    #defining the 1st method under the class.
    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    
    #defining the 2nd method in the class.
    def test_flighsearch(self):
        self.driver=webdriver.Firefox(executable_path="\drivers\geckodriver.exe")
        # self.driver=webdriver.Firefox(executable_path="\drivers\chromedriver.exe")
        self.driver.get("https://www.makemytrip.com/")
         self.driver.maximize_window()
        time.sleep(10)
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
            time.sleep(20)
            self.driver.quit()
        except NoSuchElementException:
            print(NoSuchElementException)
e=TestElearn()
e.test_flighsearch()