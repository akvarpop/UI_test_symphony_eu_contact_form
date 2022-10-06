from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # page contact Us
    COOKIES = (By.ID, "cn-notice-buttons")
    LOCATION = (By.XPATH, '//*[@id="wpcf7-f10029-o1"]/form/span[1]/select/option[2]')
    NAME = (By.XPATH, '//*[@id="wpcf7-f10029-o1"]/form/span[2]/input')
    EMAIL = (By.XPATH, '//*[@id="wpcf7-f10029-o1"]/form/span[3]/input')
    MASSAGE = (By.XPATH, '//*[@id="wpcf7-f10029-o1"]/form/span[4]/textarea')
    PRIVACY_POLICY = (By.XPATH, '//*[@id="wpcf7-f10029-o1"]/form/span[5]/span/span/label/span')
    BUTTON_CONTACT_US = (By.XPATH, '//*[@id="wpcf7-f10029-o1"]/form/input')
    RESULT_POSITIVE = (By.XPATH, '//*[@id="wpcf7-f10029-o1"]/form/div[2]')
    RESULT_FIELDS_HAVE_ERROR = (By.XPATH, '//*[@id="wpcf7-f10029-o1"]/form/div[2]')
    OUR_OFFICE = By.XPATH, '/html/body/main/section[2]/div/h2'

