import allure

@allure.step("Opening browser")
def open_browser():
    with allure.step("get brow"):
        pass

    with allure.step("start browser"):
        pass

@allure.step("Creating course")
def create_course(title: str):
    with allure.step(f"create course with title: {title}"):
        pass

@allure.step("Closing browser {name}")
def close_browser(name: str):
    pass


def test_feature_1():
    open_browser()
    create_course(title="locust")
    create_course(title="silk")
    close_browser(name="gekor")
    close_browser(name="firefox")
