import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    page_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(page_title).to_have_text("Courses")

    page_message = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(page_message).to_have_text("There is no results")

    chromium_page_with_state.wait_for_timeout(5000)
