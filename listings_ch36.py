################
## LISTING 36.1
################
import unittest                                   #A
 
class TestMyCode(unittest.TestCase):              #B
    def test_addition_2_2(self):                  #C
        self.assertEqual(2+2, 4)                  #D
    def test_subtraction_2_2(self):               #E
        self.assertNotEqual(2-2, 4)               #F
 
unittest.main()                                   #G
#A unittest 라이브러리를 불러옴
#B 실행할 테스트 스위트를 나타내는 클래스
#C 2 + 2가 4인지 검증하는 메소드
#D 2+2와 4가 같다는 단언문(assert)을 통해 2+2와 4가 같음을 검사하는 테스트
#E 2-2가 4가 아님을 검증하는 메소드
#F 2-2와 4가 같지 않다는 단언문을 통해 2-2와 4가 다름을 검사하는 테스트
#G 여러분이 만든 테스트 스위트 클래스 안에 들어있는 테스트들을 실행함




################
## LISTING 36.2
################
def is_prime(n):
    prime = True
    for i in range(1,n):
        if n%i == 0:
            prime = False
    return prime
    
def absolute_value(n):
    if n < 0:
        return -n
    elif n > 0:
        return n



################
## LISTING 36.3
################
import unittest                    #A
import funcs                       #B
 
class TestPrime(unittest.TestCase):       #C
    def test_prime_5(self):               #D
        isprime = funcs.is_prime(5)       #E
        self.assertEqual(isprime, True)   #F
    def test_prime_4(self):
        isprime = funcs.is_prime(4)
        self.assertEqual(isprime, False)
    def test_prime_10000(self):
        isprime = funcs.is_prime(10000)
        self.assertEqual(isprime, False)
        
class TestAbs(unittest.TestCase):
    def test_abs_5(self):
        absolute = funcs.absolute_value(5)
        self.assertEqual(absolute, 5)
    def test_abs_neg5(self):
        absolute = funcs.absolute_value(-5)
        self.assertEqual(absolute, 5)
    def test_abs_0(self):
        absolute = funcs.absolute_value(0)
        self.assertEqual(absolute, 0)
        
unittest.main()  
#A unittest의 클래스와 함수를 불러옴
#B funcs.py의 클래스와 함수를 불러옴
#C 한 종류의 테스트들에 대해 하나씩 클래스를 만듦
#D 테스트. 메소드 이름이 어떤 동작을 테스트하는지 표현함
#E 5를 인자로 funcs.py에 있는 is_prime을 호출하고 결과를 isprime에 저장
#F 함수 호출 결과가 True인지 검사
