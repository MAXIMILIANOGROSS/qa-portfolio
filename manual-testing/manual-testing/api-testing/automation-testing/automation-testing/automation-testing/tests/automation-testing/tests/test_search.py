import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestSearch:
    """Test cases for Search functionality"""
    
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
        self.driver.get("https://practicetestautomation.com/")
        
        yield
        
        # Teardown
        self.driver.quit()
    
    def test_search_by_keyword(self):
        """TC-A005: Search products by keyword"""
        # Act
        search_box = self.driver.find_element(By.CLASS_NAME, "search-field")
        search_box.send_keys("Test")
        search_button = self.driver.find_element(By.CLASS_NAME, "search-submit")
        search_button.click()
        
        # Assert
        wait = WebDriverWait(self.driver, 10)
        results = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product"))
        )
        assert len(results) > 0
    
    def test_search_no_results(self):
        """TC-A006: Search with no results"""
        # Act
        search_box = self.driver.find_element(By.CLASS_NAME, "search-field")
        search_box.send_keys("ZZZZZZZZZ123456")
        search_button = self.driver.find_element(By.CLASS_NAME, "search-submit")
        search_button.click()
        
        # Assert
        wait = WebDriverWait(self.driver, 10)
        no_results = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "no-results"))
        )
        assert "not found" in no_results.text.lower()
    
    def test_search_empty_field(self):
        """TC-A007: Search with empty field"""
        # Act
        search_button = self.driver.find_element(By.CLASS_NAME, "search-submit")
        search_button.click()
        
        # Assert
        assert self.driver.current_url == "https://practicetestautomation.com/"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
