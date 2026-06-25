from pages.login_page import LoginPage
from pages.admin_page import AdminPage

from utils.config import USERNAME,PASSWORD


def test_search_existing_user(page):

    login = LoginPage(page)
    admin = AdminPage(page)

    login.open()
    login.login(USERNAME, PASSWORD)

    admin.open_admin()
    admin.search_user("Admin")

    assert admin.search_result_exists()