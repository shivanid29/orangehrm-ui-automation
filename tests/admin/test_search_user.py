from pages.login_page import LoginPage
from pages.admin_page import AdminPage

from utils.config import Config


def test_search_existing_user(page):

    login = LoginPage(page)
    admin = AdminPage(page)

    login.login(Config.USERNAME, Config.PASSWORD)

    admin.open_admin()
    admin.search_user("Admin")

    assert admin.search_result_exists()