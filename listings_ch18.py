################
## LISTING 18.1
################
secret = "code"
guess = input("단어를 추측해 보세요: ")
tries = 1
while guess != secret:                                   #A
    print("지금까지 ", tries, "번 추측에 실패했습니다")
    guess = input("다른 단어를 추측해 보세요: ")            #B
    tries += 1
print("맞추셨습니다!")                                    #C
#A 추측한 단어가 비밀 단어와 다른지 검사한다
#B 사용자에게 다시 물어본다
#C 추측이 올바른 경우 여기 도달한다


################
## LISTING 18.2
################
# 아래 블럭은 정상적인 파이썬 코드 블럭이 아니어서 '''로 감싸서 오류를 방지함
'''
while <조건>:               #A
    <어떤 일을 한다>
'''
#루프 시작을 나타낸다


################
## LISTING 18.3
################
for x in range(3):                 #A             
    print("var x is", x)           

x = 0                              #B
while x < 3:                       #A
    print("var x is", x)
    x += 1                         #C
#A 루프의 시작을 나타냄
#B 루프 변수 초기화
#C 루프 변수 증가



################
## LISTING 18.4
################
secret = "code"
max_tries = 100
guess = input("단어를 추측해 보세요: ")
tries = 1
while guess != secret:
    print("지금까지 ", tries, "번 추측에 실패했습니다")
    if tries == max_tries:
        print("추측할 수 있는 기회를 다 썼습니다.")
        break                                     #A
    guess = input("다른 단어를 추측해 보세요: ")
    tries += 1
if tries <= max_tries and guess == secret:        #B
    print("맞추셨습니다!")
#A max_tries 이상 추측을 시도한 경우 루프를 깨고 루프 밖으로 나온다
#B 루프에서 나온 이유를 알아낸다


################
## LISTING 18.5
################
### 코드 버전 1 ###
x = 0
for x in range(100):
    print("x 는", x)
    if x > 5:
        print("x가 5보다 큽니다")
        if x%10 != 0:
            print("x를 10으로 나눌 수 없습니다")
            if x==2 or x==4 or x==16 or x==32 or x==64:
                print("x는 2의 거듭제곱 수입니다")
                # 코드가 더 올 수 있음

### 코드 버전 2 ###
x = 0
for x in range(100):
    print("x 는", x)
    if x <= 5:
        continue                         #A
    print("x가 5보다 큽니다")              #B
    if x%10 == 0:
        continue                         #A
    print("x를 10으로 나눌 수 없습니다")    #C
    if x!=2 and x!=4 and x!=16 and x!=32 and x!=64:
        continue                         #A 
    print("x는 2의 거듭제곱 수입니다")      #D
    # 코드가 더 올 수 있음

#A x > 5인 경우 여기로 진행함
#B x%10 != 0인 경우 여기로 진행함
#C x가 2,4,16,32,64 중 하나인 경우 여기로 진행함
#D 루프 본문의 나머지 문장 실행 생략