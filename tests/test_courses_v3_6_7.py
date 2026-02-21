from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.auth
@pytest.mark.parametrize("email", ["user.name@gmail.com", "user.name@gmail.com", "  "])
@pytest.mark.parametrize("password", ["password", "  ", "password"])
def test_wrong_emaill_or_password_auth(chromium_page: Page, email: str, password: str):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = chromium_page.get_by_test_id("login-form-email-input").locator("input")
    email_input.fill("user.name@gmail.com")

    password_input = chromium_page.get_by_test_id("login-form-password-input").locator("//div//input")
    password_input.fill("P@ssw0rd!")

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = chromium_page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

    chromium_page.wait_for_timeout(2500)
    # browser.close()
