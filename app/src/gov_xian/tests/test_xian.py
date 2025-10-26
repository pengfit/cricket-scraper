# test_xian.py
import pytest
from bs4 import BeautifulSoup
from app.src.utils.get_env import get_env_vars
from app.src.utils.logger_util import setup_logger
from app.src.utils.json_util import read_file, write_file

# Get environment variables
GOV_MODULE, MODULE_URL,REPORTS_DIR = get_env_vars()

# Set up logger
logger = setup_logger(log_file=f"{REPORTS_DIR}/running.log")

def issue_html(html: str) -> list:
    soup = BeautifulSoup(html, 'html.parser')
    result = []
    for li in soup.find_all('li'):
        name = li.get_text(strip=True)
        result.append({
            'name': name
        })
    return result


def test_module_url():
    logger.info("Testing module: %s", GOV_MODULE)
    logger.info("Module URL: %s", MODULE_URL)
    assert MODULE_URL.startswith("https://")
    logger.info("Module URL validation passed ✅")


def test_read_issue(page):
    page.goto(MODULE_URL,timeout = 60000)
    assert "西安" in page.title()
    page.wait_for_selector('#textGK').click()
    all_li = page.locator('#gklist').inner_html()
    issue = issue_html(all_li)
    write_file(f"{REPORTS_DIR}/issue.json", issue)



def test_read_pages(page):
    page.goto(MODULE_URL,timeout = 60000)
    assert "西安" in page.title()
    areas_list = read_file(f"{REPORTS_DIR}/areas.json")
    for area in areas_list:
        file_name = f"{REPORTS_DIR}/issue.json"
        issues = read_file(file_name)
        for issue in issues:
            logger.info("县区: %s 日期: %s",area,issue)
            browser_pages(page,area,issue)






def browser_pages(page,area,issue):
    #区域
    page.select_option('#ddl_qdm', area['value'])
    #日期
    page.wait_for_selector('#textGK').click()
    page.locator("ul#gklist li", has_text=f"{issue['name']}").click()
    page.wait_for_selector('.ygsf_searchbox input[value="搜索"]').click()
    while True:
        result = []
        rows = page.locator("table tbody tr").all()
        # Skip the first row (header), and parse the rest
        for row in rows[2:]:
            cells = row.locator("td").all_inner_texts()
            result.append(cells)
        logger.info("%s",row)
        pre_next = page.locator('#rptPager .prenext').last
        break
    return

