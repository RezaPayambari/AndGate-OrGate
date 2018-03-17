import unittest

from AndGate import AndGate


class AndGateTest(unittest.TestCase):

    def testcase_01(self):
        a = AndGate(False,False)
        a.execute()
        self.assertFalse(a.Output, "Class AndGate: TestCase 1 failed.")

    def testcase_02(self):
        a = AndGate(True,False)
        a.execute()
        self.assertFalse(a.Output, "Class AndGate: TestCase 1 failed.")

    def testcase_03(self):
        a = AndGate(False,True)
        a.execute()
        self.assertFalse(a.Output, "Class AndGate: TestCase 1 failed.")

    def testcase_04(self):
        a = AndGate(True,True)
        a.execute()
        self.assertTrue(a.Output, "Class AndGate: TestCase 1 failed.")


if __name__ == "__main__":
    unittest.main()



