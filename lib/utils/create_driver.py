import pytest
from selenium.webdriver import Chrome,Firefox,Ie

def get_driver_instance():
    browser = pytest.config.option.browser.lower()
    url = pytest.config.option.server.lower()

    if browser == 'firefox':
        driver = Firefox("/browser_servers/geckodriver.exe")

    elif browser == 'chrome':
        driver = Chrome("/browser_servers/chromedriver.exe")

    elif browser == 'ie':
        driver = Ie("/browser_servers/IEDriverServer.exe")

    else:
        print('------Error---------------')
        print('!!!----Invalid browser options------')

    driver.maximize_window()
    driver.implicitly_wait(30)
    if url == 'prod':
        driver.get("http://demo.actitime.com")
    else:
        driver.get('http://localhost')
    return driver

