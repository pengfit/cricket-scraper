from playwright.sync_api import sync_playwright

def test_example(page):
    page.goto("https://playwright.dev/")
    assert "Playwright" in page.title()