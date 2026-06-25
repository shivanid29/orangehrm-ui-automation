from pages.base_page import BasePage


class AdminPage(BasePage):

    ADMIN_MENU = "//span[text()='Admin']"

    # SEARCH_USERNAME = ("//label[text()='Username']/../following-sibling::div/input")

    SEARCH_USERNAME= "(// input[contains( @class ,'oxd-input')])[2]"
    SEARCH_BUTTON = "//button[@type='submit']"

    # RESULT_CELL = ("//div[@role='cell'][contains(.,'Admin')]")

    RESULT_ROWS = ".oxd-table-card"

    def open_admin(self):
        self.click( self.ADMIN_MENU)


    def search_user(self, username):

        self.fill(self.SEARCH_USERNAME,username)

        self.click(self.SEARCH_BUTTON)

        self.page.locator(self.RESULT_ROWS).first.wait_for(state="visible")

    def search_result_exists(self):
        rows = self.page.locator(self.RESULT_ROWS )

        print(f"Rows found: {rows.count()}")

        return rows.count() > 0