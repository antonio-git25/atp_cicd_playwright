import pytest
import allure

from tools.allure_tags import AllureTag
from tools.allure_epics import AllureEpic
from tools.allure_features import AllureFeature
from tools.allure_stories import AllureStory
from allure_commons.types import Severity

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.AUTHENTICATION) # Добавили feature
@allure.story(AllureStory.AUTHORIZATION) # Добавили story
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorisation:
    @allure.title('User login with correct email and password')
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(
            self,
            registration_page: RegistrationPage,
            dashboard_page: DashboardPage,
            login_page: LoginPage
    ):
        # Переход на страницу регистрации
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        # Заполнение формы регистрации и нажатие кнопки "Registration"
        registration_page.registration_form.fill(email="user.name@gmail.com", username="username", password="password")
        registration_page.click_registration_button()

        # Проверка видимости элементов Dashboard
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()

        dashboard_page.sidebar.click_logout()

        # Переход на страницу авторизации и авторизация
        login_page.login_form.fill(email="user.name@gmail.com", password="password")
        login_page.click_login_button()

        # Проверка элементов Dashboard после входа
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()



    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password")
        ]
    )
    @allure.title('User login with wrong email or password')
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_auth(self, login_page: LoginPage, email: str, password: str):
        #allure.dynamic.title(f'User login with wrong email or password: {email}')
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()


    @allure.title('Navigation from login page to registration page')
    @allure.tag(AllureTag.NAVIGATION)
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email="", username="", password="")


# python -m pytest -k "test_wrong_email_auth" -s -v
# python -m pytest -k "regression" --alluredir=./allure-results