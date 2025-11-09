import pytest
from playwright.sync_api import Playwright, Page
from _pytest.fixtures import SubRequest

import allure
from allure_commons.types import AttachmentType
from pydantic_config import settings
from tools.mocks import mock_static_resources

from pages.registration_page import RegistrationPage


@pytest.fixture(params=settings.browsers)
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    #browser = playwright.chromium.launch(headless=settings.headless, slow_mo=600)
    browser_type = request.param
    browser = playwright[browser_type].launch(headless=settings.headless, slow_mo=600)
    if settings.video_record == True:
        context = browser.new_context(
            base_url=settings.get_base_url(),  # Необходимо добавить settings.get_base_url()
            record_video_dir=settings.videos_dir
        )
    else:
        context = browser.new_context(base_url=settings.get_base_url())

    if settings.tracing_record == True:
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    mock_static_resources(page)

    yield page

    #context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    if settings.tracing_record == True:
        context.tracing.stop(path=settings.tracing_dir.joinpath(f'{request.node.name}.zip'))
        allure.attach.file(settings.tracing_dir.joinpath(f'{request.node.name}.zip'), name='trace', extension='zip')

    browser.close()

    if settings.video_record == True:
        allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)



@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    #registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.visit("./#/auth/registration")
    registration_page.registration_form.fill(
        email=settings.test_user.email,
        username=settings.test_user.username,
        password=settings.test_user.password
    )
    registration_page.click_registration_button()

    context.storage_state(path=settings.browser_state_file)
    browser.close()


@pytest.fixture(params=settings.browsers)
#def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
def chromium_page_with_state(request: SubRequest, playwright: Playwright) -> Page:
    browser_type = request.param
    browser = playwright[browser_type].launch(headless=settings.headless, slow_mo=800)
    if settings.video_record == True:
        context = browser.new_context(
            base_url=settings.get_base_url(),  # Необходимо добавить settings.get_base_url()
            storage_state=settings.browser_state_file,
            record_video_dir=settings.videos_dir
        )
    else:
        context = browser.new_context(
            base_url=settings.get_base_url(),
            storage_state=settings.browser_state_file
        )

    if settings.tracing_record == True:
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    mock_static_resources(page)

    yield page

    if settings.tracing_record == True:
        context.tracing.stop(path=settings.tracing_dir.joinpath(f'{request.node.name}.zip'))
        allure.attach.file(settings.tracing_dir.joinpath(f'{request.node.name}.zip'), name='trace', extension='zip')

    browser.close()

    if settings.video_record == True:
        allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)




# python -m pytest -m "regression" --alluredir=./allure-results
# allure serve ./allure-results