import unittest


class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("#" * 30)
        print("Class 1 -> Class Level SetUp")
        print("#" * 30)

    def setUp(self):
        print("Class 1 -> Setup")

    def test_method1(self):
        print("Class 1 -> Running Method 1")

    def test_method2(self):
        print("Class 1 -> Running Method 2")

    def test_method3(self):
        print("Class 1 -> Running Method 3")

    def tearDown(self):
        print("Class 1 -> Tear Down")

    @classmethod
    def tearDownClass(cls):
        print("#" * 30)
        print("Class 1 -> Class Level Tear Down")
        print("#" * 30)


if __name__ == "__main__":
    unittest.main(verbosity=2)
