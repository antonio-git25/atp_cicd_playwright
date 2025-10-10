from playwright.sync_api import sync_playwright, expect


with (sync_playwright() as playwright):
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registr_button = page.get_by_test_id('registration-page-registration-button')
    expect(registr_button).to_be_disabled()

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    registr_button = page.get_by_test_id('registration-page-registration-button')
    expect(registr_button).not_to_be_disabled()


    page.wait_for_timeout(3500)