from playwright.sync_api import sync_playwright

def test_example(page):
    page.goto("https://zjj.xa.gov.cn/")
    assert "西安" in page.title()