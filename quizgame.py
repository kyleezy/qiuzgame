import pgzrun
WIDTH=800
HEIGHT=600
TITLE="quiz"
msgbox=Rect(0,0,800,100)
qesbox=Rect(0,100,600,150)
timbox=Rect(620,100,160,150)
def draw():
    screen.fill("black")
    screen.draw.filled_rect(msgbox,"black")
    screen.draw.filled_rect(qesbox,"blue")
    screen.draw.filled_rect(timbox,"red")


    











pgzrun.go()