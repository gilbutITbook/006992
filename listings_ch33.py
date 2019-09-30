################
## LISTING 33.1
################
class Fraction(object):
    def __init__(self, top, bottom):          #A
        self.top = top                        #B
        self.bottom = bottom                  #B
#A 초기화 메소드는 매개변수를 2개 받음
#B 매개변수를 가지고 데이터 속성을 초기화







################
## LISTING 33.2
################
class Fraction(object):
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
    def __add__(self, other_fraction):                                #A
        new_top = self.top*other_fraction.bottom  +  \                #B
                  self.bottom*other_fraction.top                      #C
        new_bottom = self.bottom*other_fraction.bottom                #D
        return Fraction(new_top, new_bottom)                          #E
    def __mul__(self, other_fraction):                                #F
        new_top = self.top*other_fraction.top                         #F
        new_bottom = self.bottom*other_fraction.bottom                #F
        return Fraction(new_top, new_bottom)                          #F
#B 한 줄이 너무 길어서 백슬래시()를 사용해 두 줄로 나눔
#A 두 Fraction 객체 사이의 + 연산자를 정의하기 위한 특수 메소드
#C 덧셈의 분자 계산
#D 덧셈의 분모 계산
#E 새로운 분모와 분자를 사용해 새 Fraction 객체를 만들어 반환
#F 두 Fraction 객체를 곱하는 메소드







################
## LISTING 33.3
################
class Fraction(object):
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
    def __add__(self, other_fraction):
        new_top = self.top*other_fraction.bottom  +  \
                  self.bottom*other_fraction.top 
        new_bottom = self.bottom*other_fraction.bottom
        return Fraction(new_top, new_bottom)   
    def __mul__(self, other_fraction):
        new_top = self.top*other_fraction.top
        new_bottom = self.bottom*other_fraction.bottom
        return Fraction(new_top, new_bottom)
    def __str__(self):                                           #A
        return str(self.top)+"/"+str(self.bottom)                #B
#A Fraction 객체를 출력하기 위해 문자열로 변환할 때 사용하는 메소드를 정의
#B 어떤 내용을 출력할지 지정하는 문자열을 반환




