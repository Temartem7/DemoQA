from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self,driver,url):
        self.driver=driver
        self.url=url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver,timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self,locator, timeout=5):
        return wait(self.driver,timeout).until(EC.presence_of_element_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver,timeout).until(EC.invisibility_of_element(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver,timeout).until(EC.element_to_be_clickable(locator))

    def scroll_into_view(self, locator, timeout=5):
        element = wait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        return element

    def scroll_to(self, locator, timeout=5, return_element = True):    #return_element = False (Just scroll, no return, can't chain methods)
        element = wait(self.driver,timeout).until(EC.visibility_of_element_located(locator)) #return_element = True (Scroll & return, can chain methods)
        self.driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top + window.scrollY);", element)
        return element if return_element else None


    def scroll_with_action(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
