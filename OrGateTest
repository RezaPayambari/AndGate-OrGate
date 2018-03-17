import unittest

from OrGate import OrGate


class OrGateTest(unittest.TestCase):

    def testcase_01(self):
        a = OrGate(False,False)
        a.execute()
        self.assertFalse(a.Output, "Class OrGate: TestCase 1 failed.")

    def testcase_02(self):
        a = OrGate(True,False)
        a.execute()
        self.assertTrue(a.Output, "Class OrGate: TestCase 1 failed.")

    def testcase_03(self):
        a = OrGate(False,True)
        a.execute()
        self.assertTrue(a.Output, "Class OrGate: TestCase 1 failed.")

    def testcase_04(self):
        a = OrGate(True,True)
        a.execute()
        self.assertTrue(a.Output, "Class OrGate: TestCase 1 failed.")


if __name__ == "__main__":
    unittest.main()



