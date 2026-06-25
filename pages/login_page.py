from pages.base_page import BasePage
from utils.config import BASE_URL
from utils.logger import get_logger


logger = get_logger()


class LoginPage(BasePage):

    USERNAME_INPUT = 'input[name="username"]'
    PASSWORD_INPUT = 'input[name="password"]'
    LOGIN_BUTTON = 'button[type="submit"]'
    ERROR_MESSAGE = ".oxd-alert-content-text"

    def open(self):
        logger.info("Opening OrangeHRM")
        self.page.goto(BASE_URL)

    def login(self, username, password):
        try:
            self.fill( self.USERNAME_INPUT, username )

            self.fill(self.PASSWORD_INPUT,  password)

            self.click(self.LOGIN_BUTTON)

        except Exception as e:
            print(f"Login failed: {e}")
            raise

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)