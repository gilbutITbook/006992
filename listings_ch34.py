################
## LISTING 34.1
################
class Player(object):
    """ 플레이어 """
    def __init__(self, name):
        """ 이름을 설정하고, 손에는 아무 카드도 가지고 있지 않는다 """
        self.hand = []                      #A
        self.name = name                    #B
    def get_name(self):                     #C
        """ 플레이어 이름을 반환한다 """
        return self.name                    #C
#A 빈 리스트로 손에 든 카드를 설정
#B Player 객체를 만들 때 전달받은 문자열로 이름을 설정
#C 플레이어의 이름을 반환하는 메소드


################
## LISTING 34.2
################
class Player(object):
    """" 플레이어 """
    # 리스트 41.에 나왔던 메소드들 생략
    def add_card_to_hand(self, card):              #A
        """ card, 문자열
            플레이어의 손에 정상적인 카드를 추가한다 """
        if card != None:
            self.hand.append(card)                  #A
    def remove_card_from_hand(self, card):          #B
        """ card, 문자열
            플레이어의 손에서 카드를 제거한다 """
        self.hand.remove(card)                       #B
    def hand_size(self):                             #C
        """ 플레이어의 손에 있는 카드 개수를 반환한다 """
        return len(self.hand)                        #C
#A 손에 카드를 추가하면 리스트에 카드를 추가함. 다만 카드가 올바른 카드인 경우에만 추가함
#B 손에서 카드를 제거하려면 리스트에서 카드를 찾아서 그 카드를 제거
#C 손에 들고 있는 카드의 개수는 리스트의 원소 개수




################
## LISTING 34.3
################
class CardDeck(object):
    """ 스페이드, 하트, 다이아몬드, 클럽 2부터 9까지로 구성된 덱 """
    def __init__(self):
        """ 가능한 모든 카드들이 들어있는 덱
            카드를 "2H"와(하트 2) 같은 문자열로 표현한다 """
        hearts = "2H,3H,4H,5H,6H,7H,8H,9H"               #A
        diamonds = "2D,3D,4D,5D,6D,7D,8D,9D"             #A
        spades = "2S,3S,4S,5S,6S,7S,8S,9S"               #A
        clubs = "2C,3C,4C,5C,6C,7C,8C,9C"                #A
        self.deck = hearts.split(',')+diamonds.split(',')  +  \
                    spades.split(',')+clubs.split(',')     #B
#A 덱 안에 들어갈 수 있는 모든 카드들을 표현하는 문자열을 만듦
#B 긴 문자열을 콤마를 기준으로 분할해서 각 카드를 구하고, 그 모든 카드(문자열)를 리스트에 넣음






################
## LISTING 34.4
################
import random

class CardDeck(object):
    """ 스페이드, 하트, 다이아몬드, 클럽 2부터 9까지로 구성된 덱 """
    def __init__(self):
        """ 가능한 모든 카드들이 들어있는 덱
            카드를 "2H"와(하트 2) 같은 문자열로 표현한다 """
        hearts = "2H,3H,4H,5H,6H,7H,8H,9H"
        diamonds = "2D,3D,4D,5D,6D,7D,8D,9D"
        spades = "2S,3S,4S,5S,6S,7S,8S,9S"
        clubs = "2C,3C,4C,5C,6C,7C,8C,9C"
        self.deck = hearts.split(',')+diamonds.split(',')        \
                    + spades.split(',')+clubs.split(',')
    def get_card(self):
        """ 임의의 카드(문자열)를 하나 반환한다.
        덱에 카드가 없는 경우에는 `None`을 반환한다  """
        if len(self.deck) < 1:                    #A
            return None                           #A
        card = random.choice(self.deck)           #B
        self.deck.remove(card)                    #C
        return card                               #D
    def compare_cards(self, card1, card2):
        """ 다음 규칙에 따라 더 센 카드를 반환한다.
        (1) 숫자가 더 큰 카드가 더 세다. 하지만 숫자가 같다면,
        (2) 스페이드 > 하트 > 다이아몬드 > 클럽 순으로 더 세다 """
        if card1[0] > card2[0]:                    #E
            return card1                           #E
        elif card1[0] < card2[0]:                  #F
            return card2                           #F
        elif card1[1] > card2[1]:                  #G
            return card1                           #G
        else:                                      #G
            return card2                           #G
#A deck에 카드가 없으면 None을 반환
#B deck 리스트에서 임의의 카드를 하나 고름
#C deck 리스트에서 카드를 제거
#D 카드 값(문자열)을 반환
#5 카드의 숫자를 비교해서 첫번째 카드가 더 크면 첫번째 카드를 반환
#6 카드의 숫자를 비교해서 두번째 카드가 더 크면 두번째 카드를 반환
#7 카드의 숫자가 같으면 모양을 비교


################
## LISTING 34.5
################
name1 = input("이름을 입력해 주세요. 플레이어 1: ")  #A
player1 = Player(name1)                           #B

name2 = input("이름을 입력해 주세요. 플레이어 2: ")
player2 = Player(name2)

deck = CardDeck()                                 #C
#A 플레이어 1의 이름을 사용자로부터 입력받음
#B 새 Player 객체를 만듦
#C 새 CardDeck 객체를 만듦

################
## LISTING 34.6
################
name1 = input("이름을 입력해 주세요. 플레이어 1: ")
player1 = Player(name1)

name2 = input("이름을 입력해 주세요. 플레이어 2: ")
player2 = Player(name2)
deck = CardDeck()

while True:
    player1_card = deck.get_card()
    player2_card = deck.get_card()
    player1.add_card_to_hand(player1_card)
    player2.add_card_to_hand(player2_card)
    if player1_card == None or player2_card == None:                       #A
        print("게임 오버. 덱에 카드가 없습니다.")
        print(name1, ": 최종 카드수 ", player1.hand_size())
        print(name2, ": 최종 카드수 ", player2.hand_size())
        print("승자는?")
        if player1.hand_size() > player2.hand_size():                      #B
            print(name2, " 승리!")
        elif player1.hand_size() < player2.hand_size():                    #C
            print(name1, " 승리!")
        else:                                                              #D
            print("비겼습니다!")
        break                                                              #E
    else:                                                                  #F
        print(name1, ": ", player1_card)
        print(name2, ": ", player2_card)
        if deck.compare_cards(player1_card,player2_card)==player1_card:    #G
            player1.remove_card_from_hand(player1_card)                    #H
            player2.add_card_to_hand(player1_card)                         #I
        else:
            player2.remove_card_from_hand(player2_card)
            player1.add_card_to_hand(player2_card)

#A 두 플레이어 중 한 사람이라도 카드가 없으면 게임을 끝냄
#B 손에 든 카드의 개수를 비교해서, 더 적은 카드를 가진 player2가 승리
#C 손에 든 카드의 개수를 비교해서, 더 적은 카드를 가진 player1이 승리
#D 두 사람의 카드 수가 같으므로 비김
#E 둘 중 한 사람이 승리하거나, 비긴 경우 break로 while 루프를 나감
#F 손에 비교할 카드가 으므로 게임을 계속함
#G 두 플레이어의 카드를 비교. 더 높은 카드가 반환됨
#H player1이 더 센 카드를 가지고 있으므로 player2에게 그 카드를 넘김
#I player1이 더 센 카드를 가지고 있으므로 player1의 손에서 그 카드를 제거
