# 오류 방지를 위해 num_a와 num_b를 정의
num_a = -1
num_b = 10

################
## LISTING 14.1
################
if num_a < 0 and num_b < 0:
    print("둘 다 음수")


################
## LISTING 14.2
################
if num_a and num_b < 0:
    print("둘 다 음수")


################
## LISTING 14.3
################
num = int(input("수를 하나 입력하세요: "))    #A
if num > 0:                                #B
    print("양수를 입력했습니다")              #C
elif num < 0:                              #D
    print("음수를 입력했습니다")              #E
else:                                      #F
    print("영을 입력했습니다")                #G
#A 사용자 입력
#B 입력한 수가 0보다 큰지 조건 검사
#C 메시지 출력
#D num > 0이 False면 이 조건에서 입력한 수가 0보다 작은지 검사
#E 메시지 출력
#F elif num < 0도 False면 else가 나머지 모든 경우를 한꺼번에 처리
#G 메시지 출력



################
## LISTING 14.4
################
# 아래 블럭은 정상적인 파이썬 코드 블럭이 아니어서 '''로 감싸서 오류를 방지함
'''
if <조건>:                    #A
    <어떤 일을 한다>
elif <조건>:                  #B
    <어떤 일을 한다>
else:                        #C
    <어떤 일을 한다>
'''
#A if 키워드는 조건문 블록을 시작한다
#B elif 키워드는 if 조건이 성립하지 않을 때 검사할 조건(else if)을 검사하는 블록을 시작한다
#C else 키워드는 만족하는 조건이 없는 경우를 모두 처리하는(catch-all) 블록을 시작한다


################
## LISTING 14.5
################
num_a = 5
num_b = 7
lucky_num = 7
if type(num_a) != int or type(num_b) != it:       #A
    print("정수가 아닌 값을 입력했습니다")            #A
else:                                             #A
    if num_a > 0 and num_b > 0:                   #A     #C
        print("두 정수 모두 양수입니다")             #A     #C
    elif num_a < 0 and num_b < 0:                 #A     #C
        print("두 정수 모두 음수입니다")             #A     #C
    else:                                         #A     #C
        print("두 수의 부호가 서로 반대입니다")       #A     #C
if num_a == lucky_num or num_b == lucky_num:      #B
    print("게다가 행운의 수를 맞추셨습니다!")         #B
else:                                             #B
    print("마음에 둔 수가 하나 있는데요...")         #B
#A 내부에 if-elif-else문을 포함하는 if-else 그룹
#B 내포된 if-elif-else 그룹
#C 다른 if-else 그룹


################
## LISTING 14.6
################
num_a = 5
num_b = 7
lucky_num = 7
if type(num_a) != int or type(num_b) != int:
    print("정수가 아닌 값을 입력했습니다")
elif num_a > 0 and num_b > 0:                     #A
    print("두 정수 모두 양수입니다")
elif num_a < 0 and num_b < 0:                     #A
    print("두 정수 모두 음수입니다")
else:                                             #A
    print("두 수의 부호가 서로 반대입니다")
if num_a == lucky_num or num_b == lucky_num:
    print("게다가 행운의 수를 맞추셨습니다!")
else:
    print("마음에 둔 수가 하나 있는데요...")
#A 리스트 14.5의 else블럭을 여러 elif 블럭으로 바꿨다



################
## LISTING 14.7
################
greeting = input("영어나 스페인어로 인삿말을 입력하세요! ")
greet_en = ("hi", "Hi", "hello", "Hello")
greet_sp = ("hola", "Hola")
if greeting not in greet_en and greeting not in greet_sp:   #A
    print("어떤 인사인지 이해할 수가 없네요.")
elif greeting in greet_en:                                  #A
    num = int(input("1이나 2를 입력해주세요: "))
    print("영어를 하시는군요!")
    if num == 1:                                            #B
        print("one")
    elif num == 2:                                          #B
        print("two")
elif greeting in greet_sp:                                  #A
    num = int(input("1이나 2를 입력해주세요: "))
    print("스페인어를 하시는군요!")
    if num == 1:                                            #C
        print("uno")
    elif num == 2:                                          #C
        print("dos")
#A if-elif로 구성된 코드 블럭
#B if-elif 블럭을 포함하는 내포된 블럭
#C 다른 if-elif 블럭을 포함하는 내포된 블럭

