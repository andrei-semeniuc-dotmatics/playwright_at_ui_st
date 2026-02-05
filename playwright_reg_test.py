from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.get_by_test_id("login-form-email-input").locator("input")
    expect(email_input).to_be_visible()

    password_input = page.get_by_test_id("login-form-password-input").locator("input")
    expect(password_input).to_be_visible()

    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_visible()

    registration_link = page.get_by_test_id('login-page-registration-link')
    expect(registration_link).to_be_visible()

    registration_link.click()

    reg_email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    expect(reg_email_input).to_be_visible()
    reg_email_input.fill('user.name@gmail.com')

    reg_username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    expect(reg_username_input).to_be_visible()
    reg_username_input.fill('username')

    reg_password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    expect(reg_password_input).to_be_visible()
    reg_password_input.fill('password')

    reg_button = page.get_by_test_id('registration-page-registration-button')
    expect(reg_button).to_be_visible()
    reg_button.click()

    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text("Dashboard")

    page.wait_for_timeout(2500)