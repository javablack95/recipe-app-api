from django.test import TestCase
from django.contrib.auth import get_user_model

class TestModels(TestCase):
	"""test if the email and password is correct for a user"""

	def test_email_and_password(self):
		email = "javablack@javablack.com"
		password = '123456789'

		user = get_user_model().objects.create_user(

			email= email,
			password = password)

		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))	


	def test_new_user_email_normalizer(self):
		"""Test the email for a new user is normalized"""
		email ='test@JAVABLACK.COM'
		user = get_user_model().objects.create_user(email , 'tests123')

		self.assertEqual(user.email, email.lower())

	def test_new_user_invalid_email(self):
		"""Test creating user with no email raises error"""

		with self.assertRaises(ValueError):
			get_user_model().objects.create_user(None, 'test123')

	def test_create_new_superuser(self):
		"""Test creating a superuser"""

		user = get_user_model().objects.create_superuser(

			'test@javablack.com',
			'tests123')
		self.assertTrue(user.is_superuser)
		self.assertTrue(user.is_staff)


