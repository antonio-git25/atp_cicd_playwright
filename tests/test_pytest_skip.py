import pytest

@pytest.mark.skip(reason="feature in development")
def test_feature_1():
    pass


@pytest.mark.skip(reason="feature in development 2")
class TestSuiteSkip:
    def test_feature_in_dev1(self):
        pass

    def test_feature_in_dev2(self):
        pass

