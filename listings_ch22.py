################
## LISTING 22.1
################
def 파리의_연인():                  #A
    정은 = "강태영"                 #B
    print(정은)                    #C

정은 = "위원장"                     #D
파리의_연인()                       #E
print(정은)                        #F
#A 함수 정의
#B 함수 안에 있는 정은이라는 변수의 값은 “강태영”임
#C 강태영 출력
#D 메인 프로그램에서 실행되는 첫번째 문장. 정은이라는 변수를 만들고 “위원장”으로 초기화
#E 함수 호출이 새 영역을 만들어내고 “강태영”을 출력. 그 후 함수가 None을 반환하면서 영역이 끝남
#F 위원장 출력



################
## LISTING 22.2
################
def e():
    v = 5
    print(v)        #A

v = 1
e()                 #B
#A 함수내에서 정의한 v를 사용
#B 함수 호출이 잘 작동함. 이때 함수 안에서 정의한 v를 사용




################
## LISTING 22.3
################
def f():
    print(v)       #A 

v = 1
f()                 #B
#A 영역 밖의 변수에 접근
#B 함수 호출이 잘 작동함. 전역 변수 v를 함수 f()에서 사용




################
## LISTING 22.4
################
def g():
    print(v+x)     #A 

v = 1
x = 2
g()                #B
#A 변수를 읽기만 함
#B 함수 호출이 잘 작동함. 전역변수 v와 x를 함수 g()에서 사용



################
## LISTING 22.5
################
def h():
    v += 5          #A

v = 1
h()                 #B
#A v를 정의하기 전에 함수 안에서 v에 대한 연산을 사용
#B 함수 호출하면 오류 발생함




################
## LISTING 22.6
################
def odd_or_even(num):              #A
    num = num%2                    #B
    if num == 1:
        return "odd"
    else:
        return "even"

num = 4                            #C
print(odd_or_even(num))            #D
odd_or_even(5)                     #E
#A 함수 정의는 num이라는 한 매개변수만 받음
#B 2로 num을 나눈 나머지
#C 전역(글로벌 영역) 변수
#D 함수를 호출하고, 그 반환 값을 출력
#E 함수를 호출하고 반환 값에 대해 아무 일도 하지 않음


################
## LISTING 22.7
################
def sing():
    def stop(line):                      #A
        print("STOP",line)
    stop("it's hammer time")             #B
    stop("in the name of love")          #B
    stop("hey, what's that sound")       #B
stop()                                   #C
sing()
#A sing() 안에 있는 함수 정의
#B sing()안에서 stop() 함수를 호출
#C 글로벌 영역 안에 stop()이 없기 때문에 오류가 발생함



################
## LISTING 22.8
################
def sandwich(kind_of_sandwich):           #A 
   print("--------")
   print(kind_of_sandwich ())             #B 
   print("--------")

def blt():
    my_blt = " 베이컨\n상추\n 토마토"
    return my_blt

def breakfast():
    my_ec = " 달걀\n 치즈"
    return my_ec
    
print(sandwich(blt))                 #C
#A kind_of_sandwich는 매개변수임
#B kind_of_sandwich 뒤에 괄호를 붙여서 함수 호출임을 표현함
#C 함수 이름(함수 객체 자체)만 사용함



################
## LISTING 22.9
################
def grumpy():                                      #A
    print("I am a grumpy cat:")
    def no_n_times(n):                             #B
        print("No", n,"times...")
        def no_m_more_times(m):                    #C
            print("...and no", m,"more times")
            for i in range(n+m):                   #D
                print("no")
        return no_m_more_times                     #E
    return no_n_times                              #F
    
grumpy()(4)(2)                                     #G
#A 함수 정의
#B 내포 함수 정의
#C 내포 함수 정의
#D no를 n + m번 출력하는 루프
#E no_n_times 함수는 no_m_more_times 함수를 반환
#F grumpy 함수는 no_n_times 함수를 반환
#G 메인 프로그램에 있는 함수 호출
