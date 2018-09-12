#from django.test import TestCase ,    this is another abroch
import unittest
from selenium import webdriver


#class pollTestCase(TestCase): this is another abroch
class pollsFunctionalTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	def tearDown(self):
		self.browser.quit()

	def test_home_page_is_about_polls(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('poll', self.browser.title)

if __name__ == '__main__':
	unittest.main()



