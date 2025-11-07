import pytest
import allure

from tools.allure_tags import AllureTag
from tools.allure_epics import AllureEpic
from tools.allure_features import AllureFeature
from tools.allure_stories import AllureStory
from tools.routes import AppRoute
from allure_commons.types import Severity
from pydantic_config import settings

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGISTRATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @pytest.mark.xdist_group(name="authorization-group")  # Добавили xdist группу
    @allure.title('Registration with correct email, username and password')
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.click_registration_button()
        #dashboard_page.check_visible_dashboard_title()
        dashboard_page.dashboard_toolbar_view.check_visible()



# python -m pytest -k "test_successfull_registration" -s -v