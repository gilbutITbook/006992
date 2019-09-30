################
## LISTING 27.1
################
legs = {}                  #A
legs["사람"] = 2            #B
legs["고양이"] = 4          #C
legs["뱀"] = 0             #D
print(len(legs))           #E
legs["고양이"] = 3          #F
print(len(legs))           #G
print(legs)                #H
#A 빈 사전
#B “사람”과 2 연관시키기
#C “고양이”와 4 연관시키기
#D “뱀”과 0 연관시키기
#E 사전에 3가지 항목이 있으므로 3 출력
#F “고양이”와 연관된 값을 3으로 바꾸기
#G 고양이”와 연관된 값만 변경했으므로 3을 출력
#H { '사람': 2, '고양이': 3, '뱀': 0 } 출력




################
## LISTING 27.2
################
household = {"사람":4, "고양이":2, "개":1, "금붕어":2}     #A
removed = household.pop("금붕어")                          #B
print(removed)                                           #C
#A 사전을 채움
#B 키가 “금붕어”인 항목을 찾아서 제거하되, “금붕어”라는 키와 연관됐던 값을 removed에 저장함
#C 제거한 항목의 값을 출력




################
## LISTING 27.3
################
grades = {}                        #A
grades["프랭크"] = [100, 70]        #A
grades["토비"] = [90, 100]       #A
grades["도남"] = [80, 40]         #A
grades["제이스"] = [70, 70]        #A

for student in grades.keys():      #B
    print(student)                 #B

for quizzes in grades.values():    #C
    print(sum(quizzes)/2)          #C
    
for student in grades.keys():              #D
    scores = grades[student]                      #E
    grades[student].append(sum(scores)/2)         #F
print(grades)                                     #G
#A 문자열과 두 퀴즈 성적을 연관짓는 사전을 설정함
#B 키에 대해 루프를 돌며 출력
#C 값에 대해 루프를 돌며 평균을 출력
#D 모든 키에 대해 루프를 돎
#E 다음 줄에서 평균을 계산하기 위해, 각 학생의 성적을 가져와서 scores 변수에 대입
#F 원소들의 평균을 계산하고, 계산한 평균 값을 리스트 뒤에 덧붙임
#G {'프랭크': [100, 70, 85.0], '토비': [90, 100, 95.0], '도남': [80, 40, 60.0], '제이스': [70, 70, 70.0]}를 출력



################
## LISTING 27.4
################
lyrics = "Happy birthday to you Happy birthday to you Happy birthday dear Happy birthday to you"                                           #A
counts = {}                                                      #B

words = lyrics.split(" ")                                        #C
for w in words:                                                  #D
    w = w.lower()                                                #E
    if w not in counts:
        counts[w] = 1                                            #F
    else:
        counts[w] += 1                                           #G
        
print(counts)                                                    #H
#A 노래 가사 문자열
#B 비어있는 빈도 사전
#C 문자열을 공백을 기준으로 나눠서 단어 리스트를 만듦
#D 앞 줄에서 만든 리스트의 모든 단어를 이터레이션함
#E 소문자로 바꿈
#F 사전에 단어가 없었으므로 단어를 사전에 키로 추가하면서 값을 1로 지정
#G 사전에 이미 단어가 있으므로, 빈도수를 1 증가시킴
#H {'happy': 4, 'birthday': 4, 'to': 3, 'you': 3, 'dear': 1, 'frank': 1}를 출력



################
## LISTING 27.5
################
def square(x):                            #A
    return x*x                            #A
    
def circle(r):                            #B
    return 3.14*r*r                       #B
    
def equilateraltriangle(s):               #C
    return (s*s)*(3**0.5)/4               #C
    
areas = {"sq": square, "ci": circle, "eqtri": equilateraltriangle}    #D

n = 2
print(areas["sq"](n))                                    #E
print(areas["ci"](n))                                    #F
print(areas["eqtri"](n))                                 #G
#A 정사각형 넓이를 계산하는 함수
#B 원 넓이를 계산하는 함수
#C 정삼각형 넓이를 계산하는 함수
#D 문자열과 함수를 매핑하는 사전
#E 사전에서 “sq”라는 키가 가리키는 함수에 n을 넘겨 호출. n은 2
#F 사전에서 “ci”라는 키가 가리키는 함수에 n을 넘겨 호출. n은 2
#G 사전에서 “eqtri”라는 키가 가리키는 함수에 n을 넘겨 호출. n은 2
