import pytest

SYSTEM_VERSION = "v1.2.0"

@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0", # SYSTEM_VERSION = "v1.2.0" => FALSE
    reason="Test can not be run on version v1.3.0"
)
def test_system_version_valid():
    pass

@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0", # # SYSTEM_VERSION = "v1.2.0" => TRUE
    reason="Test can not be run on version v1.2.0"
)
def test_system_version_invalid():
    pass
