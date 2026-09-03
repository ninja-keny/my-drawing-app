# add the fixis you made to the small screen to the mediuem and big screen and then take it to github and just code for fun
# big disclaimer if your seeing this on git hub i am just coding for fun the readability is not the best and it was hard coded to if you are trying to analize the code it will take long
# report any bugs thanks
run = True
while run: 
 bigness = input("how big do you want the scrren to be for a small screen type small for a medium screen type medium for a large screen type large: ")
 if bigness == "small":
  width2 = 500
  height2 = 500
  run = False
 elif bigness == "medium":
  width2 = 800
  height2 = 800
  run = False
 elif bigness == "large":
   width2 = 1500
   height2 = 800
   run = False
 else:
   print("please type small, medium, or large")

# turtles
import turtle
redo = turtle.Turtle()
exit = turtle.Turtle()
b_green = turtle.Turtle()
b_menu = turtle.Turtle()
b_fill = turtle.Turtle()
e_fill = turtle.Turtle()
b_red = turtle.Turtle()
b_black = turtle.Turtle()
b_white = turtle.Turtle()
small = turtle.Turtle()
red = turtle.Turtle()
white = turtle.Turtle()
black = turtle.Turtle()
color_write = turtle.Turtle()
circle_color = turtle.Turtle()
lift = turtle.Turtle()
down = turtle.Turtle()
color_menu = turtle.Turtle()
screen = turtle.Screen()
green = turtle.Turtle()
blue = turtle.Turtle()
b_blue = turtle.Turtle()
size_menu = turtle.Turtle()
size_exit = turtle.Turtle()

# varibles
already_drawn = False
b_menu_on = 1
tap = False
t_size = 0
m_open = False
value = 0
value2 = 0
size_menu_on = 1
button_click = False
b_color = "white"
moved = 0
movedx = [0]
movedy = [0]
color = "black"
undo = False
hitbox_size = 50
controll = 0
checker = 0

#screen
screen.setup(width=width2,height = height2)

small.speed(0)
small.hideturtle()
small.color("white")

size_menu.penup()
size_menu.speed(0)
size_menu.hideturtle()
size_menu.color("grey")

b_fill.penup()
b_fill.speed(0)
b_fill.hideturtle()
b_fill.color("green")

redo.speed(0)
redo.hideturtle()
redo.color("red")
redo.penup()

b_menu.speed(0)
b_menu.penup()
b_menu.hideturtle()
b_menu.color("grey")

b_blue.color("blue")
b_blue.speed(0)

e_fill.penup()
e_fill.speed(0)
e_fill.hideturtle()
e_fill.color("purple")

size_menu.hideturtle()
size_menu.speed(0)

size_exit.hideturtle()
size_exit.speed(0)

exit.speed(0)
exit.hideturtle()

# background red turtle set up
b_red.color("red")
b_red.speed(0)
b_red.penup()
b_red.hideturtle()

b_white.color("white")
b_white.speed(0)
b_white.penup()
b_white.hideturtle()

b_black.color("black")
b_black.speed(0)
b_black.penup()
b_black.hideturtle()
b_black.pensize(10)

green.color("green")
green.speed(0)
green.hideturtle()

# black turtle set up
black.color("black")
black.speed(0)
black.penup()
black.hideturtle()

white.color("white")
white.speed(0)
white.penup()
white.hideturtle()
# red turtle set up
red.color("red")
red.speed(0)
red.hideturtle()
red.penup()

blue.color("blue")
blue.speed(0)
blue.hideturtle()

# color_write turtle set up
color_write.speed(0)
color_write.penup()
color_write.hideturtle()


#lift turtle setup
lift.speed(0)
lift.penup()
lift.hideturtle()

#down turtle setup
down.speed(0)
down.penup()
down.hideturtle()

#circle_color turtle setup
circle_color.speed(0)
circle_color.penup()
circle_color.hideturtle()

color_menu.speed(0)
color_menu.hideturtle()

b_green.hideturtle()
b_menu.hideturtle()
b_fill.hideturtle()
e_fill.hideturtle()
b_red.hideturtle()
b_black.hideturtle()
b_white.hideturtle()
red.hideturtle()
white.hideturtle
black.hideturtle()
color_write.hideturtle()
circle_color.hideturtle()
lift.hideturtle()
down.hideturtle()
color_menu.hideturtle()
green.hideturtle()
blue.hideturtle()
b_blue.hideturtle()


# placing the lift turtle and down turtle
if bigness == "small":
 lift.goto(-200,-200)
 down.goto(-124,-200)
 b_menu.goto(190,-200)
 size_menu.goto(190,200)
 redo.goto(96,-200)
 circle_color.goto(-200,200)
 b_fill.goto(-46,-200)
 e_fill.goto(20,-200)

elif bigness == "medium": 
 lift.goto(-150,-300)
 down.goto(-75,-300)
 b_menu.goto(350,-300)
 size_menu.goto(350,350)
 redo.goto(150,-300)
 circle_color.goto(-350,350)
 b_fill.goto(0,-300)
 e_fill.goto(75,-300)

elif bigness == "large":
 lift.goto(-500,-300)
 down.goto(-400,-300)
 b_menu.goto(450,-300)
 redo.goto(-100,-300) 
 size_menu.goto(700,350)
 circle_color.goto(-700,350)
 b_fill.goto(-300,-300)
 e_fill.goto(-200,-300)

# color circle
circle_color.pendown()
circle_color.color("grey")
circle_color.dot(50)

b_menu.dot(50)
exit.pensize(5)
size_menu.dot(50)

turtle.begin_fill()
turtle.shape("turtle")
turtle.speed(0)
def clicked(x,y):
  # global varibles
  global checker
  global hitbox_size
  global controll
  global undo
  global tap
  global t_size
  global m_open
  global value
  global button_click
  global value2
  global b_color
  global b_menu_on
  global movedy
  global movedx
  global moved
  global color
  global already_drawn
  global size_menu_on
  
  if size_exit.distance(x,y) < hitbox_size:
   if size_menu_on == 2:
    size_menu_on += 1
    size_exit.clear()
    size_menu.clear()
    size_menu.dot(50)
    small.clear()
    button_click = True

  if size_menu.distance(x,y) < 50:
   if size_menu_on == 1:
    size_menu_on +=1
    if bigness == "small":
     size_menu.setheading(0)
     size_menu.penup()
     size_menu.pensize(10)
     size_menu.begin_fill()
     size_menu.color("black")
     size_menu.goto(230,230)
     size_menu.pendown()
     size_menu.right(90)
     size_menu.forward(380)
     size_menu.right(90)
     size_menu.forward(120)
     size_menu.right(90)
     size_menu.forward(380)
     size_menu.right(90)
     size_menu.forward(120)
     size_menu.color("grey")
     size_menu.end_fill()
     size_menu.penup()
     size_menu.goto(200,200) 

     size_exit.setheading(0)
     size_exit.penup()
     size_exit.goto(230,200)
     size_exit.pendown()
     size_exit.pensize(8)
     size_exit.backward(115)
     size_exit.penup()
     size_exit.forward(3)
     size_exit.pendown()
     size_exit.write("size menu", font=("Arial", 12, "bold"))
     size_exit.goto(200,200)
     size_exit.left(90)
     size_exit.forward(30)
     size_exit.pensize(5)
     size_exit.right(135)
     size_exit.forward(45)
     size_exit.setheading(0)
     size_exit.penup()
     size_exit.backward(35)
     size_exit.pendown()
     size_exit.left(45)
     size_exit.forward(45)
     size_exit.backward(27.5) 
     hitbox_size = 30

     small.penup()
     small.goto(135,160)
     small.dot(35)
     small.backward(9)
     small.color("black")
     small.write("small", font=("Arial", 7, "bold"))
     small.color("white")
     small.forward(9)
    elif bigness == "medium":
     size_menu.setheading(0)
     size_menu.penup()
     size_menu.pensize(12)
     size_menu.begin_fill()
     size_menu.color("black")
     size_menu.goto(380,380)
     size_menu.pendown()
     size_menu.right(90)
     size_menu.forward(630)
     size_menu.right(90)
     size_menu.forward(200)
     size_menu.right(90)
     size_menu.forward(630)
     size_menu.right(90)
     size_menu.forward(200)
     size_menu.color("grey")
     size_menu.end_fill()
     size_menu.penup()
     size_menu.goto(350,350) 

     size_exit.setheading(0)
     size_exit.penup()
     size_exit.goto(380,320)
     size_exit.pendown()
     size_exit.pensize(10)
     size_exit.backward(200)
     size_exit.penup()
     size_exit.forward(3)
     size_exit.pendown()
     size_exit.write("size menu", font=("Arial", 20, "bold"))
     size_exit.goto(325,320)
     size_exit.left(90)
     size_exit.forward(60)
     size_exit.right(137)
     size_exit.forward(68)
     size_exit.setheading(0)
     size_exit.penup()
     size_exit.backward(40)
     size_exit.pendown()
     size_exit.left(45)
     size_exit.forward(70)
     size_exit.backward(35.5)
     hitbox_size = 50

     small.penup()
     small.goto(215,270)
     small.dot(50)
     small.backward(20)
     small.color("black")
     small.write("small", font=("Arial", 9, "bold"))
     small.color("white")
     small.forward(20)
    elif bigness == "large":
     size_menu.setheading(0)
     size_menu.penup()
     size_menu.pensize(10)
     size_menu.begin_fill()
     size_menu.color("black")
     size_menu.goto(730,380)
     size_menu.pendown()
     size_menu.right(90)
     size_menu.forward(720)
     size_menu.right(90)
     size_menu.forward(220)
     size_menu.right(90)
     size_menu.forward(720)
     size_menu.right(90)
     size_menu.forward(220)
     size_menu.color("grey")
     size_menu.end_fill()
     size_menu.penup()
     size_menu.goto(700,350)

     size_exit.setheading(0)
     size_exit.penup()
     size_exit.goto(730,320)
     size_exit.pendown()
     size_exit.pensize(10)
     size_exit.backward(215)
     size_exit.penup()
     size_exit.forward(3)
     size_exit.pendown()
     size_exit.write("size menu", font=("Arial", 20, "bold"))
     size_exit.goto(670,320)
     size_exit.left(90)
     size_exit.forward(60)
     size_exit.right(137)
     size_exit.forward(72)
     size_exit.setheading(0)
     size_exit.penup()
     size_exit.backward(40)
     size_exit.pendown()
     size_exit.left(45)
     size_exit.forward(70)
     size_exit.backward(35.5)
     hitbox_size = 50

     small.penup()
     small.goto(545,270)
     small.dot(50)
     small.backward(20)
     small.color("black")
     small.write("small", font=("Arial", 9, "bold"))
     small.color("white")
     small.forward(20)
    button_click = True

  if redo.distance(x,y) < 30:
   if b_menu_on == 2:
    try:
     if moved > -1:
      moved -= 1
      turtle.color(b_color) 
      undo = True
      turtle.goto(movedx[moved-controll],movedy[moved-controll])
      turtle.color(color)
     else:
      turtle.clear()
      controll = 0
      movedy = [0]
      movedx = [0]
      moved = 0
    except:
     pass
    
    button_click = True


  if small.distance(x,y) < hitbox_size:
   if size_menu_on == 2:
    turtle.pensize(5)
    button_click = True
  if e_fill.distance(x,y) < 30:
   if b_menu_on == 2:
    turtle.end_fill()
    button_click = True

  if b_fill.distance(x,y) < 30:
    if b_menu_on == 2:
      turtle.begin_fill()
      button_click = True
  
  # if the penup button/ lift turtle clicked wich will make the pen up
  if lift.distance(x,y) < 30:
   if b_menu_on == 2:
    turtle.penup()
    button_click = True

  # if the pendown/ down button clicked which will make the pen down
  if down.distance(x,y) < 30:
   if b_menu_on == 2:
    turtle.pendown()
    button_click = True

  if color_write.distance(x,y) < 30:
          if m_open == True:
           button_click = True
           b_black.clear()
           red.clear()
           b_red.clear()
           b_white.clear()
           white.clear()
           green.clear()
           black.clear()
           color_write.clear()
           color_menu.clear()
           blue.clear()
           b_blue.clear()
           m_open = False
  if exit.distance(x,y) < 40:
   if b_menu_on == 2:
     b_menu_on += 1
     b_menu.clear()
     redo.clear()
     lift.clear()
     down.clear()
     exit.clear()
     e_fill.clear()
     b_fill.clear()
     b_menu.penup()
     if bigness =="small":
      b_menu.goto(190,-200)
     elif bigness == "medium":
      b_menu.goto(350,-300)
     elif bigness == "large":
      b_menu.goto(450,-300)
     b_menu.pendown()
     b_menu.dot(50)
     button_click = True
  if b_menu.distance(x,y) < 40:
   if b_menu_on == 1:
    b_menu_on += 1

    if bigness == "small":
     b_menu.setheading(0)
     b_menu.goto(230,-200) 
     b_menu.pendown()
     b_menu.pensize(8)
     b_menu.begin_fill()
     b_menu.color("black")
     b_menu.left(90)
     b_menu.forward(40)
     b_menu.left(90)
     b_menu.forward(460)
     b_menu.left(90)
     b_menu.forward(80)
     b_menu.left(90)
     b_menu.forward(460)
     b_menu.left(90)
     b_menu.forward(80)
     b_menu.color("grey")
     b_menu.end_fill()
     lift.pendown()
     lift.color("blue")
     lift.dot(50)
     lift.backward(20)
     lift.color("black")
     lift.write("pen up", font=("Arial", 10, "bold"))   
     lift.penup()
     lift.forward(20)
     down.pendown()
     down.color("orange")
     down.dot(50)
     down.backward(20)
     down.color("black")
     down.write("pen down", font=("Arial", 7, "bold"))  
     down.color("orange")
     down.forward(20)
     down.color("black")
     e_fill.pendown()
     e_fill.color("purple")
     e_fill.dot(50)
     e_fill.backward(20)
     e_fill.color("black")
     e_fill.write("end fill", font=("Arial", 8, "bold"))
     e_fill.penup()
     e_fill.forward(20)
     b_fill.pendown()
     b_fill.color("green")
     b_fill.dot(50)
     b_fill.backward(20)
     b_fill.color("black")
     b_fill.write("begin fill", font=("Arial", 7, "bold"))
     b_fill.penup()
     b_fill.forward(20)
     redo.dot(50)
     redo.backward(20)
     redo.color("black")
     redo.write("undo", font=("Arial", 9, "bold"))
     redo.color("red")
     redo.forward(20)
    elif bigness == "medium":
     b_menu.setheading(0)
     b_menu.goto(390,-300)
     b_menu.pendown()
     b_menu.pensize(8)
     b_menu.begin_fill()
     b_menu.color("black")
     b_menu.left(90)
     b_menu.forward(40)
     b_menu.left(90)
     b_menu.forward(570)
     b_menu.left(90)
     b_menu.forward(80)
     b_menu.left(90)
     b_menu.forward(570)
     b_menu.left(90)
     b_menu.forward(80)
     b_menu.color("grey")
     b_menu.end_fill()
     lift.pendown()
     lift.color("blue")
     lift.dot(50)
     lift.backward(20)
     lift.color("black")
     lift.write("pen up", font=("Arial", 10, "bold"))   
     lift.penup()
     lift.forward(20)
     down.pendown()
     down.color("orange")
     down.dot(50)
     down.backward(20)
     down.color("black")
     down.write("pen down", font=("Arial", 7, "bold"))  
     down.color("orange")
     down.forward(20)
     down.color("black")
     e_fill.pendown()
     e_fill.color("purple")
     e_fill.dot(50)
     e_fill.backward(20)
     e_fill.color("black")
     e_fill.write("end fill", font=("Arial", 8, "bold"))
     e_fill.penup()
     e_fill.forward(20)
     b_fill.pendown()
     b_fill.color("green")
     b_fill.dot(50)
     b_fill.backward(20)
     b_fill.color("black")
     b_fill.write("begin fill", font=("Arial", 7, "bold"))
     b_fill.penup()
     b_fill.forward(20)
     redo.dot(50)
     redo.backward(20)
     redo.color("black")
     redo.write("undo", font=("Arial", 9, "bold"))
     redo.color("red")
     redo.forward(20)
    elif bigness == "large":
     b_menu.setheading(0)
     b_menu.goto(500,-300)
     b_menu.pendown()
     b_menu.pensize(8)
     b_menu.begin_fill()
     b_menu.color("black")
     b_menu.left(90)
     b_menu.forward(40)
     b_menu.left(90)
     b_menu.forward(1030)
     b_menu.left(90)
     b_menu.forward(80)
     b_menu.left(90)
     b_menu.forward(1030)
     b_menu.left(90)
     b_menu.forward(80)
     b_menu.color("grey")
     b_menu.end_fill()
     lift.pendown()
     lift.color("blue")
     lift.dot(50)
     lift.backward(20)
     lift.color("black")
     lift.write("pen up", font=("Arial", 10, "bold")) 
     lift.penup()
     lift.forward(20)
     down.pendown()
     down.color("orange")
     down.dot(50)
     down.backward(20)
     down.color("black")
     down.write("pen down", font=("Arial", 7, "bold"))  
     down.color("orange")
     down.forward(25)
     down.color("black")
     e_fill.pendown()
     e_fill.color("purple")
     e_fill.dot(50)
     e_fill.backward(20)
     e_fill.color("black")
     e_fill.write("end fill", font=("Arial", 8, "bold"))
     e_fill.penup()
     e_fill.forward(20)
     b_fill.pendown()
     b_fill.color("green")
     b_fill.dot(50)
     b_fill.backward(20)
     b_fill.color("black")
     b_fill.write("begin fill", font=("Arial", 7, "bold"))
     b_fill.penup()
     b_fill.forward(20)
     redo.dot(50)
     redo.backward(20)
     redo.color("black")
     redo.write("undo", font=("Arial", 9, "bold"))
     redo.color("red")
     redo.forward(20)
    exit.penup()
    exit.goto(b_menu.xcor(),b_menu.ycor())
    exit.pendown()
    exit.setheading(0)
    exit.left(180)
    exit.forward(50)
    exit.left(90)
    exit.forward(50)
    exit.left(90)
    exit.forward(50)
    exit.left(90)
    exit.forward(50)
    exit.left(135)
    exit.forward(70)
    exit.setheading(0)
    exit.penup()
    exit.forward(45)
    exit.pendown()
    exit.left(135)
    exit.forward(60)
    exit.penup()
    exit.backward(35)
    button_click = True
   elif b_menu_on == 3:
     b_menu_on = 1



  
  # wich will open a menu
  if circle_color.distance(x,y) < 30:
    if m_open == False:
      button_click = True
      m_open = True
      color_menu.color("black")
      color_menu.penup()
      color_menu.goto(circle_color.xcor()-37.5, circle_color.ycor()+30)
      color_menu.setheading(0)
      color_menu.pensize(10)
      color_menu.pendown()
      color_menu.begin_fill()
      #making the menu box with the turtle
      if bigness == "small":
       for i in range(2):
        color_menu.forward(120)
        color_menu.right(90)
        color_menu.forward(380)
        color_menu.right(90)
       t_size = 12

      elif bigness == "medium":
       for i in range(2):
        color_menu.forward(200)
        color_menu.right(90)
        color_menu.forward(700)
        color_menu.right(90)
       t_size = 18
 
      elif bigness == "large":
       for i in range(2):
        color_menu.forward(200)
        color_menu.right(90)
        color_menu.forward(700)
        color_menu.right(90)
       t_size = 18

      # once the menu box is made the color_menu turtle fills it with the color grey
      color_menu.color("grey")
      color_menu.end_fill()
      color_write.color("black")
      
      # drawing the x box so the player can leave the menu and drawing the menu title
      if bigness == "small":
       color_write.setheading(0)
       color_write.pensize(10)
       color_write.penup()
       color_write.goto(circle_color.xcor()-30, circle_color.ycor())
       color_write.write("color menu", font=("Arial", t_size, "bold"))
       color_write.pendown()
       color_write.forward(110)
       color_write.pensize(5)
       for i in range(4):
        color_write.left(90)
        color_write.forward(25)
       color_write.left(135)
       color_write.forward(35)
       color_write.setheading(0)
       color_write.forward(25)
       color_write.right(135)
       color_write.forward(30)
       color_write.backward(5)

      else:
       color_write.pensize(10)
       color_write.penup()
       color_write.goto(circle_color.xcor()-30, circle_color.ycor()-20)
       color_write.setheading(0)
       color_write.write("color menu", font=("Arial", t_size, "bold"))
       color_write.pendown()
       color_write.forward(140)
       for i in range(4):
        color_write.forward(50)
        color_write.left(90)
       color_write.left(40)
       color_write.forward(60)
       color_write.penup()
       color_write.right(45)
       color_write.backward(40)
       color_write.pendown()
       color_write.right(40)
       color_write.forward(50)
       color_write.backward(15)
      if  bigness == "small":
       red.goto(circle_color.xcor()-15, circle_color.ycor()-30)
       red.pendown()
       red.dot(30)
       value = 30
       black.goto(circle_color.xcor()+20, circle_color.ycor()-30)
       black.pendown()
       black.dot(30)
       white.goto(circle_color.xcor()+60, circle_color.ycor()-30)
       white.dot(30)
       green.penup()
       green.goto(circle_color.xcor()-15, circle_color.ycor()-80)
       green.pendown()
       green.dot(30)
       blue.penup()
       blue.goto(circle_color.xcor()+20, circle_color.ycor()-80)
       blue.pendown()
       blue.dot(30)
       value2 = 20
      else:
       red.goto(circle_color.xcor() , circle_color.ycor()-80)
       red.pendown()
       red.dot(50)
       value = 50
       black.goto(circle_color.xcor()+65, circle_color.ycor()-80)
       black.pendown()
       black.dot(50)
       white.goto(circle_color.xcor()+125, circle_color.ycor()-80)
       white.pendown()
       white.dot(50)
       green.penup()
       green.goto(circle_color.xcor(), circle_color.ycor()-160)
       green.pendown()
       green.dot(50)
       blue.penup()
       blue.goto(circle_color.xcor()+65, circle_color.ycor()-160)
       blue.pendown()
       blue.dot(50)
       value2 = 40

      if bigness == "small":
        b_black.pensize(9)
        b_black.color("black")
        b_black.penup()
        b_black.goto(-230,20)
        b_black.write("background colors", font=("Arial",10,"bold"))
        b_black.pendown()
        b_black.forward(110)
        b_black.penup()
        b_red.goto(-217,-20)
        b_red.color("red")
        b_red.dot(30)
        b_black.goto(-180,-20)
        b_black.dot(30)
        b_white.goto(-140,-20)
        b_white.dot(30)
        b_blue.penup()
        b_blue.goto(-180,-70)
        b_blue.pendown()
        b_blue.dot(30)
        valu2 = 20
      else:
       b_black.pensize(10)
       b_black.color("black")
       b_black.penup()
       b_black.goto(red.xcor()-30,black.ycor()-250)
       b_black.write("backround colors", font=("Arial",16,"bold"))
       b_black.pendown()
       b_black.forward(190)
       b_black.penup()
       b_red.goto(red.xcor(),red.ycor()-300)
       b_red.color("red")
       b_red.dot(50)
       b_black.goto(black.xcor(),black.ycor()-300)
       b_black.dot(50)
       b_white.penup()
       b_white.goto(white.xcor(),black.ycor()-300)
       b_white.dot(50)
       b_blue.penup()
       b_blue.goto(blue.xcor(),black.ycor()-370)
       b_blue.dot(50)
       valu2 = 40

    else:
      button_click = False

  if b_white.distance(x,y) < value2:
    if m_open == True:
      button_click = True
      if b_color != "white":
         turtle.clear()
         b_color = "white"
         screen.bgcolor("white")

  if b_blue.distance(x,y) < value2:
    if m_open == True:
     button_click = True
     if b_color != "blue":
       b_color = "blue"
       turtle.clear()
       screen.bgcolor(b_color)

  if b_red.distance(x,y) < value2:
    if m_open == True:
     button_click = True
     if b_color != "red":
       b_color = "red"
       turtle.clear()
       screen.bgcolor(b_color)


  if b_black.distance(x,y) < value2:
    button_click = True
    if m_open == True:
     if b_color != "black":
      turtle.clear()
      b_color = "black"
      screen.bgcolor("black")

  if green.distance(x,y) < value:
   if m_open == True:
    color = "green"
    turtle.color("green")
    button_click = True

  if blue.distance(x,y) < value:
   if m_open == True:
    color = "blue"
    turtle.color("blue")
    button_click = True

  # and if the red circle is clicked while the menu is open it changes the turtle color
  if red.distance(x,y) < value:
      if m_open == True:
         color = "red"
         turtle.color("red")
         button_click = True


  if white.distance(x,y) < value:
    if m_open == True:
     color = "white"
     turtle.color("white")
     button_click = True

  # if the black circle is clicked it makes the circle black
  if black.distance(x,y) < value:
   if m_open == True:
     color = "black"
     turtle.color("black") 
     button_click = True

  if size_menu_on == 3:
   size_menu_on = 1
  # if no buttons where clicked it make the turtle goto a position
  if button_click == False:
   if undo == True:
    moved = len(movedx)-1
    controll = 1
    undo = False
   else:
    controll = 0

   if bigness == "small":
     if m_open == True and b_menu_on == 2 and y > -150 and x > -130:
      checker = 1
      already_drawn = True
      tap = True
      movedx.append(x)       
      movedy.append(y)
      moved += 1
      turtle.goto(x,y)
      print("you clicked at")
      print(int(x),int(y))
      tap = False 

     if checker != 1:
      if m_open == True and x  > -130:
       if b_menu_on != 2:
        if tap == False:
         already_drawn = True
         tap = True
         print("1")
         movedx.append(x)
         movedy.append(y)
         moved += 1
         turtle.goto(x,y)
         print("you clicked at")
         print(int(x),int(y))
         tap = False 

     if checker != 1:
      if b_menu_on == 2 and y > -150:
       if m_open == False:
        if tap == False:
         if already_drawn == False:
          tap = True
          movedx.append(x)
          movedy.append(y)
          moved += 1
          turtle.goto(x,y)
          print("you clicked at")
          print(int(x),int(y))
          tap = False
       else:
         already_drawn = False
       
     if b_menu_on != 2 and m_open == False:
       if tap == False:
        tap = True
        movedx.append(x)
        movedy.append(y)
        moved += 1
        turtle.goto(x,y)
        print("you clicked at")
        print(int(x),int(y))
        tap = False
         

   if bigness == "medium":
     if m_open == True and b_menu_on == 2 and y > -252 and x > -205:
      checker = 1
      already_drawn = True
      tap = True
      movedx.append(x)       
      movedy.append(y)
      moved += 1
      turtle.goto(x,y)
      print("you clicked at")
      print(int(x),int(y))
      tap = False 

     if checker != 1:
      if m_open == True and b_menu_on != 2: 
       if x > -205:  
        if tap == False:
         tap = True
         movedx.append(x)
         movedy.append(y)
         moved += 1
         turtle.goto(x,y)
         print("you clicked at")
         print(int(x),int(y))
         tap = False 
         already_drawn = True
       else:
        already_drawn = True

     if checker != 1:
      if b_menu_on == 2 and m_open == False:
       if y > -252:
        if tap == False:
         if already_drawn == False:
          tap = True
          movedx.append(x)
          movedy.append(y)
          moved += 1
          turtle.goto(x,y)
          print("you clicked at")
          print(int(x),int(y))
          tap = False
         else:
          already_drawn = False

      if b_menu_on != 2 and m_open == False:
       if tap == False:
        tap = True
        movedx.append(x)
        movedy.append(y)
        moved += 1
        turtle.goto(x,y)
        print("you clicked at")
        print(int(x),int(y))
        tap = False

   if bigness == "large":
       if m_open == True and b_menu_on == 2 and y > -252 and x > -550:
        checker = 1
        already_drawn = True
        tap = True
        movedx.append(x)       
        movedy.append(y)
        moved += 1
        turtle.goto(x,y)
        print("you clicked at")
        print(int(x),int(y))
        tap = False 

       if checker != 1:
        if m_open == True and b_menu_on != 2:
          if x > -550:  
           if tap == False:
            tap = True
            movedx.append(x)
            movedy.append(y)
            moved += 1
            turtle.goto(x,y)
            print("you clicked at")
            print(int(x),int(y))
            tap = False 
            already_drawn = True


       if checker != 1:
        if b_menu_on == 2 and m_open == False:
         if y > -252:
          if tap == False:
            tap = True
            movedx.append(x)
            movedy.append(y)
            moved += 1
            turtle.goto(x,y)
            print("you clicked at")
            print(int(x),int(y))
            tap = False

        if b_menu_on != 2 and m_open == False:
         if tap == False:
          tap = True
          movedx.append(x)
          movedy.append(y)
          moved += 1
          turtle.goto(x,y)
          print("you clicked at")
          print(int(x),int(y))
          tap = False
  checker = 0
  button_click = False 
 

    

screen.onscreenclick(clicked)
turtle.mainloop() 