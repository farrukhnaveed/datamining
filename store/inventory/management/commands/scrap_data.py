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
	help = 'Scrap Items'

	def handle_noargs(self, **options):
		driver = webdriver.Firefox()
		driver.maximize_window()

		#driver.get("http://www.daraz.pk/selfie-sticks/")
		driver.get("http://www.kaymu.pk/chargers-batteries-adapters/samsung/")
		category = Category.objects.get(name='Phone Accessories')
		tag = 'samsung'
		for count in [1,2,3,4,5,6,7,13,21]:
			image_xpath = '/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[6]/section/div/div[{}]/div/a/div/div[1]/span'.format(str(count))
			name_xpath = '/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[6]/section/div/div[{}]/div/a/div/div[2]/span'.format(str(count))
			price_xpath = '/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[6]/section/div/div[{}]/div/a/div/div[2]/div/span'.format(str(count))
			
			price = wait_visible_xpath(driver, price_xpath)
			price = int(price.text[3:].replace(',',''))

			name = wait_visible_xpath(driver, name_xpath)

			print name

			image = wait_visible_xpath(driver, image_xpath)
			src = image.get_attribute('data-image')

			print '\nCOUNT:', count
			print 'NAME:', name.text
			print 'PRICE:', price
			print 'IMAGE:', src
			
			# store/site_media/media/items/phone-accessories-bluetooth-{}-{}.jpg
			if image and price and name:
				# status = urllib.urlretrieve(src, 'store/site_media/media/items/phone-accessories-bluetooth-{}-{}.jpg'.format(tag.lower(), str(count)))

				item = Item()
				item.category = category
				if len(name.text) > 50:
					item.name = name.text[:50]
				else:
					item.name = name.text
				item.price = price
				item.image = 'items/phone-accessories-charger-{}-{}.jpg'.format(tag.lower(), str(count))
				item.save()
				item.tags.add("phone accessories", "chargers", tag.lower())
				item.save()






		'''
		driver.get("http://www.daraz.pk/selfie-sticks/")
		driver.get("http://www.daraz.pk/selfie-sticks/")
		

		elem = wait_visible_xpath(driver, '/html/body/div[1]/div/div')
		for i in range(10):
			elem.send_keys(Keys.PAGE_DOWN)
		# button = wait_visible_xpath(driver, '/html/body/div[1]/div/div/div[3]/div/div[2]/div/div/div')
		# button.click()

		# sleep(3)
		# for i in range(30):
		# 	elem.send_keys(Keys.PAGE_UP)

		
		category = Category.objects.get(name='Phone Accessories')
		
		for count in range(1,40):
			image = None
			price = None
			name = None
			image_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[1]'.format(str(count))
			image = wait_visible_xpath(driver, image_xpath)
	
			tag_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[2]/div/label[1]'.format(str(count))
			price_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[2]/span/span/span[2]'.format(str(count))
			name_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[2]/div/label[2]'.format(str(count))
			try:
				print 'try 1'
				tag = wait_visible_xpath(driver, tag_xpath)
				print 'TAG:', tag.text
				price = wait_visible_xpath(driver, price_xpath)
				print 'PRICE:', price.text
				name = wait_visible_xpath(driver, name_xpath)
				print 'NAME:', name.text
			except:
				tag_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[3]/div/label[1]'.format(str(count))
				price_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[3]/span/span/span[2]'.format(str(count))
				name_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[3]/div/label[2]'.format(str(count))
				try:
					print 'try 2'
					tag = wait_visible_xpath(driver, tag_xpath)
					print 'TAG:', tag.text
					price = wait_visible_xpath(driver, price_xpath)
					print 'PRICE:', price.text
					name = wait_visible_xpath(driver, name_xpath)
					print 'NAME:', name.text
				except:
					tag_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[4]/div/label[1]'.format(str(count))
					price_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[4]/span/span/span[2]'.format(str(count))
					name_xpath = '/html/body/div[1]/div/div/div[3]/div/section/ul/li[{}]/div/a/span[4]/div/label[2]'.format(str(count))
					print price_xpath
					try:
						print 'try 3'
						tag = wait_visible_xpath(driver, tag_xpath)
						print 'TAG:', tag.text
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

				urllib.urlretrieve(src, 'store/site_media/media/items/phone-accessories-selfie-{}-{}.jpg'.format(tag.text.lower(), str(count)))
				
				item = Item()
				item.category = category
				if len(name.text) > 50:
					item.name = name.text[:50]
				else:
					item.name = name.text
				item.price = price
				item.image = 'items/phone-accessories-selfie-{}-{}.jpg'.format(tag.text.lower(), str(count))
				item.save()
				item.tags.add("phone accessories", "selfie sticks", tag.text.lower())
				item.save()
		'''		
		driver.quit()


def wait_visible_xpath(driver, xpath):
	return WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, xpath)))
