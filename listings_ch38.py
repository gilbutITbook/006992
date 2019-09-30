################
## LISTING 38.1
################
import tkinter 
window = tkinter.Tk()
window.geometry("800x800")
window.title("태그!")
canvas = tkinter.Canvas(window)           #A
canvas.pack(expand=1, fill='both')        #B
#A 플레이어의 말을 그릴 캔버스 위젯
#B 창 크기에 변해도 그에 맞춰 캔버스가 창 전체를 차지하도록 캔버스 위치를 지정



################
## LISTING 38.2
################
import random
class Player(object):
    def __init__(self, canvas, color):            #A
        self.color = color                        #B
        size = random.randint(1,100)              #C
        x1 = random.randint(100,700)              #D
        y1 = random.randint(100,700)              #E
        x2 = x1+size                              #F
        y2 = y1+size                              #G
        self.coords = [x1, y1, x2, y2]            #H
        self.piece = canvas.create_rectangle(self.coords)        #I
        canvas.itemconfig(self.piece, fill=color)                #J
#A 모양을 더할 캔버스와 모양을 표현할 색을 데이터 속성으로 저장하는 객체를 위한 초기화 메소드
#B 객체의 데이터 속성으로 color 설정
#C 1이상 100 미만의 정수를 플레이어 말 크기로 정함
#D 플레이어 말의 좌상단 좌표의 x 값을 정해진 범위에서 선택
#E 플레이어 말의 좌상단 좌표의 y 값을 정해진 범위에서 선택
#F 플레이어 말의 우하단 좌표의 x 값
#G 플레이어 말의 우하단 좌표의 y 값
#H 모양을 표시할 좌표를 리스트로 만들고 객체의 데이터 속성으로 저장
#I 플레이어의 말을 캔버스상의 직사각형으로 설정. 이때 앞에서 계산한 좌표를 사용
#J 앞 줄에서 모양을 저장한 self.piece라는 변수를 사용해 플레이어의 말을 어떤 색으로 표시할지 지정함



################
## LISTING 38.3
################
def handle_key(event):                    #A
    if event.char == 'w' :                #B
        player1.move("u")                 #C
    if event.char == 's' :
        player1.move("d")
    if event.char == 'a' :
        player1.move("l")
    if event.char == 'd' :
        player1.move("r")
    if event.char == 'i' :                 #D
        player2.move("u")                  #E
    if event.char == 'k' :
        player2.move("d")
    if event.char == 'j' :
        player2.move("l")
    if event.char == 'l' :
        player2.move("r")
          
window = tkinter.Tk()
window.geometry("800x800")
window.title("태그!")
canvas = tkinter.Canvas(window)
canvas.pack(expand=1, fill='both')

player1 = Player(canvas, "yellow")
player2 = Player(canvas, "blue")
canvas.bind_all('<Key>', handle_key)           #F
#A 이벤트 핸들러 함수
#B 이벤트에서 눌린 키가 W인지 검사
#C move는 Player 클래스에 정의된 메소드. 그 메소드를 호출해서 모양을 위로 이동
#D 이벤트에서 눌린 키가 I인지 검사
#E move는 Player 클래스에 정의된 메소드. 다른 플레이어에 대해 그 메소드를 호출해서 모양을 위로 이동
#F 캔버스 키 눌림 이벤트는 모두 handle_key 함수가 처리


################
## LISTING 38.4
################
class Player(object):
    def __init__(self, canvas, color):
        size = random.randint(1,100)
        x1 = random.randint(100,700)
        y1 = random.randint(100,700)
        x2 = x1+size
        y2 = y1+size
        self.color = color
        self.coords = [x1, y1, x2, y2]
        self.piece = canvas.create_rectangle(self.coords, tags=color)
        canvas.itemconfig(self.piece, fill=color)

    def move(self, direction):                           #A
        if direction == 'u':                             #B
            self.coords[1] -= 10                         #C
            self.coords[3] -= 10                         #C
            canvas.coords(self.piece, self.coords)       #D
        if direction == 'd':
            self.coords[1] += 10
            self.coords[3] += 10
            canvas.coords(self.piece, self.coords)
        if direction == 'l':
            self.coords[0] -= 10
            self.coords[2] -= 10
            canvas.coords(self.piece, self.coords)
        if direction == 'r':
            self.coords[0] += 10
            self.coords[2] += 10
            canvas.coords(self.piece, self.coords)
#A 'u', 'd', 'l', 'r' 방향 중 한쪽으로 모양을 움직이는 메소드
#B 네가지 가능한 입력('u', 'd', 'l', 'r') 중 하나인 경우 입력에 따라 다른 동작 수행
#C 위로 움직일 경우 coords 리스트의 y1과 y2 값을 10 감소시킴
#D self.piece가 가리키는 직사각형의 좌표 변경


################
## LISTING 38.5
################
def handle_key(event):
    # 리스트 38.3의 기존 키 이벤트 처리 로직부분 생략
    yellow_xy = canvas.bbox(1)                                          #A
    overlapping = canvas.find_overlapping(
                   yellow_xy[0],yellow_xy[1],yellow_xy[2],yellow_xy[3]) #B
    if 2 in overlapping:                                                #C
        canvas.create_text(100,100,font=("Arial",20),text="Tag!")       #D
#A 모양 중 하나를 둘러싼 바운딩 박스의 좌표 구함
#B 바운딩 박스와 겹치는 모양의 ID를 모두 찾기
#C 겹치는 ID 들 중에 다른 사용자가 조종하는 모양의 ID가 들어 있는지 검사
#D 캔버스에 텍스트 더하기
