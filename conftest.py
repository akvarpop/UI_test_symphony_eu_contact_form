import pytest
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


options = Options()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
# ua = UserAgent()
# userAgent = ua.random
# print(userAgent)
# options.add_argument(f'user-agent={userAgent}')
"""
Код для запуска с ПК  
"""
@pytest.fixture(scope='function', autouse=True)
def driver():
    driver = webdriver.Chrome(chrome_options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.delete_all_cookies()
    yield driver
    driver.quit()







"""Код для запуск через контейнер"""
# useragent = UserAgent()
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-ssl-errors=yes')
# options.add_argument('--ignore-certificate-errors')
# options.add_argument(f"user-agent={useragent.cache}")
# options.add_argument(f"user-agent={useragent.random}")


# @pytest.fixture(scope='function', autouse=True)
# def driver():
#     driver = webdriver.Remote(
#         command_executor='http://localhost:4444/wd/hub',
#         options=options
#     )
#     driver.maximize_window()
#     yield driver
#     driver.quit()




"""
docker run -d --name selenium_chrome -p 4444:4444 -p 5900:5900 selenium/standalone-chrome-debug
docker rm selenium_chrome
docker stop selenium_chrome
docker rm --force selenium_chrome
"""
