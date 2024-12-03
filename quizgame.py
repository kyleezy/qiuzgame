import pgzrun
WIDTH=800
HEIGHT=600
TITLE="quiz"
msgbox=Rect(0,0,800,100)
qesbox=Rect(0,100,600,150)
timbox=Rect(620,100,160,150)
box1=Rect(0,260,280,180)
box2=Rect(320,260,280,180)
def draw():
    screen.fill("black")
    screen.draw.filled_rect(msgbox,"black")
    screen.draw.filled_rect(qesbox,"blue")
    screen.draw.filled_rect(timbox,"red")
    screen.draw.filled_rect(box1,"yellow")
    screen.draw.filled_rect(box2,"yellow")
    











pgzrun.go()