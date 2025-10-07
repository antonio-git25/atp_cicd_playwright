from playwright.sync_api import sync_playwright

#viewport={"width": 375, "height": 667}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    #browser = p.webkit.launch(headless=False)
    context = browser.new_context(viewport={"width": 1170, "height": 2532}, is_mobile=True, user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)')
    page = context.new_page()
    page.goto('https://mail.yandex.ru')
    #assert page.title() == 'Example Domain'
    page.wait_for_timeout(4000)