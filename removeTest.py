import unittest

def remove_buggy(L, e):
    """
    L, 리스트
    e, 임의의 객체
    L에 있는 모든 e를 제거함.
    """
    for i in L:
        if e == i:
            L.remove(i)

def remove_buggy_fixed(L, e):
    """
    L, 리스트
    e, 임의의 객체
    L에 있는 모든 e를 제거함.
    """
    for i in L.copy():
        if e == i:
            L.remove(i)

class Tests(unittest.TestCase):
    def test_123_1(self):
        L = [1,2,3]
        remove_buggy(L,1)
        self.assertEqual(L, [2,3])
    def test_1123_1(self):
        L = [1,1,2,3]
        remove_buggy(L,1)
        self.assertEqual(L, [2,3])

unittest.main()
