import time
from generator.generator import generated_person, generated_person_ua
from locators.elements_page_locators import PageLocatorsQuickApply, MainPage
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = MainPage()
    locator = PageLocatorsQuickApply()

    def user_transition_from_the_main_page_to_the_form(self):
        """We are testing the transition of the user from the main page to the application form
        Тестуємо перехід юзера з головної сторінки фо форми заповнення анкети"""
        self.element_is_visible(self.locators.MAIN_LOGO_SS_GO_MAIN).click()
        self.element_is_visible(self.locators.MAIN_MENU_BUTTON_JOIN_US).click()
        assert self.element_is_visible(self.locators.PAGE_JOIN_US_CHECK).text == 'Join Us'
        self.element_is_visible(self.locators.JOIN_US_PAGE_LOCATION_LIST).click()
        self.element_is_visible(self.locators.JOIN_US_PAGE_LOCATION_LIST_UKRAINE).click()
        assert self.element_is_visible \
                   (self.locators.CHECK_JOIN_US_PAGE_LOCATION_LIST_UKRAINE).text == 'Vacancies in Ukraine'
        self.element_is_visible(self.locators.BUTTON_APPLY_NOW).click()
        assert self.element_is_visible(self.locators.CHECK_PAGE_APPLY_NOW).text == 'Apply Now!'

        """Використовуємо бібліотеку Faker для заповнення форми EN"""
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        location = person_info.location
        company = person_info.company
        massage = person_info.massage

        #self.element_is_visible(self.locator.COOKIES).click()
        self.element_is_visible(self.locator.LOCATION_ANYWHERE).click()
        self.element_is_visible(self.locator.YOUR_NAME).send_keys(full_name)
        self.element_is_visible(self.locator.YOUR_EMAIL).send_keys(email)
        self.element_is_presents(self.locator.UPLOAD_CV).send_keys('/Users/antongrunt/Desktop/project/symphony'
                                                                    '-solutions.eu_contact_form/test.pdf')
        self.go_to_element(self.element_is_visible(self.locator.PRIVACY_POLICY_1))
        time.sleep(2)
        self.element_is_presents(self.locator.PRIVACY_POLICY_1).click()
        self.element_is_presents(self.locator.PRIVACY_POLICY_2).click()
        self.element_is_presents(self.locator.SUBMIT).click()
        self.go_to_element(self.element_is_presents(self.locator.PRIVACY_POLICY_2))
        return full_name, email, location, company, massage

    """return повертає що було відправленно у форму, для перевірки данніх в assert"""



    def check_field_apply_now(self):
        result = self.element_is_visible(self.locator.RESULT_POSITIVE).text
        return result
