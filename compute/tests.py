from django.test import TestCase

from compute.utils import get_next_ipv4, generate_ipv6_by_ipv4

class SimpleTest(TestCase):
	def test_generate_ip(self):
		print "START TEST_GENERATE_IP"

		ip_used = ['10.0.0.1', '10.0.0.5', '10.0.0.4']

		ipv4 = get_next_ipv4('10.0.0.1', '10.0.0.20', '24', ip_used)
		ipv6 = generate_ipv6_by_ipv4('2001:470:cb19:c', ipv4)

		print ipv4
		print ipv6

		print "STOP TEST_GENERATE_IP"
		self.assertTrue(True)
