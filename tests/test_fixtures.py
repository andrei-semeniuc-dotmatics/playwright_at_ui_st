import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Sending data to the Analytics service")

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Initialize settings for autotests")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Create userdata one time per each class")

@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] Launch browser per each autotest")

class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        pass

    def test_user_can_create_course(self, settings, user, browser):
        pass

class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        pass
