################
## LISTING 20.1
################
a = 1               #A
b = 2               #A
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#A 변수 a와 b를 사용해 a+b, a-b, a*b, a/b를 계산한다.



################
## LISTING 20.2
################
a = 1               #A
b = 2               #A
print(a+b)          #A
print(a-b)          #A
print(a*b)          #A
print(a/b)          #A
a = 3                      #B
b = 4                      #B
print(a+b)                 #B
print(a-b)                 #B
print(a*b)                 #B
print(a/b)                 #B
a = 5               #C
b = 6               #C
print(a+b)          #C
print(a-b)          #C
print(a*b)          #C
print(a/b)          #C
#A a = 1, b = 2일 때 연산을 수행하는 코드
#B a = 3, b = 4일 때 연산을 수행하는 코드
#C a = 5, b = 6일 때 연산을 수행하는 코드


################
## LISTING 20.3
################
a = 1
b = 2
<a와 b에 대한 네가지 연산을 감싼 래퍼>  #A
a = 3
b = 4
<a와 b에 대한 네가지 연산을 감싼 래퍼>  #A
a = 5
b = 6
<a와 b에 대한 네가지 연산을 감싼 래퍼>  #A
#A (진짜 코드가 아님) 네가지 연산을 수행하는 블랙박스의 위치를 표시
