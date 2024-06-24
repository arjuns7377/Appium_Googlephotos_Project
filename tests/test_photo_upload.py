import unittest
from appium import webdriver
from pages.google_photos_page import GooglePhotosPage
from pages.gmail_page import GmailPage
import base64

class PhotoUploadTest(unittest.TestCase):
		 def setUp(self):
			 desired_cap = {
						      'platformName': 'Android',
							  'deviceName': 'emulator-5554',
						      'appPackage': 'com.google.android.apps.photos',
						      'appActivity': 'com.google.android.apps.photos.home.HomeActivity',
							   'app': '/mnt/c/Users/91952/Downloads/gphoto.apk',
						      'noReset': 'true'
					      }
			 self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
		     self.google_photos = GooglePhotosPage(self.driver)
		     self.gmail = GmailPage(self.driver)

		def test_upload_photo(self):
		    local_image = "local_image.png"
		    local_image_path = "/mnt/c/Users/Arjun/Downloads/def/" + local_image
		    device_image_path = '/storage/emulated/0/Pictures/local_image.png'

	     # Push image from local machine to emulator
		    self.google_photos.push_file_to_device(device_image_path, local_image_path)

	    # Open Google Photos
	       self.google_photos.open_library_tab()
	       self.google_photos.implicitly_wait(30)

	       self.google_photos.open_album()
	       self.google_photos.implicitly_wait(30)

	      self.google_photos.open_photo()
	      self.google_photos.implicitly_wait(30)

																																								        # Change orientation
																																										        self.google_photos.set_orientation("LANDSCAPE")
																																										        self.google_photos.implicitly_wait(30)

																																										        self.google_photos.set_orientation("PORTRAIT")
																																										        self.google_photos.implicitly_wait(30)

																																										        self.google_photos.open_overflow_menu()
																																										        self.google_photos.implicitly_wait(100)

																																								        # Assertion
																																									        assert self.google_photos.compare_images(device_image_path, local_image)

																																								        # Open Gmail and send email
																																									        self.gmail.start_activity('com.google.android.gm', 'com.google.android.gm.ConversationListActivityGmail')
																																									        self.gmail.compose_email("arjunspanicker4@gmail.com")
																																									        self.gmail.attach_photo()
																																									        self.gmail.send_email()

																																										    def tearDown(self):
																																										        self.driver.quit()

			  																																							if __name__ == "__main__":
																																										    unittest.main()

