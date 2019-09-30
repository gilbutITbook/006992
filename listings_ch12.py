################
## LISTING 12.1
################
print("Welcome to the Mashup Game!")
name1 = input("Enter one full name (FIRST LAST): ")              #A
name2 = input("Enter another full name (FIRST LAST): ")          #A
#A 사용자에게 원하는 형식으로 정보를 입력하라고 요청





################
## LISTING 12.2
################
space = name1.find(" ")                    #A
name1_first = name1[0:space]               #B
name1_last = name1[space+1:len(name1)]     #C
space = name2.find(" ")                    #D
name2_first = name2[0:space]               #D
name2_last = name2[space+1:len(name2)]     #D
#A 공백 문자의 인덱스를 얻어서 저장. 공백 문자로 이름과 성을 구분
#B 전체 이름 시작부터 공백 문자까지(공백은 제외) 모든 문자를 가져와서 이름으로 저장
#C 공백 바로 다음 문자부터 전체 이름 끝까지 모든 문자를 가져와서 성으로 저장
#D 두번째 이름에 대해 같은 처리를 반복




################
## LISTING 12.3
################
len_name1_first = len(name1_first)                #A
len_name2_first = len(name2_first)                #A
len_name1_last = len(name1_last)                  #A
len_name2_last = len(name2_last)                  #A
index_name1_first = int(len_name1_first/2)                #B
index_name2_first = int(len_name2_first/2)                #B
index_name1_last = int(len_name1_last/2)                  #B
index_name2_last = int(len_name2_last/2)                  #B

lefthalf_name1_first = name1_first[0:index_name1_first]                  #C
righthalf_name1_first = name1_first[index_name1_first:len_name1_first]   #D
lefthalf_name2_first = name2_first[0:index_name2_first]
righthalf_name2_first = name2_first[index_name2_first:len_name2_first]

lefthalf_name1_last = name1_last[0:index_name1_last]
righthalf_name1_last = name1_last[index_name1_last:len_name1_last]
lefthalf_name2_last = name2_last[0:index_name2_last]
righthalf_name2_last = name2_last[index_name2_last:len_name2_last]
#A 입력에서 얻어온 이름과 성의 길이를 저장
#B 길이를 반으로 나눈 값을 정수로 타입 변환하면 소수점 이하를 버림하면서 중간 인덱스를 정수로 계산할 수 있음
#C 앞쪽 절반은 이름의 시작부터 중간 인덱스까지
#D 뒤쪽 절반은 중간 인덱스부터 이름의 끝까지




################
## LISTING 12.4
################
#A
newname1_first = lefthalf_name1_first.capitalize() + \
righthalf_name2_first.lower()                 #B
newname1_last = lefthalf_name1_last.capitalize() +  \
righthalf_name2_last.lower()

newname2_first = lefthalf_name2_first.capitalize() +  \
righthalf_name1_first.lower()
newname2_last = lefthalf_name2_last.capitalize() +  \
righthalf_name1_last.lower()

print("All done! Here are two possibilities, pick the one you like best!")
print(newname1_first, newname1_last)       #C
print(newname2_first, newname2_last)       #C
#A 앞쪽 절반에 대해, 첫 글자를 대문자로 나머지를 소문자로 만듦
#B 뒤쪽 절반 전체를 소문자로 만듦
#C 사용자에게 새 이름을 두 가지 보여줌

