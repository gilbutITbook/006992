################
## LISTING 17.1
################
for ch in "Python is fun so far! 재미있는 파이썬!": #A
    print("문자:", ch)                 #B
#A ch가 루프 변수임
#B 루프 변수 값을 출력



################
## LISTING 17.2
################
my_string = "Python is fun so far! 재미있는 파이썬!"   #A
len_s = len(my_string)                               #A
for i in range(len_s):                               #B
    print("문자:", my_string[i])                      #C
#A 문자열과 문자열 길이를 변수에 저장
#B 0부터 len_s - 1까지 반복
#C 문자열에 대해 인덱스를 사용
