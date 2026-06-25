from pages.login_page import LoginPage
from utils.logger import get_logger


logger = get_logger()


def test_invalid_login(page):
    logger.info("Starting Invalid Login Test")

    login = LoginPage(page)

    login.open()
    logger.info("Attempting login with invalid credentials")

    login.login(
        "WrongUser",
        "WrongPassword"  )
    actual_error = login.get_error_message()

    logger.info(f"Error message received: {actual_error}")

    assert ( actual_error   == "Invalid credentials" )
