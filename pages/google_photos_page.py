
import base_page import BasePage
from selenium.webdriver.common.by import By

class GooglePhotosPage(BasePage):
	  TAB_LIBRARY = (By.ID, 'com.google.android.apps.photos:id/tab_library')
	  ALBUM_COVER_TITLE = (By.ID, 'com.google.android.apps.photos:id/album_cover_title')
	  PHOTO_ACCESSIBILITY_ID = (By.ACCESSIBILITY_ID, 'Photo taken on Jan 30, 2023 12:17:32 PM')
	  PHOTOS_OVERFLOW_ICON = (By.ID, 'com.google.android.apps.photos:id/photos_overflow_icon')

	  def open_library_tab(self):
		 self.click(self.TAB_LIBRARY)

	  def open_album(self):
		  self.click(self.ALBUM_COVER_TITLE)

     def open_photo(self):
		  self.click(self.PHOTO_ACCESSIBILITY_ID)

	 def open_overflow_menu(self):
	     self.click(self.PHOTOS_OVERFLOW_ICON)

