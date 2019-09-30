import time
import random

def roll_dice():
   r = str(random.randint(1,6))
   #  _
   # |6| 처럼 숫자 주변을 둘러싸서 주사위처럼 보이게 표시한다
   dice = " _ \n|" + r + "|\n"
   print(dice)
   return r

start = time.clock()

p = "r"
while p == "r":
    print("플레이어가 주사위를 굴립니다...")
    userroll = roll_dice()
    print("컴퓨터가 주사위를 굴립니다...")
    comproll = roll_dice()
    time.sleep(2)
    if userroll >= comproll:
        print("플레이어가 이겼습니다!")
    else:
        print("플레이어가 졌습니다.")
    p = input("더 굴리고 싶으면 r을, 그렇지 않으면 아무 키나 누르십시오: ")
end = time.clock()
print("총", end-start, "초동안 플레이하셨습니다.")
