################
## LISTING 6.1
################
minutes_to_convert = 123
hours_decimal = minutes_to_convert/60                #A
hours_part = int(hours_decimal)                      #A

minutes_decimal = hours_decimal-hours_part           #B
minutes_part = round(minutes_decimal*60)             #B

print(hours_part)                                    #C
print("시간")                                       #C
print(minutes_part)                                  #C
print("분")                                     #C
#A 몇 시간인지를 실수로 계산한 다음 정수로 변환해서 온전한 시간이 몇 시간이 되는지 찾음
#B 소수점 아래 부분을 얻어서 분에 해당하는 정수 값으로 변환
#C 결과를 출력




################
## LISTING 6.2
################
minutes_to_convert = 123                  #A

hours_decimal = minutes_to_convert/60     #B
hours_part = int(hours_decimal)           #C

minutes_part = minutes_to_convert%60      #D

print(hours_part)
print("시간")
print(minutes_part)
print("분")
#A 분에 해당하는 정수가 주어짐
#B 실수로 몇 시간인지 계산
#C 정수로 변환해서 온전한 시간을 구함
#D 나머지 연산을 사용해 분을 60으로 나눌 때의 나머지를 계산해서 온전한 분을 얻음





















