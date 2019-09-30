################
## LISTING 37.1
################
import tkinter                            #A
 
window = tkinter.Tk()                     #B
window.geometry("800x200")                #C
window.title("첫번째 GUI")                 #D
window.configure(background="grey")       #E
window.mainloop()                         #F
#A tkinter 라이브러리를 불러옴
#B 새 객체를 만들고 window라는 변수에 대입
#C 창 크기 변경
#D 창에 제목 추가
#E 창 배경색 변경
#F 프로그램 시작



################
## LISTING 37.2
################
import tkinter
window = tkinter.Tk()
window.geometry("800x200")
window.title("첫번째 GUI")
window.configure(background="grey")

red = tkinter.Button(window, text="빨강", bg="red")               #A
red.pack()                                                       #B

yellow = tkinter.Button(window, text="노랑", bg="yellow")
yellow.pack()

green = tkinter.Button(window, text="초록", bg="green")
green.pack()

textbox = tkinter.Entry(window)                           #C
textbox.pack()                                            #C

colorlabel = tkinter.Label(window, height="10", width="10")             #D
colorlabel.pack()                                                       #D

window.mainloop()
#A window을 부모로 빨간 배경에 “빨강”이라는 글씨가 적힌 버튼을 새로 만듦
#B 방금 정한 특성을 지닌 버튼을 창에 추가
#C 텍스트를 입력할 수 있는 박스를 만듦
#D 높이가 10인 레이블을 만듦




################
## LISTING 37.3
################
import tkinter

def change_color():                               #A
    window.configure(background="white")          #B

window = tkinter.Tk()
window.geometry("800x200")
window.title("첫번째 GUI")
window.configure(background="grey")

white = tkinter.Button(window, text="누르세요", command=change_color)      #C
white.pack()

window.mainloop()
#A 발생할 수 있는 이벤트를 표현하는 함수
#B 함수가 창의 배경 색을 바꿈
#C 어떤 동작과 연결된 버튼. command에 함수 이름을 지정해서 동작을 연결함



################
## LISTING 37.4
################
import tkinter
import time

def countdown():                                         #A
    countlabel.configure(background="white")             #B
    howlong = int(textbox.get())                         #C
    for i in range(howlong,0,-1):                        #D
        countlabel.configure(text=i)                     #E
        window.update()                                  #F
        time.sleep(1)                                    #G
    countlabel.configure(text="끝!")                   #H

window = tkinter.Tk()
window.geometry("800x600")
window.title("첫번쨰 GUI")
window.configure(background="grey")

lbl = tkinter.Label(window, text="몇 초를 카운트다운 하겠습니까?")          #I
lbl.pack()
textbox = tkinter.Entry(window)                                         #J
textbox.pack()
count = tkinter.Button(window, text="카운트다운!", command=countdown)     #K
count.pack()
countlabel = tkinter.Label(window, height="10", width="10")             #L
countlabel.pack()

window.mainloop()
#A 이벤트 핸들러 함수
#B 레이블의 색을 흰색으로 바꿈
#C 텍스트 박스의 값을 가져와서 int로 변환
#D 텍스트 박스에 입력한 수부터 0까지 내려가는 루프 시작
#E 레이블의 텍스트를 루프 변수의 값으로 설정
#F 윈도우를 갱신해서 변경한 레이블 값을 표시하게 만듦
#G time 라이브러리를 사용해 1초간 일시 중단
#H 값이 0이 되면 레이블 텍스트를 변경
#I 사용자에게 사용법을 알려주기 위한 레이블
#J 사용자에게서 수를 입력받기 위한 텍스트 박스
#K 카운트 다운을 시작하기 위한 버튼. 소스코드 맨 앞에서 정의한 함수를 버튼 command에 연결함
#L 카운트 다운되는 동안 변하는 숫자를 보여주는 레이블
