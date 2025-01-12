import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage


class TestElements:

    class TestTextBox:

        def test_text_box(self,driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            text_box_page.fill_all_fields()
            input_data = text_box_page.check_filled_form()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, "checkboxes have not been selected"

    class TestRadioButton:

        def test_radio_button(self,driver):

           radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
           radio_button_page.open()
           radio_button_page.click_on_radio_button("Yes")
           output_yes = radio_button_page.get_output_result().text.strip()
           print(output_yes)
           #assert "Yes" in output_yes

           radio_button_page.click_on_radio_button("Impressive")
           output_impressive = radio_button_page.get_output_result().text
           print(output_impressive)
           #assert "Impressive" in output_impressive

           radio_button_page.click_on_radio_button("No")
           output_no = radio_button_page.get_output_result().text
           print(output_no)
           #assert "No" in output_no
           assert output_yes == "Yes", "Yes, wasn't selected"
           assert output_impressive == "Impressive, Impressive, wasn't selected"
           assert output_no == "No, No, wasn't selected"

    class TestWebTable:

        def test_webtable_add_person(self,driver):
            webtable_page = WebTablePage(driver, "https://demoqa.com/webtables")
            webtable_page.open()
            new_person = webtable_page.add_new_person()
            time.sleep(3)
            table_result = webtable_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result

        def test_webtable_search_person(self, driver):
            webtable_page = WebTablePage(driver, "https://demoqa.com/webtables")
            webtable_page.open()
            first_name = webtable_page.add_new_person()[0]
            webtable_page.search_person_by_name(first_name)
            table_result = webtable_page.check_searched_person()
            print("Key Word: " + first_name)
            print("Table Results: " + table_result)
            assert first_name in table_result

        def test_webtable_update_person_info(self, driver):
            webtable_page = WebTablePage(driver, "https://demoqa.com/webtables")
            webtable_page.open()
            last_name = webtable_page.add_new_person()[1]
            webtable_page.search_person_by_name(last_name)
            age = webtable_page.update_person_info()
            row = webtable_page.check_searched_person()
            print(age)
            print(row)
            assert age in row

        def test_change_row_count(self,driver):
            webtable_page = WebTablePage(driver, "https://demoqa.com/webtables")
            webtable_page.open()
            count = webtable_page.select_amount_of_rows_visible()
            assert count == [5, 10, 20, 25, 50, 100]

    class TestButtonsPage:

        def test_all_buttons(self, driver):
            webtable_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            webtable_page.open()
            double_click = webtable_page.click_different_buttons("double_click")
            right_click = webtable_page.click_different_buttons("right_click")
            dynamic_click = webtable_page.click_different_buttons("dynamic_click")
            print(double_click)
            print(right_click)
            print(dynamic_click)
            assert double_click == "You have done a double click"
            assert right_click == "You have done a right click"
            assert dynamic_click == "You have done a dynamic click"

        def test_double_click(self, driver):
            webtable_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            webtable_page.open()
            double_click = webtable_page.click_different_buttons("double_click")
            print(double_click)
            assert double_click == "You have done a double click"

        def test_right_click(self, driver):
            webtable_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            webtable_page.open()
            right_click = webtable_page.click_different_buttons("right_click")
            print(right_click)
            assert right_click == "You have done a right click"

        def test_dynamic_click(self, driver):
            webtable_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            webtable_page.open()
            dynamic_click = webtable_page.click_different_buttons("dynamic_click")
            print(dynamic_click)
            assert dynamic_click == "You have done a dynamic click"






