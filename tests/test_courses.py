from operator import index
import pytest
import allure

from tools.allure_tags import AllureTag
from tools.allure_epics import AllureEpic
from tools.allure_features import AllureFeature
from tools.allure_stories import AllureStory

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
@allure.tag(AllureTag.REGISTRATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
class TestCourses:
    @allure.title('Create course')
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_toolbar_view.check_visible()

        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="", estimated_time="", description="", max_score="0", min_score="0"
        )

        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image("./testdata/RW_4.jpg")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )

        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()

        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        )


    @allure.title('Check displaying of empty courses list')
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page.navbar.check_visible("username")
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()


    @allure.title('Edit course')
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.image_upload_widget.upload_preview_image("./testdata/RW_4.jpg")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright-2",
            estimated_time="3 weeks",
            description="Playwright-2",
            max_score="200",
            min_score="15"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright-2",
            estimated_time="3 weeks",
            max_score="200",
            min_score="15"
        )

        #steps for edit
        courses_list_page.course_view.menu.click_edit(index=0)

        create_course_page.create_course_form.fill(
            title="Playwright-3",
            estimated_time="4 weeks",
            description="Playwright-3",
            max_score="300",
            min_score="45"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        #step for check edited
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright-3",
            estimated_time="4 weeks",
            max_score="300",
            min_score="45"
        )



# python -m pytest -k "test_create_course" -s -v
# python -m pytest -k "test_empty_courses_list" -s -v