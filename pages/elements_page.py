import time
from generator.generator import generated_person, generated_person_ua
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields_contuct_us(self):
        """Використовуємо бібліотеку Faker для заповнення форми EN"""
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        location = person_info.location
        company = person_info.company
        massage = person_info.massage

        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_visible(self.locators.LOCATION).click()
        self.element_is_visible(self.locators.NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.MASSAGE).send_keys(massage)
        self.element_is_presents(self.locators.PRIVACY_POLICY).click()
        self.element_is_presents(self.locators.BUTTON_CONTACT_US).click()
        self.go_to_element(self.element_is_visible(self.locators.BUTTON_CONTACT_US))
        return full_name, email, location, company, massage

    """return повертає що було відправленно у форму, для перевірки данніх в assert"""

    def fill_all_fields_ua_contact_ua(self):
        """Використовуємо бібліотеку Faker для заповнення форми UA"""
        person_info = next(generated_person_ua())
        full_name = person_info.full_name
        email = person_info.email
        location = person_info.location
        company = person_info.company
        massage = person_info.massage

        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_visible(self.locators.LOCATION).click()
        self.element_is_visible(self.locators.NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.MASSAGE).send_keys(massage)
        self.element_is_presents(self.locators.PRIVACY_POLICY).click()
        self.element_is_presents(self.locators.BUTTON_CONTACT_US).click()
        self.go_to_element(self.element_is_visible(self.locators.BUTTON_CONTACT_US))
        return full_name, email, location, company, massage

    """return повертає що було відправленно у форму, для перевірки данніх в assert"""

    def fill_all_fields_large(self):
        """Використовуємо бібліотеку Faker для заповнення форми EN"""
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        location = person_info.location
        company = person_info.company
        massage = person_info.massage

        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_visible(self.locators.LOCATION).click()
        self.element_is_visible(self.locators.NAME).send_keys(full_name * 5)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.MASSAGE).send_keys(massage * 5)
        self.element_is_presents(self.locators.PRIVACY_POLICY).click()
        self.element_is_presents(self.locators.BUTTON_CONTACT_US).click()
        self.go_to_element(self.element_is_visible(self.locators.BUTTON_CONTACT_US))
        return full_name, email, location, company, massage

    def fill_all_fields_short(self):
        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_visible(self.locators.LOCATION).click()
        self.element_is_visible(self.locators.NAME).send_keys('t')
        self.element_is_visible(self.locators.EMAIL).send_keys('t@test.t')
        self.element_is_visible(self.locators.MASSAGE).send_keys('t')
        self.element_is_presents(self.locators.PRIVACY_POLICY).click()
        self.element_is_presents(self.locators.BUTTON_CONTACT_US).click()
        self.go_to_element(self.element_is_visible(self.locators.BUTTON_CONTACT_US))

    def check_field_contact_us(self):
        result = self.element_is_visible(self.locators.RESULT_POSITIVE).text
        return result

    def fill_fields_without_email(self):
        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_visible(self.locators.LOCATION).click()
        self.element_is_visible(self.locators.NAME).send_keys('test')
        self.element_is_visible(self.locators.EMAIL).send_keys('')
        self.element_is_visible(self.locators.MASSAGE).send_keys('test')
        self.element_is_presents(self.locators.PRIVACY_POLICY).click()
        self.element_is_presents(self.locators.BUTTON_CONTACT_US).click()
        self.go_to_element(self.element_is_visible(self.locators.BUTTON_CONTACT_US))

    def fill_fields_without_full_name(self):
        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_visible(self.locators.LOCATION).click()
        self.element_is_visible(self.locators.NAME).send_keys('')
        self.element_is_visible(self.locators.EMAIL).send_keys('test@test.test')
        self.element_is_visible(self.locators.MASSAGE).send_keys('test')
        self.element_is_presents(self.locators.PRIVACY_POLICY).click()
        self.element_is_presents(self.locators.BUTTON_CONTACT_US).click()
        self.go_to_element(self.element_is_visible(self.locators.BUTTON_CONTACT_US))

    def check_field_have_error(self):
        result = self.element_is_visible(self.locators.RESULT_FIELDS_HAVE_ERROR).text
        return result
