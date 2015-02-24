from django.core.management.base import NoArgsCommand
from selenium import webdriver
import urllib
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from store.inventory.models import *
class Command(NoArgsCommand):
	help = 'Update Last Connected time of printer'

	def handle_noargs(self, **options):
		driver = webdriver.Firefox()
		driver.maximize_window()

		driver.get("http://www.daraz.pk/phones/nokia/")
		driver.get("http://www.daraz.pk/phones/nokia/")
		
		'''
		elem = wait_visible_xpath(driver, '/html/body/div[1]/div/div')
		for i in range(10):
			elem.send_keys(Keys.PAGE_DOWN)
		button = wait_visible_xpath(driver, '/html/body/div[1]/div/div/div[3]/div/div[2]/div/div/div')
		button.click()

		sleep(3)
		for i in range(30):
			elem.send_keys(Keys.PAGE_UP)
		'''
		
		category = Category.objects.get(name='Phones')
		
		for count in range(1,76):
			image = None
			price = None
			name = None
			image_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[1]'.format(str(count))
			image = wait_visible_xpath(driver, image_xpath)
	
			price_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[2]/span/span/span[2]'.format(str(count))
			name_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[2]/div/label[2]'.format(str(count))
			try:
				print 'try 1'
				price = wait_visible_xpath(driver, price_xpath)
				print 'PRICE:', price.text
				name = wait_visible_xpath(driver, name_xpath)
				print 'NAME:', name.text
			except:
				price_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[3]/span/span/span[2]'.format(str(count))
				name_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[3]/div/label[2]'.format(str(count))
				try:
					print 'try 2'
					price = wait_visible_xpath(driver, price_xpath)
					print 'PRICE:', price.text
					name = wait_visible_xpath(driver, name_xpath)
					print 'NAME:', name.text
				except:
					price_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[4]/span/span/span[2]'.format(str(count))
					name_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[4]/div/label[2]'.format(str(count))
					print price_xpath
					try:
						print 'try 3'
						price = wait_visible_xpath(driver, price_xpath)
						print 'PRICE:', price.text
						name = wait_visible_xpath(driver, name_xpath)
						print 'NAME:', name.text
					except:
						print 'PRICE NOT FOUND'	
			
			if image and price and name:
				price = int(price.text.replace(',',''))
				src = image.get_attribute('data-image')
				print 'SRC:', src

				urllib.urlretrieve(src, 'store/site_media/media/items/phone-nokia-{}.jpg'.format(str(count)))
				
				item = Item()
				item.category = category
				if len(name.text) > 50:
					item.name = name.text[:50]
				else:
					item.name = name.text
				item.price = price
				item.image = 'items/phone-nokia-{}.jpg'.format(str(count))
				item.save()
				item.tags.add("phone", "nokia")
				item.save()
				
		driver.quit()


def wait_visible_xpath(driver, xpath):
	return WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, xpath)))
