from tkinter import *
import random

GAME_HEIGHT=700
GAME_WIDTH=700

SPEED=200
SPACE_SIZE=50
BODY_PARTS=1

SNAKE_COLOR="#00FF00"
FOOD_COLOR="#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake() :
    def __init__(self):
        self.body_size=BODY_PARTS
        self.coordinates=[]
        self.squares=[]

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
            self.squares.append(square)

class  Food() :
    def __init__(self):

        x=random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y=random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE

        self.coordinates=[x,y]
        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food")

def nxt_Turn(snake,food):

    x,y=snake.coordinates[0]

    if direction=="up":
        y-=SPACE_SIZE
    elif direction=="down":
        y+=SPACE_SIZE
    elif direction=="left":
        x-=SPACE_SIZE
    elif direction=="right":
        x+=SPACE_SIZE

    snake.coordinates.insert(0,(x,y))

    square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)

    snake.squares.insert(0,square)

    if x==food.coordinates[0] and y==food.coordinates[1]:

        global score
        score+=1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")
        food=Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        windows.after(SPEED,nxt_Turn,snake,food)


def Change_Direction(new_direction):

    global direction

    if new_direction=='left':
        if direction!='right':
            direction=new_direction
    elif new_direction=='right':
        if direction!='left':
            direction=new_direction
    elif new_direction=='up':
        if direction!='down':
            direction = new_direction
    elif new_direction=='down':
        if direction!='up':
            direction=new_direction


def check_collisions(snake):

    x,y=snake.coordinates[0]

    if x<0 or x>=GAME_WIDTH:
        return True
    elif y<0 or y>=GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x==body_part[0] and y==body_part[1]:
            return True

    return False


def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,
                       font=('montserrat',70),text="GAME OVER", fill="red",tag="gameover")

windows=Tk()
windows.title("Snake Xe")
windows.resizable(False,False)

score=0
direction='down'

label=Label(windows,text="Your Score : {}".format(score),font=('montserrat',30))
label.pack()

canvas=Canvas(windows,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_HEIGHT)
canvas.pack()

windows.update()

window_width=windows.winfo_width()
window_height=windows.winfo_height()
screen_width=windows.winfo_screenwidth()
screen_height=windows.winfo_screenheight()

x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))

windows.geometry(f"{window_width}x{window_height}+{x}+{y}")

windows.bind('<Left>',lambda event:Change_Direction('left'))
windows.bind('<Right>',lambda event:Change_Direction('right'))
windows.bind('<Up>',lambda event:Change_Direction('up'))
windows.bind('<Down>',lambda event:Change_Direction('down'))

snake=Snake()
food=Food()

nxt_Turn(snake,food)

windows.mainloop()