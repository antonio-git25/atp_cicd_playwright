import pytest
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorisation:
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
    def test_wrong_email_auth(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()


    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email="", username="", password="")


# python -m pytest -k "test_wrong_email_auth" -s -v