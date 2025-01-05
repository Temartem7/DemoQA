from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "p[id='name']")
    CREATED_EMAIL = (By.CSS_SELECTOR, "p[id='email']")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "p[id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "p[id='permanentAddress']")

class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR,"button[title='Expand all']")
    ITEMS_LIST = (By.CSS_SELECTOR,"span .rct-title")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, ".text-success")

class RadioButtonPageLocators:

    YES_RADIO_BTN = (By.CSS_SELECTOR, "label[for='yesRadio']")
    NO_RADIO_BTN = (By.CSS_SELECTOR, "label[for='noRadio']")
    IMPRESSIVE_RADIO_BTN = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, ".text-success")


