from django.test import TestCase

from compute.utils import get_next_ip

class SimpleTest(TestCase):
	def test_generate_ip(self):
		print "START TEST_GENERATE_IP"

		print get_next_ip()

		print "STOP TEST_GENERATE_IP"
		self.assertTrue(True)
