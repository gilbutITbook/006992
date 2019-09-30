################
## LISTING 19.1
################
words = """art
hue
ink
oil
pen
wax
clay
draw
film
form
kiln
line
tone
tube
wood
batik
brush
carve
chalk
color
craft
easel
erase
frame
gesso
glass
glaze
image
latex
liner
media
mixed
model
mural
paint
paper
photo
print
quill
quilt
ruler
scale
shade
stone
style
tools
video
wheel
artist
bridge
canvas
chisel
crayon
create
depict
design
enamel
eraser
fresco
hammer
marble
marker
medium
mobile
mosaic
museum
pastel
pencil
poster
pounce
roller
sculpt
sketch
vellum
visual
acrylic
artwork
cartoon
carving
casting
collage
compass
drawing
engrave
etching
exhibit
gallery
gilding
gouache
painter
palette
pigment
portray
pottery
primary
realism
solvent
stained
stencil
tempera
textile
tsquare
varnish
woodcut
abstract
airbrush
artistic
blending
ceramics
charcoal
contrast
critique
decorate
graffiti
graphite
hatching
maquette
marbling
painting
portrait
printing
quilting
sculptor
seascape
template
animation
cloisonne
decoupage
encaustic
engraving
landscape
porcelain
portfolio
sculpture
secondary
stippling
undertone
assemblage
brightness
creativity
decorative
exhibition
illustrate
lithograph
paintbrush
photograph
proportion
sketchbook
turpentine
watercolor
waterscape
calligraphy
composition
masterpiece
perspective
architecture
glassblowing
illustration
installation
stonecutting
crosshatching
"""
tiles = "hijklmnop"

all_valid_words = ()       #B
start = 0                  #C
end = 0                    #D
found_words = ()           #E
#A 올바른 단어들을 큰 문자열로 저장한다
#B 모든 올바른 단어들을 저장하기 위한 빈 튜플
#C 검색중인 단어의 시작 위치 인덱스를 초기화한다
#D 검색중인 단어의 끝 위치 인덱스를 초기화한다
#E 타일로 만들 수 있는 단어들을 저장하기 위한 빈 튜플




################
## LISTING 19.2
################
for char in words:                                                 #A
    if char == "\n":                                               #B
        all_valid_words = all_valid_words + (words[start:end],)    #C
        start = end + 1                                            #D
        end = end +1                                               #D
    else:
        end = end + 1                                              #E
#A 모든 문자를 가져오면서 루프를 돈다
#B 문자가 새줄문자인지 검사한다
#C 모든 올바른 단어가 들어있는 튜플 뒤에 단어가 하나만 들어있는 튜플을 덧붙인다
#D start와 end가 다음 단어의 시작을 가리키게 만든다
#E end가 다음 글자를 가리키게 만든다


################
## LISTING 19.3
################
for word in all_valid_words:                                     #A
    tiles_left = tiles                                           #B
    for letter in word:                                          #C
        if letter not in tiles_left:                             #D
            break                                                #D
        else:
            index = tiles_left.find(letter)                      #E
            tiles_left = tiles_left[:index]+tiles_left[index+1:] #F
    if len(word) == len(tiles)-len(tiles_left):                  #G
        found_words = found_words + (word,)                      #H
print(found_words)
#A 모든 올바른 단어들을 살펴본다
#B tiles_left는 타일 중복을 처리한다
#C 올바른 단어의 모든 문자를 처리한다
#D tiles_left 안에 문자가 없으면 루프를 중단한다
#E tiles_left에서 문자 위치를 찾는다
#F 찾은 문자를 없앤 새 tiles_left를 만든다
#G 타일로 단어를 만들 수 있었는지 검사한다
#H found_words에 단어를 추가한다
