from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

from utils.config import Config
from utils.logger import get_logger


logger = get_logger()


def test_valid_login(page):
    logger.info("Starting Valid Login Test")

    login = LoginPage(page)

    dashboard = DashboardPage(page)

    logger.info("Application Opened")

    login.login(Config.USERNAME, Config.PASSWORD)
    logger.info("User Logged In")

    assert (dashboard.is_dashboard_loaded())
    logger.info("Dashboard Loaded Successfully")