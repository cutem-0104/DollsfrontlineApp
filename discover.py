import unittest, sys

def suite():
	test_suite = unittest.TestSuite()
	all_test_suite = unittest.defaultTestLoader.discover("test", pattern="test_*.py")
	for ts in all_test_suite:
		test_suite.addTest(ts)
	return test_suite

if __name__ == "__main__":
	mySuite = suite()
	try:
		unittest.TextTestRunner().run(mySuite)
	except ImportError as e:
		sys.exit(1)
