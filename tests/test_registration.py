from playwright.sync_api import sync_playwright, Page, expect
import pytest

@pytest.mark.regression
@pytest.mark.registration
def test_successfull_registration(chromium_page: Page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    welcome_head = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(welcome_head).to_be_visible()
    expect(welcome_head).to_have_text("Dashboard")