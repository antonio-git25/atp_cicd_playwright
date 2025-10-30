from playwright.sync_api import sync_playwright, Page, expect
import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    def test_successfull_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
        registration_page.click_registration_button()
        #dashboard_page.check_visible_dashboard_title()
        dashboard_page.dashboard_toolbar_view.check_visible()



# python -m pytest -k "test_successfull_registration" -s -v