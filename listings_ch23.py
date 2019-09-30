################
## LISTING 23.1
################
word = "bird\n"                            #A
print(word)                                #B
word = word.replace("\n", "")              #C
print(word)                                #D
#A 새줄 문자가 들어있는 문자열을 저장한 변수를 만듦
#B 출력하면 빈 줄이 한 줄 더 보임
#C 새줄 문자를 빈 문자열로 대치하고 그 결과를 같은 변수에 저장
#D 출력하면 빈 줄이 보이지 않음




################
## LISTING 23.2
################
def read_file(file):
    """                                                          #A
    file, 파일 객체                                               #A
    첫번째 줄부터 시작해서 매 두번째 줄들을 튜플에 넣는다              #A
    두번째 줄부터 시작해서 매 두번째 줄들을 다른 튜플에 넣는다          #A
    Returns 두 튜플로 이뤄진 튜플                                   #A
    """                                                          #A
    first_every_2 = ()                            #B
    second_every_2 = ()                           #B
    line_count = 0                                        #C
    for line in file:                                     #D
        stripped_line = line.replace("\n", "")            #E
        if line_count%2 == 0:                             #F
            first_every_2 += (stripped_line,)             #G
        elif line_count%2 == 1:                           #H
            second_every_2 += (stripped_line,)            #I
        line_count += 1                                   #J
    return (first_every_2, second_every_2)               #K
#A 둑스트링
#B 이름과 전화번호를 저장할 빈 튜플들
#C 줄 번호를 저장할 변수
#D 파일의 모든 줄에 대해 루프 수행
#E 새줄 문자 없앰
#F 홀수 번째에 있는 줄
#G 이름을 튜플에 추가
#H 짝수 번째에 있는 줄
#I 전화번호를 튜플에 추가
#J 줄 번호를 1증가시킴
#K 튜플의 튜플 반환


################
## LISTING 23.3
################
def sanitize(some_tuple):
    """ 
    phones, 문자열이 들있는 튜플
    튜플에 들어 있는 문자열에서 모든 대시, 공백, 괄호를 없앤다
    Returns 대시, 공백, 괄호를 없앤 문자열로 이뤄진 새 튜플
    """
    clean_string = ()                      #A
    for st in some_tuple:
        st = st.replace(" ", "")           #B
        st = st.replace("-", "")           #B
        st = st.replace("(", "")           #B
        st = st.replace(")", "")           #B
        clean_string += (st,)              #C
    return clean_string                    #D
#B 불필요한 문자를 빈 문자열로 바꿈
#A 빈 튜플
#C 정리한 전화번호를 튜플에 추가
#D 튜플을 반환
 


################
## LISTING 23.4
################
friends_file = open('friends.txt')             #A
(names, phones) = read_file(friends_file)      #B

print(names)                                      #C
print(phones)                                     #C
clean_phones = sanitize(phones)                   #D

print(clean_phones)                               #C
friends_file.close()                              #E
#A 파일 열기
#B 함수 호출
#C 함수가 반환한 내용을 사용자에게 표시
#D 함수가 잘 작동하는지 시험해보기
#E 파일 닫기



################
## LISTING 23.5
################
def get_unique_area_codes():    
    """ 
    Returns phones에 있는 지역 코드 목록(중복된 경우 1개만 포함)
    """
    area_codes = ()                               #A 
    for ph in phones:                             #B
        if ph[0:3] not in area_codes:             #C
            area_codes += (ph[0:3],)              #D

    return area_codes
#A 유일한 지역 코드를 저장하기 위한 튜플
#B 모든 지역 코드를 처리. phones 변수는 analyze_friends의 매개변수임
#C 지역 코드가 이미 들어있지는 않은지 검사
#D 유일한 지역코드 튜플 뒤에 지역 코드가 하나만 들어있는 튜플을 덧붙임



################
## LISTING 23.6
################
def get_states(some_areacodes):
    """
    some_areacodes, 지역 코드들이 들어있는 튜플
    Returns 지역 코드에 해당하는 주 이름들이 들어있는 튜플
    """
    states = ()
    for ac in some_areacodes:
        if ac not in all_areacodes:              #A
            states += ("BAD AREACODE",)
        else:
            index = all_areacodes.index(ac)       #B 
            states += (all_places[index],)        #C 
    return states
#A 사용자가 잘못된 지역번호를 입력함. all_areacodes 변수는 analyze_friends의 매개변수임
#B 튜플에서 지역 코드의 위치를 찾음
#C 지역 코드의 위치를 활용해 주 이름을 가져옴




################
## LISTING 23.7
################
def analyze_friends(names, phones, all_areacodes, all_places):
    """
    names, 친구 이름들이 들어있는 튜플
    phones, 친구 전화 번호(특수문자는 없앰)들이 들어있는 튜플
    all_areacodes, 지역 코드들이 들어있는 튜플
    all_places, 지역 코드에 대한 주 이름이 들어있는 튜플
    친구가 몇 명인지와 친구들의 전화번호가 속한 주 목록을 표시한다
    (이때 같은 주는 단 한번만 표시한다)
    """

    def get_unique_area_codes():    
        """ 
        Returns phones에 있는 지역 코드 목록(중복된 경우 1개만 포함)
        """
        area_codes = ()
        for ph in phones:
            if ph[0:3] not in area_codes:            
                area_codes += (ph[0:3],)

        return area_codes

    def get_states(some_areacodes):
        """
        some_areacodes, 지역 코드들이 들어있는 튜플
        Returns 지역 코드에 해당하는 주 이름들이 들어있는 튜플
        """
        states = ()
        for ac in some_areacodes:
            if ac not in all_areacodes:
                states += ("BAD AREACODE",)
            else:
                index = all_areacodes.index(ac)
                states += (all_places[index],)
        return states
    
    num_friends = len(names)                              #A 
    unique_area_codes = get_unique_area_codes()           #B 
    unique_states = get_states(unique_area_codes)         #C 
        
    print("You have", num_friends, "friends!")            #D 
    print("They live in", unique_states)          #E

                                                  #F
#A 유일한 지역 코드들만 남김
#B 유일한 지역 코드에 해당하는 주 이름을 가져옴
#C 친구 인원 수
#D 친구 수를 출력
#E 유일한 주 이름들을 찍음
#F 반환할 값이 없음


################
## LISTING 23.8
################
friends_file = open('friends.txt')                #A
(names, phones) = read_file(friends_file)         #B
areacodes_file = open('map_areacodes_states.txt') #A
(areacodes, states) = read_file(areacodes_file)   #B

clean_phones = sanitize(phones)                           #C
analyze_friends(names, clean_phones, areacodes, states)   #D

friends_file.close()                              #E
areacodes_file.close()                            #E
#A 프로그램과 같은 디렉터리에 있는 파일을 엶
#B 두 데이터 집합을 읽을 때 같은 함수를 활용
#C 전화번호 데이터를 정규화(정해진 형식에 따라 정리)
#D 대부분의 작업을 수행하는 함수를 호출
#E 파일을 닫음
