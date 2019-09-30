################
## LISTING 35.1
################
import math                                                              #A

distance = float(input("친구와 당신의 거리는 얼마입니까? (m) "))
speed = float(input("당신이 던진 공의 속력은 얼마입니까? (m/s) "))
angle_d = float(input("던진 공이 지면과 이루는 각도는 얼마입니까? (도) "))
tolerance = 2

angle_r = math.radians(angle_d)                                          #B

reach = 2*speed**2*math.sin(angle_r)*math.cos(angle_r)/9.8               #C

if reach > distance - tolerance and reach < distance + tolerance:
    print("나이스 피처!")
elif reach < distance - tolerance:
    print("충분히 멀리 던지지 못했습니다.")
else:
    print("너무 멀리 던졌습니다.")
#A 수학 라이브러리인 math 라이브러리를 임포트함
#B math.sin과 math.cos는 각도로 도(degree)가 아닌 라디안을 입력받음. 따라서 사용자 입력을 라디안으로 변환함
#C 수학 라이브러리의 함수를 사용해 공식을 구현








################
## LISTING 35.2
################
import random                              #A

choice = input("가위, 바위, 보 중 하나를 고르세요: ")
r = random.random()                        #B
if r < 1/3:                                #C
    print("컴퓨터는 바위를 냈습니다.")
    if choice == "보":
        print("당신이 이겼습니다!")
    elif choice == "가위":
        print("당신이 졌습니다.")
    else:
        print("비겼습니다.")
elif 1/3 <= r < 2/3:                       #D
    print("컴퓨터는 보를 냈습니다.")
    if choice == "가위":
        print("당신이 이겼습니다!")
    elif choice == "바위":
        print("당신이 졌습니다.")
    else:
        print("비겼습니다.")
else:                                      #E
    print("컴퓨터는 가위를 냈습니다.")
    if choice == "바위":
        print("당신이 이겼습니다!")
    elif choice == "보":
        print("당신이 졌습니다.")
    else:
        print("비겼습니다.")
#A random라이브러리에 정의된 함수들을 불러옴
#B 0이상 1미만의 부동소수점 난수를 발생시킴
#C 1/3 확률로 컴퓨터가 바위를 선택한 경우
#D 1/3 확률로 컴퓨터가 보를 선택한 경우
#E 1/3 확률로 컴퓨터가 가위를 선택한 경우





################
## LISTING 35.3
################
import time                 #A

# 원서 코드는 time.clock()이었으나 3.7부터는 사용 금지됐다.
# 대신 time.perf_counter()를 써야 한다.
# pref_counter()의 값은 나노초 단위까지 돌려주며, 정밀도는 시스템에 따라 다르다
start = time.perf_counter() #B

count = 0                   #C
for i in range(1000000):    #C
    count += 1              #C

end = time.perf_counter()   #D
print(end-start)            #D
#A time 라이브러리에 정의된 함수를 불러옴
#B 클럭의 현재 시간을 나노초(ns) 단위로 가져옴
#C 1백만번 카운트를 세는 코드
#D 클럭의 현재 시간을 나노초(ns) 단위로 가져옴
#E start와 end 사이의 차이를 출력




################
## LISTING 35.4
################
import time                                                      #A

print("Loading...")
for i in range(10):                                              #B
    print("[",i*"*",(10-i)*" ","]",i*10,"% complete")            #C
    time.sleep(0.5)                                              #D
#A time 라이브러리에 정의된 함수를 불러옴
#B 10%씩 증가하는 프로그래스바를 표현하는 루프
#C 여러 * 문자로 표시되는 프로그래스 바를 출력
#D 0.5초간 프로그램을 일시 중단
