################
## LISTING 21.1
################
def take_attendance(classroom_roaster, who_is_here):             #A
    """                                                          #B
    classroom_roaster, tuple                                     #B
    who_is_here, tuple                                           #B
    
    classroom_roaster(출석부)에 있는 모든 사람이                    #B
    who_is_here(현재 교실에 있는 사람 목록)에 들어있는지 검사한다      #B
    학생이 who_is_here에 있는 경우에만 그 이름을 출력한다             #B
    
    Returns "출석 부르기 끝"
    """                                                  #B
    for kid in classroom_roaster:                        #C
        if kid in who_is_here:                           #D
            print(kid)                                   #E
    return "출석 부르기 끝"                                #F
#A 함수 정의
#B 함수 명세(독스트링)
#C 출석부에 있는 모든 학생에 대해 루프를 반복
#D kid가 who_is_here 튜플 안에 들어있는지 검사
#E 교실에 있는 학생 이름을 출력
#F 문자열을 반환





################
## LISTING 21.2
################
def get_word_length(word1, word2):             #A
    word = word1+word2                         #B
    return len(word)                           #C
    print("이 문자열은 절대로 출력되지 않습니다")   #D
#A 매개변수를 둘 받는 함수 정의
#B 두 매개변수를 이어 붙임
#C 두 문자열을 연결한 문자열 길이 반환
#D return 문 뒤에 있는 문장은 실행되지 않음



################
## LISTING 21.3
################
def word_length(word1, word2):                 #A
    word = word1+word2                         #A
    return len(word)                           #A
    print("이 문자열은 절대로 출력되지 않습니다")  #A

length1 = word_length("Rob", "Banks")            #B
length2 = word_length("Barbie", "Kenn")          #B
length3 = word_length("Holly", "Jolley")         #B

print("One name is", length1, "letters long.")                   #C
print("Another name is", length2, "letters long.")               #C
print("The final name is", length3, "letters long.")             #C
#A word_length 함수 정의
#B 각 줄은 여러 다른 입력으로 함수를 호출하고, 함수가 반환한 결과를 변수에 저장함
#C 각 줄은 변수를 출력




################
## LISTING 21.4
################
def add_sub(n1, n2):
    add = n1 + n2
    sub = n1 - n2
    return (add, sub)      #A

(a, b) = add_sub(3,4)      #B
#A 덧셈과 뺄셈 결과가 담긴 튜플을 반환
#B 결과를 튜플에 저장



################
## LISTING 21.5
################
def say_name(kid):         #A
    print(kid)             #B 


def show_kid(kid):         #C 
    return kid             #D 

say_name("재인")            #E
show_kid("정숙")            #F
print(say_name("명박"))     #G
print(show_kid("근혜"))     #H
#A 아이 이름을 문자열로 받음
#B 명시적으로 아무것도 반환하지 않으면 파이썬이 None을 반환함
#C 아이 이름을 문자열로 받음
#D 문자열 반환
#E 콘솔에 “재인”을 출력
#F 콘솔에 아무 것도 출력하지 않음
#G 명박을 출력한 다음 None을 콘솔에 출력
#H 콘솔에 근혜를 출력



