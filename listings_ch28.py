################
## LISTING 28.1
################
def add_word(d, word, definition):            #A
    """ d, 문자열을 문자열의 리스트와 연관시키는 사전(dict)
        word, 문자열
        definition, 문자열
        d를 변경한다(word: definition 쌍을 사전에 추가)
        word가 이미 d에 들어있다면 definition을 word와 연관된 리스트에 추가한다
        아무 것도 반환하지 않는다
    """
    if word in d:                             #B
        d[word].append(definition)            #C
    else:                                     #D
        d[word] = [definition]                #E

words = {}                                    #F
add_word(words, 'box', 'fight')               #G
print(words)                                  #H
add_word(words, 'box', 'container')           #I
print(words)                                  #J
add_word(words, 'ox', 'animal')               #K
print(words)                                  #L
#A 사전, 문자열(word), 다른 문자열(definition)을 매개변수로 받는 함수
#B 사전에 들어있는 word
#C definition을 word와 연관된 리스트 끝에 추가
#D 사전에 들어있지 않은 word
#E word를 키로 definition을 유일한 원소로 하는 리스트를 값으로 사전에 추가
#F 함수 밖; 빈 사전 생성
#G “words”라는 이름의 사전을 인자로 함수 호출
#H {'box': ['fight']} 출력
#I “box”라는 키에 대한 값을 추가하기 위해 함수 호출
#J {'box': ['fight', 'container']} 출력
#K 다른 항목을 추가하기 위해 함수 호출
#L {'box': ['fight', 'container'], 'ox': ['animal']} 출력




################
## LISTING 28.2
################
songs = {"Wannabe": 1, "Roar": 1, "Let It Be": 5, "Red Corvette": 4}     #A

for s in songs.keys():               #B
    if songs[s] == 1:                #C
        songs.pop(s)                 #D
#A 노래 사전
#B 모든 키-값 쌍에 대해 루프 수행
#C 평점이 1이면…
#D … 그 노래를 제거


################
## LISTING 28.3
################
songs = [1, 1, 5, 4]               #A

for s in songs:                    #B
    if s == 1:                     #C
        songs.pop(s)               #D
print(songs)                       #E
#A 노래 평점 리스트
#B 모든 평점에 대해 루프를 돎
#C 평점이 1이면…
#D 그 노래를 제거
#E [1, 5, 4]를 출력


################
## LISTING 28.4
################
songs = [1, 1, 5, 4]               #A
songs_copy = songs.copy()          #B
songs = []                         #C
for s in songs_copy:               #D
    if s != 1:                     #E
        songs.append(s)            #F
print(songs)                       #G
#A 원래의 평점 리스트
#B 복사본 만듦
#C 원본 리스트를 빈 리스트로 설정
#D 모든 평점에 대해 루프 수행
#E 평점이 제거 대상이 아닌 경우라면…
#F … 원본 리스트에 그 평점을 추가
#G [5, 4]를 출력
