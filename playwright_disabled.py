from playwright.sync_api import sync_playwright, expect


with (sync_playwright() as playwright):
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_disabled() #-> .not_to_be_disabled()

    page.wait_for_timeout(3500)




#python -m playwright_disabled