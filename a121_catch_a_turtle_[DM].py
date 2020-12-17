#-----import statements-----
import turtle as trtl
import random as rand
#colors and configs
color = "purple"
shape = "square"
pen = 3
score = 0

#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

abc = trtl.Turtle()
abc.pensize(pen)
abc.shape(shape)
abc.color(color)

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.pencolor(color)
score_writer.penup()
score_writer.goto(-100,-100)
score_writer.pendown()

#-----countdown writer-----
counter = trtl.Turtle()
counter.hideturtle()
counter.pencolor(color)
counter.penup()
counter.goto(-100,-150)
counter.pendown()

#-----game functions-----
def spot_clicked(x,y):

    global timer 
    if timer > 0:
        update_score()
        change_position()
    else:
        abc.hideturtle()

def change_position():
    abc.hideturtle()
    newxpos = rand.randint(0,200)
    newypos = rand.randint(0,125)
    abc.penup()
    abc.goto(newxpos,newypos)
    abc.pendown()
    abc.showturtle()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font = font_setup)     

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#---------events---------
abc.onclick(spot_clicked)

wn = trtl.Screen()
wn.bgcolor("lime")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()