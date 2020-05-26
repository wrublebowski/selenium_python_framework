'''
In conftest we describe all fixtures (class and method setUp)
'''

import pytest
from pages.home.login_page import LoginPage # dodane na końcu
from base.webdriverfactory import WebDriverFactory
from pages.courses.register_courses_page import RegisterCoursesPage

@pytest.fixture()
def setUp():
    print('setUp before method')
    yield
    print('tearDown after method')

@pytest.fixture(scope='class')
def oneTimeSetUp(request, browser):
    print('One time setUp')

    # use WebDriverFactory class instance with argument (browser) from request
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    baseURL = 'https://letskodeit.teachable.com/'
    driver.get(baseURL)

    lp = LoginPage(driver)
    lp.login('test@email.com', 'abcabc')


    # add driver atribute to the test class using request keyword
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print('One time tearDown')

# set addoption fixture to fixture from above
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")