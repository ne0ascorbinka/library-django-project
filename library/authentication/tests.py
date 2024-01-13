from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .models import CustomUser

# SERVER_LINK = 'http://127.0.0.1:8000/'
DRIVER_PATH = "D:\\downloads\\geckodriver-v0.34.0-win64\\geckodriver.exe"

VALID_EMAIL = "email@test.com"
VALID_PASSWORD = "1234"
INVALID_EMAIL = "totally@invalid.com"
INVALID_PASSWORD = "wrooong"

class TestAuth(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        driver = webdriver.Firefox()
        cls.driver = driver
        return super().setUpClass()
    
    def setUp(self) -> None:
        CustomUser.create(VALID_EMAIL, VALID_PASSWORD)
        self.driver.get(self.live_server_url)
    
    def click_login(self) -> None:
        elem = self.driver.find_element(By.LINK_TEXT, "Login")
        elem.click()
    
    def login(self, email, passwd) -> None:
        driver = self.driver
        email_input = driver.find_element(By.NAME, "email")
        passwd_input = driver.find_element(By.NAME, "password")
        email_input.send_keys(email)
        passwd_input.send_keys(passwd)
        driver.find_element(By.XPATH, "//form").submit()

    def test_login_valid(self):
        self.click_login()
        self.login(VALID_EMAIL, VALID_PASSWORD)
        time.sleep(2)
        
        elem = self.driver.find_element(By.CLASS_NAME, "user_email")
        self.assertEqual(elem.text, VALID_EMAIL)
    
    def test_logout(self):
        self.click_login()
        self.login(VALID_EMAIL, VALID_PASSWORD)
        time.sleep(3)

        elem = self.driver.find_element(By.LINK_TEXT, "Logout")
        elem.click()
        time.sleep(3)

        elem = self.driver.find_element(By.CLASS_NAME, "user_email")
        self.assertEqual(elem.text, '')
    
    def test_login_invalid(self): 
        self.click_login()
        self.login(INVALID_EMAIL, INVALID_PASSWORD)
        time.sleep(2)
        elem = self.driver.find_element(By.XPATH, '//form')
        self.assertIn("Wrong credentials, try again.", elem.text)
    
    @classmethod
    def tearDownClass(cls) -> None:
        driver = cls.driver
        driver.close()
        return super().tearDownClass()