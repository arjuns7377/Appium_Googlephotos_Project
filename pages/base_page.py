
import appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
		  def __init__(self, driver):
		  self.driver = driver

		  def find_element(self, locator, timeout=10):
			  return WebDriverWait(self.driver, timeout).until( EC.presence_of_element_located(locator))

          def click(self, locator, timeout=10):
		     self.find_element(locator, timeout).click()

	      def send_keys(self, locator, text, timeout=10):
		     self.find_element(locator, timeout).send_keys(text)

		 def set_orientation(self, orientation):
			 self.driver.orientation = orientation

	     def start_activity(self, app_package, app_activity):
	         self.driver.start_activity(app_package, app_activity)

	     def push_file_to_device(self, device_path, local_file_path):
		     with open(local_file_path, "rb") as file:
    																																							            file_data = file.read()
 																																								            encoded_file_data = base64.b64encode(file_data).decode('utf-8')
																																								            self.driver.push_file(device_path, encoded_file_data)

																																										    def implicitly_wait(self, time_to_wait):
	    																																								        self.driver.implicitly_wait(time_to_wait)
																																												
																																										   def compare_images(self, full_path, local_image_file_name):
																																										       return full_path.split("/")[-1] == local_image_file_name

