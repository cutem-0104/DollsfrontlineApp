import unittest, sys

def suite():
	try:
		test_suite = unittest.TestSuite()
		all_test_suite = unittest.defaultTestLoader.discover("test", pattern="test_*.py")
		for ts in all_test_suite:
			test_suite.addTest(ts)
		return test_suite
	except Exception as e:
		print(e)
		sys.exit(1)

if __name__ == "__main__":
	try:
		mySuite = suite()
		unittest.TextTestRunner().run(mySuite)
	except Exception as e:
		print(e)
		sys.exit(1)
	
