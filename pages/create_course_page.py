from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from components.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.create_course_form_component import CreateCourseFormComponent
from components.image_upload_widget_component import ImageUploadWidgetComponent
from components.navbar_component import NavbarComponent
from components.empty_view_component import EmptyViewComponent


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.create_course_form = CreateCourseFormComponent(page)
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.create_course_exercise_form = CreateCourseExerciseFormComponent(page)
        self.create_course_toolbar_view = CreateCourseToolbarViewComponent(page)
        self.create_course_exercises_toolbar_view = CreateCourseExercisesToolbarViewComponent(page)


    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )

