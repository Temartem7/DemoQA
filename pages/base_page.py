from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:

    def __init__(self,driver,url, request=None):
        self.driver=driver
        self.url=url

        # If request is passed, check for headless option
        if request:
            headless = request.config.getoption("--headless")
            chrome_options = Options()

            if headless:
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--disable-blink-features=AutomationControlled")
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--no-sandbox")

            # Update the driver to use the new options if headless mode is enabled
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10) -> list[WebElement]:
        return wait(self.driver,timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self,locator, timeout=5):
        return wait(self.driver,timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self,locator, timeout=5):
        return wait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver,timeout).until(EC.invisibility_of_element(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver,timeout).until(EC.element_to_be_clickable(locator))

    def scroll_into_view(self, element_or_locator, timeout=5):
        '''
        Scroll to an element using locator or WebElement
        '''
        if isinstance(element_or_locator, tuple):  # If locator, find the element first
            element = wait(self.driver, timeout).until(EC.presence_of_element_located(element_or_locator))
        else:  # If already a WebElement, use it directly
            element = element_or_locator
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        return element

    def scroll_to(self, element_or_locator, timeout=5, return_element=True):
        """
        Scrolls to an element using a locator or WebElement.
        :param element_or_locator: Can be either a locator (tuple) or a WebElement.
        :param timeout: Maximum wait time in seconds (default: 5).
        :param return_element: If True, returns the WebElement (allows method chaining).
                               If False, just scrolls without returning anything.
        :return: The WebElement if return_element=True, else None.
        """
        if isinstance(element_or_locator, tuple):  # If it's a locator, find the element first
            element = wait(self.driver, timeout).until(EC.visibility_of_element_located(element_or_locator))
        else:  # If it's already a WebElement, use it directly
            element = element_or_locator

        self.driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top + window.scrollY);",
                                   element)
        return element if return_element else None

    def actions_scroll(self, element_or_locator, timeout=5):
        """
        Scrolls to an element using ActionChains.
        :param element_or_locator: Can be either a locator (tuple) or a WebElement.
        :param timeout: Maximum wait time in seconds (default: 5).
        :return: The WebElement after scrolling.
        """
        if isinstance(element_or_locator, tuple):  # If it's a locator, find the element first
            element = wait(self.driver, timeout).until(EC.visibility_of_element_located(element_or_locator))
        else:  # If it's already a WebElement, use it directly
            element = element_or_locator

        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return element  # Returning the element allows method chaining

    def actions_double_click(self, element_or_locator, timeout=10):
        if isinstance(element_or_locator, tuple):  # If it's a locator, find the element first
            element = wait(self.driver, timeout).until(EC.visibility_of_element_located(element_or_locator))
        else:  # If it's already a WebElement, use it directly
            element = element_or_locator

        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        return element  # Returning the element allows method chaining

    def actions_right_click(self, element_or_locator, timeout=10):
        if isinstance(element_or_locator, tuple):  # If it's a locator, find the element first
            element = wait(self.driver, timeout).until(EC.visibility_of_element_located(element_or_locator))
        else:  # If it's already a WebElement, use it directly
            element = element_or_locator

        actions = ActionChains(self.driver)
        actions.context_click(element).perform()
        return element  # Returning the element allows method chaining

    def actions_dynamic_click(self, element_or_locator, timeout=10):
        if isinstance(element_or_locator, tuple):  # If it's a locator, find the element first
            element = wait(self.driver, timeout).until(EC.visibility_of_element_located(element_or_locator))
        else:  # If it's already a WebElement, use it directly
            element = element_or_locator

        actions = ActionChains(self.driver)
        actions.click(element).perform()
        return element  # Returning the element allows method chaining