import pytest

SYSTEM_VERSION = "v1.3.0"

@pytest.mark.skipif(SYSTEM_VERSION == "v1.3.0", reason="test can not be executed in v1.3.0")
def test_system_version_valid():
    pass

@pytest.mark.skipif(SYSTEM_VERSION == "v1.2.0", reason="test can not be executed in v1.2.0")
def test_system_version_invalid():
    pass


