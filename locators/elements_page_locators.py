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

class WebTablePageLocators:

    #add person form
    ADD_BTN = (By.CSS_SELECTOR, "#addNewRecordButton")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#lastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#userEmail")
    AGE_INPUT = (By.CSS_SELECTOR, "#age")
    SALARY_INPUT = (By.CSS_SELECTOR, "#salary")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "#department")
    SUBMIT_BTN = (By.CSS_SELECTOR, "#submit")

    #table
    FULL_CLIENT_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#searchBox")
    DELETE_BTN = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"

    #update
    EDIT_BTN = (By.CSS_SELECTOR, "span[title='Edit']")
    TOTAL_ROWS_DISPLAYED = (By.CSS_SELECTOR, "select[aria-label='rows per page']")



