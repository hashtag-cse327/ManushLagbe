from django.test import TestCase
from driver.models import Driver, Driver_Customer
from django.utils import timezone
from django.urls import reverse

# Create your tests here.

# models test
class DriverTest(TestCase):

	def create_driver(self, name="test name", mob="test mob", address="test address", 
						gender= "test gender", age="test age", transmission="transmission",
						auto_price= 200, manual_price=200):
		return Driver.objects.create(name=name, mob=mob, address=address, gender=gender, age=age,
									 transmission=transmission, auto_price=auto_price, manual_price=manual_price)

	def test_driver_creation(self):
		d = self.create_driver()
		#self.assertTrue(ininstance(d, Driver))
		#self.assertTrue(self.assertIsInstance(d, Driver))
		self.assertEqual(d.__str__(),d.name)


	#def test_driver(self):
	#	driver=Driver(name="my name is khan")
	#	self.assertEqual(str(driver),driver.name)

	def create_customer(self, name="test name", mob="test mob", address="test address", 
								transmission="transmission", hours=8):
		return Driver_Customer.objects.create(name=name, mob=mob, address=address, transmission=transmission, hours=hours) 

	def test_customer_creation(self):
		dc = self.create_customer()
		self.assertEqual(dc.__str__(),dc.name)


	# views test
	#def test_driver_form(self):
	#	df = self.create_driver()
	#	url = reverse("driver.views.driver")
	#	resp = self.client.gt(url)
#
	#	self.assertEqual(resp.status_code, 200)
	#	self.assertIn(df.name, resp.content)
