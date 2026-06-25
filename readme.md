# OrangeHRM UI Automation Framework

## Project Overview

This project implements a reusable UI automation framework for the OrangeHRM demo application using **Playwright**, **Pytest**, and **Python**.

The framework follows the **Page Object Model (POM)** design pattern and includes:

* Login automation
* Positive and negative test scenarios
* Reusable page classes
* HTML reporting
* Logging support
* GitHub Actions CI/CD integration

Application Under Test:

https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

---

## Project Structure

```text
orangehrm-ui-automation/

├── .github/
│   └── workflows/
│       └── ui-tests.yml

├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── admin_page.py

├── tests/
│   ├── login/
│   │   ├── test_valid_login.py
│   │   └── test_invalid_login.py
│   │
│   └── admin/
│       └── test_search_user.py

├── utils/
│   ├── config.py
│   └── logger.py

├── reports/

├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Framework Design

The framework uses the Page Object Model (POM) pattern.

### Base Page

Contains reusable methods:

* click()
* fill()
* get_text()

### Page Classes

Each page contains its own locators and actions:

* LoginPage
* DashboardPage
* AdminPage

This improves:

* Reusability
* Maintainability
* Readability

---

## Test Scenarios Implemented

### 1. Valid Login

Steps:

1. Open OrangeHRM application
2. Enter valid credentials
3. Click Login
4. Verify Dashboard page is displayed

Expected Result:

User is successfully logged in.

---

### 2. Invalid Login

Steps:

1. Open OrangeHRM application
2. Enter invalid credentials
3. Click Login
4. Verify error message

Expected Result:

"Invalid credentials" message is displayed.

---

### 3. Admin User Search (Optional)

Steps:

1. Login successfully
2. Navigate to Admin module
3. Search for a user
4. Verify search results

Note:

The OrangeHRM demo environment is public and data may change over time, so this test is considered optional.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd orangehrm-ui-automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install chromium
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/login/test_valid_login.py
```

Run tests with verbose output:

```bash
pytest -v
```

---

## Reporting

The framework uses pytest-html to generate execution reports.

Generated report:

```text
reports/report.html
```

Open the HTML file in a browser to view:

* Passed tests
* Failed tests
* Execution time
* Environment information

---

## Logging

Basic logging support is implemented using Python's logging module.

Logs can be extended to capture:

* Test execution steps
* Errors
* Debug information

---

## Error Handling

Error handling is implemented through:

* Assertions with meaningful validations
* Exception propagation
* Optional screenshot capture on failures

This ensures easier debugging and maintenance.

---

## CI/CD Integration

GitHub Actions is configured to execute UI tests automatically.

The pipeline performs the following steps:

1. Checkout repository
2. Setup Python environment
3. Install dependencies
4. Install Playwright browsers
5. Execute UI tests
6. Generate HTML reports
7. Upload reports as workflow artifacts

The workflow is triggered on:

* Push to main branch
* Pull Requests to main branch

---

## Technologies Used

* Python 3.13
* Playwright
* Pytest
* Pytest HTML Reporter
* GitHub Actions
* Page Object Model (POM)

---

## Future Improvements

Possible enhancements include:

* Parallel execution using Pytest XDist
* Allure reporting integration
* Data-driven testing
* Cross-browser execution
* Automatic screenshot capture on failures
* Environment-based configuration
