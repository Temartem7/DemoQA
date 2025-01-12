import random
import time
from random import choices

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):

    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.scroll_to(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address

class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        items_list = self.elements_are_visible(self.locators.ITEMS_LIST)
        if not items_list: #prevent error if no checkboxes are found
            raise Exception("No checkboxes found!")
        item = random.choice(items_list) #picks a random checkbox
        self.scroll_to(item)
        item.click()

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            selected_item = box.find_element(By.XPATH, ".//ancestor::span[@class='rct-text']")
            data.append(selected_item.text)
        #print(data)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        #print(data)
        return str(data).replace(' ', '').lower()

class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_radio_button(self, choice):
        choices = {
            "Yes": self.locators.YES_RADIO_BTN,
            "Impressive": self.locators.IMPRESSIVE_RADIO_BTN,
            "No": self.locators.NO_RADIO_BTN
        }
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT)

class WebTablePage(BasePage):

    locators = WebTablePageLocators()

    def add_new_person(self, count=1):
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BTN).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BTN).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def add_new_client(self, count=1):
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BTN).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BTN).click()
            count -= 1
            data = [first_name, last_name, str(age), email, str(salary), department]
        return data

    def check_new_added_person(self):
        clients_list = self.elements_are_visible(self.locators.FULL_CLIENT_LIST)
        data = []
        for item in clients_list:
            data.append(item.text.splitlines())
        return data

    def search_person_by_name(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_searched_person(self):
        delete_btn = self.element_is_present(self.locators.DELETE_BTN)
        row = delete_btn.find_element(By.XPATH, self.locators.ROW_PARENT)
        return " ".join(row.text.splitlines())
        #return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.EDIT_BTN).click()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BTN).click()
        return str(age)

    def select_amount_of_rows_visible(self):
        count = [5,10,20,25,50,100]
        data = []
        for item in count:
            amount_of_rows_displayed = self.scroll_to(self.element_is_visible(self.locators.TOTAL_ROWS_DISPLAYED))
            amount_of_rows_displayed.click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{item}']")).click()
            data.append(self.check_amount_of_rows())

    def check_amount_of_rows(self):
        list_of_rows = self.elements_are_present(self.locators.FULL_CLIENT_LIST)
        return len(list_of_rows)

