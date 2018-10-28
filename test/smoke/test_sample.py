import unittest
from lib.ui.login_page import Loginpage
from lib.utils import create_driver

class TestSample(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver.get_driver_instance()
        self.login =  Loginpage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_sample(self):
        self.login.wait_for_login_page_to_load()
        actual_title = self.driver.title
        expected_title = 'actTIME-Login'
        assert actual_title == expected_title
