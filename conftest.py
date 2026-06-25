import pytest
from playwright.sync_api import sync_playwright
from utils import testdat_json_reader

data = testdat_json_reader.return_url()

# 1. Register the custom command-line flag
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against: dev, staging, prod"
    )


# 2. Fixture to capture the environment string
@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env").lower()


# 3. Fixture to map the environment to a specific Base URL
@pytest.fixture(scope="session")
def base_url(env):
    urls = data['urls']
    # Fallback to dev if an invalid environment is passed
    return urls.get(env, urls["dev"])


# 4. Your updated page fixture
@pytest.fixture
def page(base_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Automatically navigate to the environment's base URL
        page.goto(base_url)

        yield page
        browser.close()