from django.test import TestCase
from .forms import RegisterForm

# Create your tests here.

class RegisterForm_test(TestCase):

	def test_registerForm(self):

		 # test invalid data

		 invalid_data = {
		 	"username":"user@test.com",
		 	"email"   :"horraira",
		 	"password": "secret",
     	    "confirm": "not secret"
		 }

		 form = RegisterForm(data=invalid_data)
		 form.is_valid()
		 self.assertTrue(form.errors)

		 # test valid data

		 valid_data = {
		 	"username":"user@test.com",
		 	"email"   :"horraira",
		 	"password": "secret",
     	    "confirm": "not secret"
		 }

		 form = RegisterForm(data=invalid_data)
		 form.is_valid()
		 self.assertFalse(form.errors)
