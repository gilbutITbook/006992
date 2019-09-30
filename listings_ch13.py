################
## LISTING 13.1
################
num = int(input("Enter a number: "))       #A
if num > 0:                                #B
    print("num is positive")               #C
print("finished comparing num to 0")       #D
#A 사용자 입력을 기다렸다가 사용자가 입력한 값을 num이라는 변수에 저장
#B num에 저장된 값이 0보다 큰지 검사하는 if문
#C num이 0보다 크다면 이 들여쓰기 한 블록 안으로 들어가서 블록 안에 있는 모든 문장을 실행
#D num이 0과 같거나 0보다 작다면 들여 쓴 블록 안에 들어가지 않고 이 줄을 바로 출력



################
## LISTING 13.2
################
# 아래 블럭은 정상적인 파이썬 코드 블럭이 아니어서 '''로 감싸서 오류를 방지함
'''
<if 조건문 앞의 코드>                 #A
if <조건식>:                  #B
    <어떤 일을 수행하는 코드>                 #C
<if 조건문 뒤의 코드>                  #A
'''
#A <if조건문 앞의 코드>는 조건을 검사하기 전에 수행되고, <if조건문 뒤의 코드>는 조건문을 다 실행한 다음에 실행됨
#B “if” 키워드는 조건문을 시작하며, “if” 뒤에는 조건 식이 옴
#C 들여쓰기는 if문의 조건이 참인 경우에만 실행되는 코드들을 표현함


################
## LISTING 13.3
################
num_a = int(input("Pick a number: "))             #A
if num_a > 0:                                     #B
    print("Your number is positive")              #C
if num_a < 0:                                     #D
    print("Your number is negative ")             #E
if num_a == 0:                                    #F
    print("Your number is zero")                  #G
print("Finished!")                                #H
#A 사용자 입력 받기
#B 입력받은 수가 0보다 큰지 검사
#C 앞의 조건이 참인 경우에만 이 문장을 실행
#D 입력받은 수가 0보다 작은지 검사
#E 앞의 조건이 참인 경우에만 이 문장을 실행
#F 입력받은 수가 0과 같은지 검사
#G 앞의 조건이 참인 경우에만 이 문장을 실행
#H 조건과 관계 없이 이 문장을 실행




################
## LISTING 13.4
################
num_a = int(input("수를 하나 입력하세요: "))
num_b = int(input("수를 하나 입력하세요: "))
if num_a < 0:                       #A   
    print("num_a는 음수입니다")
    if num_b < 0:                   #B   
        print("num_b는 음수입니다")   #C
print("끝")

num_a = int(input("수를 하나 입력하세요: "))
num_b = int(input("수를 하나 입력하세요: "))
if num_a < 0:                       #A
    print("num_a는 음수입니다")
if num_b < 0:                       #B
    print("num_b는 음수입니다")       #C
print("끝")
#A 첫번째 조건문
#B 두번째 조건문
#C 실행할 문장



################
## LISTING 13.5
################
price = float(input("초콜릿 바 1개 가격은 몇 원인가요? "))           #A
hungry = input("배가 고픈가요 (yes/no)? ")                         #A
bars = 0

if hungry == "yes":                                               #B
    if price < 1:                                                 #C
        print("초콜릿 바를 전부 다 산다.")                           #D
        bars = 100                                                #D
    if 1 <= price <= 5:                                           #E
        print("초콜릿 바를 전부 다 산다.")                           #E
        bars = 10                                                 #E
    if price > 5:                                                 #F
        print("초콜릿 바를 1개 산다.")                              #F
        bars = 1                                                  #F
if hungry == "no":                                                #G
    print("쇼핑 목록에 원래 들어있던 것만 산다.")                     #G
if bars > 10:                                                     #H
    print("계산원: 배고픈 분이 계신가봐요!")                          #H
#A 사용자 입력
#B 배고픈지 결정하기 위한 조건문
#C 초콜릿 바 가격이 1000원 미만인지 결정하기 위한 조건문
#D 초콜릿 바가 1000원 미만일 때 수행할 동작
#E 초콜릿 바 가격이 1000원 이상 5000원 이하인지 결정하기 위한 조건문과 동작
#F 초콜릿 바 가격이 5000원 초과인지 결정하기 위한 조건문과 동작
#G 사용자가 배고프지 않아서 “no”라고 답했을 때 적절한 문장을 출력하기 위한 조건문
#H 초콜릿 바를 10개 초과해서 산 경우에만 메시지를 출력하기 위한 조건문
