from playwright.sync_api import Page, expect
from typing import Pattern
import allure
from tools.logger import  get_logger

logger = get_logger("BASE_PAGE")

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        step =f'Opening the url: {url}' # Метод для открытия ссылок
        with allure.step(f'Opening the url: {url}'):
            logger.info(step)
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        step = f'Reloading page with: {self.page.url}' # Метод для перезагрузки страницы
        with allure.step(f'Reloading page with: {self.page.url}'):
            logger.info(step)
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that current url matches with pattern: {expected_url.pattern}'
        with allure.step(f'Checking that current url matches with pattern: {expected_url.pattern}'):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)