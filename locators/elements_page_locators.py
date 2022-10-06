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

class PageLocatorsQuickApply:
    COOKIES = (By.ID, "cn-notice-buttons")
    LOCATION_ANYWHERE = (By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/span[1]/select/option[2]')
    LOCATION_NIGERIA = (By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/span[1]/select/option[3]')
    LOCATION_POLAND = (By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/span[1]/select/option[4]')
    LOCATION_UKRAINE = (By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/span[1]/select/option[5]')
    LOCATION_MACEDONIA = (By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/span[1]/select/option[6]')
    LOCATION_BRAZIL = (By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/span[1]/select/option[7]')
    LOCATION_PORTUGAL = (By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/span[1]/select/option[8]')
    LOCATION_LVIV = (By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/span[1]/select/option[9]')
    TECHNOLOGY = (By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/span[2]/select')
    YOUR_NAME = (By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/span[3]/input')
    YOUR_EMAIL = (By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/span[4]/input')
    UPLOAD_CV = (By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/div[2]/label')
    PRIVACY_POLICY_1 = (By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/span[5]/span/span/label/input')
    PRIVACY_POLICY_2 = (By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/span[6]/span/span/label/input')
    SUBMIT = (By.XPATH, '//*[@id="wpcf7-f12314-p12310-o1"]/form/input')







