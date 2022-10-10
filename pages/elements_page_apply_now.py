import time
from generator.generator import generated_person, generated_person_ua
from locators.elements_page_locators import PageLocatorsQuickApply
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = PageLocatorsQuickApply()

    def fill_all_fields_apply_now(self):
        """Використовуємо бібліотеку Faker для заповнення форми EN"""
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        location = person_info.location
        company = person_info.company
        massage = person_info.massage

        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_visible(self.locators.LOCATION_ANYWHERE).click()
        self.element_is_visible(self.locators.YOUR_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.YOUR_EMAIL).send_keys(email)
        self.element_is_presents(self.locators.UPLOAD_CV).send_keys('/Users/antongrunt/Desktop/project/symphony'
                                                                    '-solutions.eu_contact_form/test.pdf')
        self.go_to_element(self.element_is_visible(self.locators.PRIVACY_POLICY_1))
        time.sleep(2)
        self.element_is_presents(self.locators.PRIVACY_POLICY_1).click()
        self.element_is_presents(self.locators.PRIVACY_POLICY_2).click()
        self.element_is_presents(self.locators.SUBMIT).click()
        self.go_to_element(self.element_is_presents(self.locators.PRIVACY_POLICY_2))
        return full_name, email, location, company, massage

    """return повертає що було відправленно у форму, для перевірки данніх в assert"""

    def fill_all_fields_apply_now_ua(self):
        """Використовуємо бібліотеку Faker для заповнення форми UA"""
        person_info = next(generated_person_ua())
        full_name = person_info.full_name
        email = person_info.email
        location = person_info.location
        company = person_info.company
        massage = person_info.massage

        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_visible(self.locators.LOCATION_ANYWHERE).click()
        self.element_is_visible(self.locators.YOUR_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.YOUR_EMAIL).send_keys(email)
        self.element_is_presents(self.locators.UPLOAD_CV).send_keys('/Users/antongrunt/Desktop/project/symphony'
                                                                    '-solutions.eu_contact_form/test.pdf')
        self.go_to_element(self.element_is_visible(self.locators.PRIVACY_POLICY_1))
        time.sleep(2)
        self.element_is_presents(self.locators.PRIVACY_POLICY_1).click()
        self.element_is_presents(self.locators.PRIVACY_POLICY_2).click()
        self.element_is_presents(self.locators.SUBMIT).click()
        self.go_to_element(self.element_is_presents(self.locators.PRIVACY_POLICY_2))
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
        self.element_is_visible(self.locators.LOCATION_ANYWHERE).click()
        self.element_is_visible(self.locators.YOUR_NAME).send_keys(full_name * 10)
        self.element_is_visible(self.locators.YOUR_EMAIL).send_keys(email)
        self.element_is_presents(self.locators.UPLOAD_CV).send_keys('/Users/antongrunt/Desktop/project/symphony'
                                                                    '-solutions.eu_contact_form/test.pdf')
        self.go_to_element(self.element_is_visible(self.locators.PRIVACY_POLICY_1))
        time.sleep(2)
        self.element_is_presents(self.locators.PRIVACY_POLICY_1).click()
        self.element_is_presents(self.locators.PRIVACY_POLICY_2).click()
        self.element_is_presents(self.locators.SUBMIT).click()
        self.go_to_element(self.element_is_presents(self.locators.PRIVACY_POLICY_2))
        return full_name, email, location, company, massage

    def fill_all_fields_short(self):
        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_visible(self.locators.LOCATION_ANYWHERE).click()
        self.element_is_visible(self.locators.YOUR_NAME).send_keys('t')
        self.element_is_visible(self.locators.YOUR_EMAIL).send_keys('test@test.test')
        self.element_is_presents(self.locators.UPLOAD_CV).send_keys('/Users/antongrunt/Desktop/project/symphony'
                                                                    '-solutions.eu_contact_form/test.pdf')
        self.go_to_element(self.element_is_visible(self.locators.PRIVACY_POLICY_1))
        time.sleep(2)
        self.element_is_presents(self.locators.PRIVACY_POLICY_1).click()
        self.element_is_presents(self.locators.PRIVACY_POLICY_2).click()
        self.element_is_presents(self.locators.SUBMIT).click()
        self.go_to_element(self.element_is_presents(self.locators.PRIVACY_POLICY_2))

    def check_field_apply_now(self):
        result = self.element_is_visible(self.locators.RESULT_POSITIVE).text
        return result

    def fill_fields_without_email(self):
        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_visible(self.locators.LOCATION_ANYWHERE).click()
        self.element_is_visible(self.locators.YOUR_NAME).send_keys('test')
        self.element_is_visible(self.locators.YOUR_EMAIL).send_keys('')
        self.element_is_presents(self.locators.UPLOAD_CV).send_keys('/Users/antongrunt/Desktop/project/symphony'
                                                                    '-solutions.eu_contact_form/test.pdf')
        self.go_to_element(self.element_is_visible(self.locators.PRIVACY_POLICY_1))
        time.sleep(2)
        self.element_is_presents(self.locators.PRIVACY_POLICY_1).click()
        self.element_is_presents(self.locators.PRIVACY_POLICY_2).click()
        self.element_is_presents(self.locators.SUBMIT).click()
        self.go_to_element(self.element_is_presents(self.locators.PRIVACY_POLICY_2))

    def fill_fields_without_full_name(self):
        self.element_is_visible(self.locators.COOKIES).click()
        self.element_is_visible(self.locators.LOCATION_ANYWHERE).click()
        self.element_is_visible(self.locators.YOUR_NAME).send_keys('')
        self.element_is_visible(self.locators.YOUR_EMAIL).send_keys('test@test.test')
        self.element_is_presents(self.locators.UPLOAD_CV).send_keys('/Users/antongrunt/Desktop/project/symphony'
                                                                    '-solutions.eu_contact_form/test.pdf')
        self.go_to_element(self.element_is_visible(self.locators.PRIVACY_POLICY_1))
        time.sleep(2)
        self.element_is_presents(self.locators.PRIVACY_POLICY_1).click()
        self.element_is_presents(self.locators.PRIVACY_POLICY_2).click()
        self.element_is_presents(self.locators.SUBMIT).click()
        self.go_to_element(self.element_is_presents(self.locators.PRIVACY_POLICY_2))

    def check_field_have_error(self):
        result = self.element_is_visible(self.locators.RESULT_FIELDS_HAVE_ERROR).text
        return result
