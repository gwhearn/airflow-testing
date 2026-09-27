import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = os.getenv("AIRFLOW_BASE_URL")
USERNAME = os.getenv("AIRFLOW_USERNAME")
PASSWORD = os.getenv("AIRFLOW_PASSWORD")
SELENIUM_URL = os.getenv("SELENIUM_URL")

def test_login_and_see_dags():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Remote(
        command_executor=SELENIUM_URL,
        options=options
    )

    try:
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 30)

        # Wait for username field
        username_field = wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "input[name='username'], input#username, input[type='text'], input[autocomplete='username']"
            ))
        )
        password_field = wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "input[name='password'], input#password, input[type='password']"
            ))
        )

        username_field.clear()
        username_field.send_keys(USERNAME)
        password_field.clear()
        password_field.send_keys(PASSWORD)

        # Most reliable way: press Enter on the password field
        password_field.send_keys(Keys.RETURN)

        # Wait until we are no longer on the login page
        wait.until(
            lambda d: "login" not in d.current_url.lower() or "dags" in d.page_source.lower()
        )

        page_source = driver.page_source.lower()
        assert "dags" in page_source or "dag" in page_source
        print("\nSuccessfully logged in and reached the DAGs page!")

    finally:
        driver.quit()
