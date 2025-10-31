import pytest
import allure

from tools.allure_tags import AllureTag
from tools.allure_epics import AllureEpic
from tools.allure_features import AllureFeature
from tools.allure_stories import AllureStory

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGISTRATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.title('Registration with correct email, username and password')
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
        registration_page.click_registration_button()
        #dashboard_page.check_visible_dashboard_title()
        dashboard_page.dashboard_toolbar_view.check_visible()



# python -m pytest -k "test_successfull_registration" -s -v