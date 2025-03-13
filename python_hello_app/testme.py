#!/usr/bin/env python3

import unittest

def hello(a):
	return a.upper()

class TestMe(unittest,TestCase):
	def test_hello(self):
		result = hello("mama")
		self.assertEqual(result,"MAMA")

if __name__ == "__main__":
	unittest.main()
