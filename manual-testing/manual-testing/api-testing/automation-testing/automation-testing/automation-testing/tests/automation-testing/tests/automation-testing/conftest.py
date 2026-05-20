import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def browser():
    """Create and close browser for each session"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def setup_teardown():
    """Setup and teardown for each test"""
    print("\n--- Starting Test ---")
    yield
    print("\n--- Test Completed ---")
