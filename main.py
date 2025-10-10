from playwright.sync_api import sync_playwright, expect
import time


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, devtools=True)
    context = browser.new_context()
    context.add_cookies([{'name': 'hello', 'value': 'world', 'domain': 'www.google.com', 'path': '/'}])
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    page.wait_for_timeout(100000)



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    #System waits while we enter log/pass by manually
    #Email: user.name@gmail.com
    #User: username
    #Pass: password
    time.sleep(25)

    welcome_head = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(welcome_head).to_have_text("Dashboard")

    dash_tab = page.get_by_test_id('dashboard-drawer-list-item-title-text')
    curse_tab = page.get_by_test_id('courses-drawer-list-item-title-text')

    page.wait_for_timeout(1500)
    curse_tab.click()

    curse_head = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(curse_head).to_have_text("Courses")

    context.storage_state(path="browser-state.json")
    page.wait_for_timeout(3000)

