import time

from enums.page_response import PageResponse
from pages.base_page import BasePage
from enums.global_enums import GlobalErrorMessage
from pages.elements_page import TextBoxPage
from resources.data_json_on_python import URL_CONTACT_US


class TestElements:
    class TestTextBox:

        def test_text_contact_form_en(self, driver):
            """Testing the form for sending data from the user (English): contact-us"""
            """Тестуємо форму відправлення даних від користувача (англіською): contact-us"""
            text_box_page = TextBoxPage(driver, URL_CONTACT_US)
            text_box_page.open()
            text_box_page.fill_all_fields_contuct_us()
            time.sleep(0.5)#для створення скріншоту
            driver.get_screenshot_as_file("screenshots/CONTACT_EN.png")
            assert text_box_page.check_field_contact_us() == PageResponse.FORM_SUBMITTED_OK, GlobalErrorMessage.CONTACT_FORM_NOT_SEND
            """Якщо буде доступ до данних які поступили на сервер то можливо реалізувати перевірку:
            full_name, email, location, company, describe_your_project = ext_box_page.fill_all_fields()
            full_name, email, location, company, describe_your_project = text_box_page.check_field()
            assert full_name == треба доповнити check_field() ящо буде доступ до сервера,
            email ==
            .....
            """

        def test_text_contact_form_ua(self, driver):
            """Testing the form for sending data from the user (Ukraine): contact-us"""
            """Тестуємо форму відправлення даних від користувача (Українською): contact-us"""
            text_box_page = TextBoxPage(driver, URL_CONTACT_US)
            text_box_page.open()
            text_box_page.fill_all_fields_ua_contact_ua()
            time.sleep(0.5)
            driver.get_screenshot_as_file("screenshots/CONTACT_UA.png")
            assert text_box_page.check_field_contact_us() == PageResponse.FORM_SUBMITTED_OK, GlobalErrorMessage.CONTACT_FORM_NOT_SEND

        def test_text_contact_form_large_fields(self, driver):
            """Тестуємо форму відправлення даних від користувача де забагото символів: contact-us"""
            text_box_page = TextBoxPage(driver, URL_CONTACT_US)
            text_box_page.open()
            text_box_page.fill_all_fields_large()
            time.sleep(0.5)
            driver.get_screenshot_as_file("screenshots/CONTACT_LARGE.png")
            assert text_box_page.check_field_contact_us() == PageResponse.FORM_SUBMITTED_OK, GlobalErrorMessage.CONTACT_FORM_NOT_SEND

        def test_contact_form_short(self, driver):
            """Тестуємо форму відправлення даних від користувача де замало символів, але коректний url: contact-us"""
            text_box_page = TextBoxPage(driver, URL_CONTACT_US)
            text_box_page.open()
            text_box_page.fill_all_fields_short()
            time.sleep(0.5)
            driver.get_screenshot_as_file("screenshots/CONTACT_short.png")
            assert text_box_page.check_field_contact_us() == PageResponse.FORM_SUBMITTED_OK, GlobalErrorMessage.CONTACT_FORM_NOT_SEND

        def test_contact_form_without_email(self, driver):
            """Тестуємо форму відправлення даних від користувача не заповнючи email"""
            text_box_page = TextBoxPage(driver, URL_CONTACT_US)
            text_box_page.open()
            text_box_page.fill_fields_without_email()
            time.sleep(0.5)
            driver.get_screenshot_as_file("screenshots/CONTACT_without_email.png")
            assert text_box_page.check_field_have_error() == PageResponse.FIELDS_HAVE_ERROR, GlobalErrorMessage.INCORRECT_DATA


        def test_contact_form_without_full_name(self, driver):
            """Тестуємо форму відправлення даних від користувача не заповнючи full name"""
            text_box_page = TextBoxPage(driver, URL_CONTACT_US)
            text_box_page.open()
            text_box_page.fill_fields_without_full_name()
            time.sleep(0.5)
            driver.get_screenshot_as_file("screenshots/CONTACT_without_name.png")
            assert text_box_page.check_field_have_error() == PageResponse.FIELDS_HAVE_ERROR, GlobalErrorMessage.INCORRECT_DATA