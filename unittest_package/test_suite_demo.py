import unittest
from unittest_package.test_class1 import TestClass1
from unittest_package.test_class2 import TestClass2

# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# Create a test suite combining TestClass1 and TestClass2
smoke_test = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(smoke_test)