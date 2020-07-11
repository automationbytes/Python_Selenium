import unittest

def setUpModule():
    print("Its Setup module")

class sample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Its setup class")

    def setUp(self):
        print("Its Setup step")

    def test1(self):
        print("Its Test1")

    def test2(self):
        print("Its Test2")
    @unittest.skipUnless(1>2,"1 is less than 2")
    def test3(self):
        #self.skipTest("Not needed")
        print("Test3")

    #@unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

    def tearDown(self):
        print("Its Teardown step ")

    @classmethod
    def tearDownClass(cls):
        print("Its Teardown class method")


def tearDownModule():
    print("Its teardown module")
if __name__ == '__main__':
    unittest.main()