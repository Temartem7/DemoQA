import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


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




