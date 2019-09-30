################
## LISTING 32.1
################
class Stack(object):
    def __init__( self):
        self.stack = []                   #A
    def get_stack_elements(self):
        return self.stack.copy()          #B
    def add_one(self , item):
        self.stack.append(item)           #C
    def add_many(self , item, n):
        for i in range(n):                #D
            self.stack.append(item)       #D
    def remove_one(self):
        self.stack.pop()                  #E
    def remove_many(self , n):
        for i in range(n):                #F
            self.stack.pop()              #F
    def size(self):
        return len(self.stack)            #G
    def prettyprint(self):
        for thing in self.stack[::-1]:    #H
            print('|_',thing, '_|')       #H
#A 스택을 정의하는 데이터 속성인 리스트
#B 스택을 표현하는 데이터 속성의 복사본을 반환하는 메소드
#C 스택에 원소를 추가하는 메소드. 리스트 맨 끝에 원소를 추가함
#D 같은 원소를 n개 추가하는 메소드
#E 원소를 하나 제거하는 메소드
#F 스택에서 n개의 원소를 제거하는 메소드
#G 스택에 들어있는 원소의 개수를 알려주는 메소드
#H 한줄에 한 원소씩 스택을 출력하는 메소드. 최근에 들어온 원소를 더 위쪽에 출력함





################
## LISTING 32.2
################
pancakes = Stack()                        #A
pancakes.add_one("해물")                  #B
pancakes.add_many("감자", 4)              #C
print(pancakes.size())                    #D
pancakes.remove_one()                     #E
print(pancakes.size())                    #F
pancakes.prettyprint()                    #G
#A Stack 객체를 만들어서 buchimgae라는 이름의 변수에 대입
#B 해물 부침개를 하나 추가
#C 감자 부침개를 4개 추가
#D 5를 출력
#E 맨 마지막에 추가했던 문자열을 제거(“감자”를 제거)
#F 4를 출력
#G 한 줄에 하나씩 부침개를 출력. 감자가 3번 먼저 출력되고 맨 마지막에 해물 출력





################
## LISTING 32.3
################
circles  = Stack()                        #A
one_circle = Circle()                     #B
one_circle.change_radius(2)               #B
circles.add_one(one_circle)               #B

for i in range(5):                        #C
    one_circle = Circle()                 #D
    one_circle.change_radius(1)           #D
    circles.add_one(one_circle)           #D

print(circles.size())                     #E
circles.prettyprint()                     #F
#A 스택을 만들고 그 객체를 circles라는 변수에 대입
#B 새 Circle 객체를 만들고 반지름을 2로 설정한 후 스택에 추가
#C 새 Circle 객체를 다섯개 추가하는 루프
#D 루프를 돌 때마다 새 Circle 객체를 만들어서 반지름을 1로 설정한 후 스택에 추가
#E 6을 출력
#F 각 Circle 객체와 연관된 파이썬 정보(타입과 메모리 상의 위치)를 출력


################
## LISTING 32.4
################
circles  = Stack()                        #A
one_circle = Circle()                     #A
one_circle.change_radius(2)               #A
circles.add_one(one_circle)               #A

one_circle = Circle()                     #B
one_circle.change_radius(1)               #B
circles.add_many(one_circle, 5)           #C

print(circles.size())                     #D
circles.prettyprint()                     #E
#A 리스트 32.3과 같은 연산들
#B 새 Circle 객체를 만들고 반지름을 1로 설정
#C 똑같은 Circle 객체를 Stack 클래스의 메소드를 사용해 다섯번 추가
#D 이 시점에 스택에 들어있는 원의 개수인 6을 출력
#E 각 Circle 객체와 연관된 파이썬 정보(타입과 메모리 상의 위치)를 출력
