import time
from enums.page_response import PageResponse
from pages.base_page import BasePage
from enums.global_enums import GlobalErrorMessage
from pages.main_page import TextBoxPage
from resources.data_json_on_python import URL_CONTACT_US, MAIN_PAGE


class TestElements:
    class TestTextBox:

        def test_text_contact_form_en(self, driver):
            """We are testing the transition of the user from the main page to the application form
            Тестуємо перехід юзера з головної сторінки фо форми заповнення анкети"""
            text_box_page = TextBoxPage(driver, MAIN_PAGE)
            text_box_page.open()
            text_box_page.user_transition_from_the_main_page_to_the_form()
            time.sleep(0.5) #для створення скріншоту
            driver.get_screenshot_as_file("screenshots/MAIN_CONTACT_EN.png")
            assert text_box_page.check_field_apply_now() == PageResponse.FORM_SUBMITTED_OK, GlobalErrorMessage.CONTACT_FORM_NOT_SEND