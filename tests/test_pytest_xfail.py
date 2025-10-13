import pytest

@pytest.mark.xfail(reason="fail known issue: ")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail
def test_without_bug():
    pass