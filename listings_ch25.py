################
## LISTING 25.1
################
years = [1984, 1986, 1988, 1988]
print(len(years))                         #A
print(years.count(1988))                  #B
print(years.count(2017))                  #C
print(years.index(1986))                  #D
print(years.index(1988))                  #E
#A 리스트에 원소가 4개 있으므로 4를 출력
#B 리스트에 1988이 두 번 나타나므로 2를 출력
#C 2017이 리스트에 없으므로 0을 출력
#D 1986이 1번 인덱스 위치에 있으므로 1을 출력(첫번째 원소의 인덱스는 0)
#E 1988 중에 가장 앞에 있는 것의 위치가 세번째이므로 2를 출력




################
## LISTING 25.2
################
first3letters = []                         #A
first3letters.append("a")                  #B
first3letters.append("c")                  #C
first3letters.insert(1,"b")                #D
print(first3letters)                       #E
last3letters = ["x", "y", "z"]             #F
first3letters.extend(last3letters)         #G
print(first3letters)                       #H
last3letters.extend(first3letters)         #I
print(last3letters)                        #J
#A 빈 리스트
#B first3letters 리스트 맨 뒤에 “a” 추가
#C first3letters 리스트 맨 뒤에 “c” 추가
#D first3letters 리스트의 1번 인덱스 위치에 “b” 삽입
#E ['a', 'b', 'c'] 출력
#F 원소가 3개 있는 리스트 생성
#G first3letters 리스트 맨 뒤에 “x”, “y”, “z” 추가
#H ['a', 'b', 'c', 'x', 'y', 'z'] 출력
#I 상태가 바뀐 first3letters 리스트를 last3letters 뒤에 덧붙임. “a”, “b”, “c”, “x”, “y”, “z”를 덧붙이는 것과 같은 효과
#J ['x', 'y', 'z', 'a', 'b', 'c', 'x', 'y', 'z'] 출력


################
## LISTING 25.3
################
polite = ["please", "and", "thank", "you"]                       #A
print(polite.pop())                                              #B
print(polite)                                                    #C
print(polite.pop(1))                                             #D
print(polite)                                                    #E
#A 원소가 4개인 리스트
#B pop()이 리스트의 맨 마지막 원소를 반환하기 때문에 “you”를 출력
#C pop()이 리스트의 맨 마지막 원소를 제거했기 때문에 ['please', 'and', 'thank']를 출력
#D pop(1)이 1번 인덱스에 있는 원소를 반환하기 때문에 “and”를 출력
#E pop(1)이 1번 인덱스의 원소(두번째 원소)를 제거했기 떄문에 ['please', 'thank']를 출력


################
## LISTING 25.4
################
colors = ["red", "blue", "yellow"]                #A
colors[0] = "orange"                              #B
print(colors)                                     #C
colors[1] = "green"                               #D
print(colors)                                     #E
colors[2] = "purple"                              #F
print(colors)                                     #G
#A 문자열로 이뤄진 리스트를 초기화
#B “red”를 “orange”로 변경
#C 두번째 줄에서 0번 인덱스에 있는 원소를 바꿨기 때문에 ['orange', 'blue', 'yellow']를 출력
#D 0번 인덱스에 “orange”가 들어있게 상태가 바뀐 리스트의 “blue”를 “green”으로 변경
#E 네번째 줄에서 1번 인덱스의 원소를 바꿨기 때문에 ['orange', 'green', 'yellow']를 출력
#F 0번 인덱스에”orange“, 1번 인덱스에”green“이 들어있게 된 리스트의”yellow“를”purple"로 변경
#G 여섯번쨰 줄에서 2번 인덱스에 있는 원소를 바꿨기 때문에 ['orange', 'green', 'purple']를 출력
