import pytest
import random

PLATFORM = "Linux"

#need import additional pytest plugin: pip install pytest-rerunfailures
@pytest.mark.flaky(reruns=4, reruns_delay=2)
def test_reruns():
    assert random.choice([True,False,False])


@pytest.mark.flaky(reruns=4, reruns_delay=2)
class TestReruns:
    def test_rerun_1(self):
        assert random.choice([True, False, False])

    def test_rerun_2(self):
        assert random.choice([True, False, False])


@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == "Windows")
def test_rerun_with_condition():
    assert random.choice([True, False, False])