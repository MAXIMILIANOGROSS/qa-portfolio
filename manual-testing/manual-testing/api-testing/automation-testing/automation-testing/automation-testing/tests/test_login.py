import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestLogin:
    """Test cases for Login functionality"""
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Setup and teardown for each test"""
        # Setup
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        
        yield
        
        # Teardown
        self.driver.quit()
    
    def test_valid_login(self):
        """TC-A001: Login with valid credentials"""
        # Arrange
        username = "student"
        password = "Password123"
        
        # Act
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "submit")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        
        # Assert
        wait = WebDriverWait(self.driver, 10)
        success_message = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "post-title"))
        )
        assert "Congratulations" in success_message.text
    
    def test_invalid_password(self):
        """TC-A002: Login with invalid password"""
        # Arrange
        username = "student"
        password = "WrongPassword"
        
        # Act
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "submit")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        
        # Assert
        wait = WebDriverWait(self.driver, 10)
        error_message = wait.until(
            EC.presence_of_element_located((By.ID, "error"))
        )
        assert "invalid" in error_message.text.lower()
    
    def test_empty_username(self):
        """TC-A003: Login with empty username"""
        # Arrange
        password = "Password123"
        
        # Act
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "submit")
        
        password_field.send_keys(password)
        login_button.click()
        
        # Assert
        error_message = self.driver.find_element(By.ID, "error")
        assert error_message.is_displayed()
        assert "username" in error_message.text.lower()
    
    def test_empty_password(self):
        """TC-A004: Login with empty password"""
        # Arrange
        username = "student"
        
        # Act
        username_field = self.driver.find_element(By.ID, "username")
        login_button = self.driver.find_element(By.ID, "submit")
        
        username_field.send_keys(username)
        login_button.click()
        
        # Assert
        error_message = self.driver.find_element(By.ID, "error")
        assert error_message.is_displayed()
        assert "password" in error_message.text.lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
