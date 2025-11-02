from playwright.sync_api import Page, expect
from typing import Pattern
import allure


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):  # Метод для открытия ссылок
        with allure.step(f'Opening the url: {url}'):
            self.page.goto(url, wait_until='networkidle')

    def reload(self):  # Метод для перезагрузки страницы
        with allure.step(f'Reloading page with: {self.page.url}'):
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking that current url matches with pattern: {expected_url.pattern}'):
            expect(self.page).to_have_url(expected_url)