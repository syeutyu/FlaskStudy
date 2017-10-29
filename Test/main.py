import unittest # 파이썬에서 기본 제공하는 모듈단위 테스트방식

def add(x):
    return x + 1

class Test_01(unittest.TestCase):
    def test(self):
        self.assertEqual(add(3), 5, msg="Wrong!") # Error
        self.assertEqual(add(3), 4)

class Test_02(unittest.TestCase):
    def test(self):
        self.assertEqual(add(4), 5)
        self.assertEqual(add(4), 5)

class Test_03(unittest.TestCase):
    def test(self):
        self.assertTrue(self.checkBool(True,False), msg="Bool false") # Error
    def checkBool(self,A,B):
        return True if A and B else False

#assertEqual(A, B, msg='') : A와 B가 같은지 테스트, 같지 않은 경우 테스트가 실패하며 msg 출력.
#assertNotEqual(A, B, msg='') : A와 B가 다른지 테스트, 같은 경우 테스트가 실패하며 msg 출력.
#assertTrue(A, msg='') : A가 True 인지 테스트, False 경우 테스트가 실패하며 msg 출력.
#assertFalse(A, msg='') : A가 False 인지 테스트, True 경우 테스트가 실패하며 msg 출력

if __name__ == '__main__':
    unittest.main()

