from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        # page = browser.new_page()
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        email_input.fill("username@gmail.com")

        username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        username_input.fill("username")

        password_input = page.get_by_test_id("registration-form-password-input").locator("input")
        password_input.fill("password")

        registration_button = page.get_by_test_id("registration-page-registration-button")
        registration_button.click()

        context = context.storage_state(path="browser-state_course.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state_course.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        page_title = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(page_title).to_have_text("Courses")

        page_message = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(page_message).to_have_text("There is no results")

        page.wait_for_timeout(5000)