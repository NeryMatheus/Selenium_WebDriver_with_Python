import unittest


class TestClass2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("#" * 30)
        print("Class 2 -> Class Level SetUp")
        print("#" * 30)

    def setUp(self):
        print("Class 2 -> Setup")

    def test_class2_method1(self):
        print("Class 2 -> Running Method 1")

    def test_class2_method2(self):
        print("Class 2 -> Running Method 2")

    def test_class2_method3(self):
        print("Class 2 -> Running Method 3")

    def tearDown(self):
        print("Class 2 -> Tear Down")

    @classmethod
    def tearDownClass(cls):
        print("#" * 30)
        print("Class 2 -> Class Level Tear Down")
        print("#" * 30)


if __name__ == "__main__":
    unittest.main(verbosity=2)
