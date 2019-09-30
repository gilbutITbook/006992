################
## LISTING 29.1
################
def read_text(filename):
    """
    filename: string, 읽을 파일의 이름                      #A
    returns: string, 파일의 모든 내용이 들어 있음            #A
    """
    inFile = open(filename, 'r')                          #B
    line = inFile.read()                                  #C
    return line                                           #D

text = read_text("sonnet18.txt")                          #E
print(text)
#A 독문자열
#B 파일 이름을 가지고 파일을 여는 파이썬 함수
#C 파일의 모든 내용을 문자열로 읽어 오는 파이썬 함수
#D 문자열 반환
#E 함수 호출







################
## LISTING 29.2
################
import string                                      #A

def find_words(text):
    """
    text: string
    returns: list. 입력 문자열인 text에 들어있는 단어들이 들어 있다
    """
    text = text.replace("\n", " ")               #B
    for char in string.punctuation:              #C
        text = text.replace(char, "")            #D

    words = text.split(" ")                      #E
    return words                                 #F

words = find_words(text)                         #G
#A 문자열과 관련된 함수들을 가져온다
#B 새줄문자를 공백으로 바꾼다
#C string에 정의된 기호 문자들을 활용한다
#D 기호를 빈 문자열로 바꾼다(따라서 기호를 제거하는 효과가 있다)
#E 공백을 기준으로 문자열을 분리해 단어들로 이뤄진 리스트로 만든다
#F 단어의 리스트를 반환한다
#G 함수 호출



################
## LISTING 29.3
################
def frequencies(words):
    """
    words: list. 단어들이 들어있는 리스트
    returns: 입력으로 들어온 단어들의 빈도가 들어있는 사전
    """
    freq_dict = {}                              #A

    for word in words:                          #B
        if word in freq_dict:                   #C
            freq_dict[word] += 1                #D
        else:                                   #E
            freq_dict[word] = 1                 #F
       return freq_dict                         #G

freq_dict = frequencies(words)                  #H
#A 빈 사전으로 초기화
#B 리스트에 있는 각 단어를 처리
#C 단어가 사전에 이미 들어 있다면…
#D 그 단어의 빈도에 1을 더해 사전 항목 갱신
#E 단어가 사전에 들어있지 않다면
#F 그 단어와 빈도 1을 사전에 새로 추가
#G 사전 반환
#H 함수 호출




################
## LISTING 29.4
################
def calculate_similarity(dict1, dict2):
    """
    dict1: 한 문서의 단어 빈도 사전
    dict2: 다른 문서의 단어 빈도 사전
    returns: float, 두 문서의 유사도를 표현하는 값(1이면 같음. 0이면 완전히 다름)
    """
    diff = 0
    total = 0

    for word in dict1.keys():                               #A
        if word in dict2.keys():                            #B
            diff += abs(dict1[word] - dict2[word])          #C
        else:                                               #D
            diff += dict1[word]                             #E

    for word in dict2.keys():                                #F
        if word not in dict1.keys():                         #G
            diff += dict2[word]                              #H

    total = sum(dict1.values()) + sum(dict2.values())        #I
    difference = diff / total                                #J
    similar = 1.0 - difference                               #K

    return round(similar, 2)                                 #L
#A 한 사전에 들어있는 모든 단어에 대해 이터레이션
#B 단어가 양 사전 모두에 들어있음
#C 빈도 차이를 더함
#D 단어가 반대쪽 사전에는 들어있지 않음
#E 단어의 빈도를 더함
#F 나머지 사전의 모든 단어에 대해 이터레이션
#G 양 사전에 모두 포함된 단어는 이미 검사했으므로, 반대쪽 사전에 들어있지 않는 단어만 검사
#H 단어의 빈도를 더함
#I 양 사전의 모든 단어 수를 더함
#J 빈도 차이의 합을 전체 단어 수로 나눔
#K 1에서 difference를 뺌
#L 소수점 이하 2자리까지 반올림하고 0부터 1 사이의 점수를 반환



################
## LISTING 29.5
################
text_1 = read_text("sonnet18.txt")
text_2 = read_text("sonnet19.txt")
words_1 = find_words(text_1)
words_2 = find_words(text_2)
freq_dict_1 = frequencies(words_1)
freq_dict_2 = frequencies(words_2) 
print(calculate_similarity(freq_dict_1, freq_dict_2))
