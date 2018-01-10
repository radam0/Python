#Nikhil Vemula
#Feb 16 2016
#CS61002 Algorithm & Programming 1
#American flag in turtle.py


import turtle   #To use graphics



#WIKIPEDIA INFO

'''Hoist (width) of flag: A = 1.0

Fly (length) of flag: B = 1.9

Hoist (width) of Union: C = 0.5385 (7/13)

Fly (length) of Union: D = 0.76

E = F = 0.054

G = H = 0.063

Diameter of star: K = 0.0616

Width of stripe: L = 0.0769 (1/13)

'''


#function to determine rgb colors

def get_color(color):

    r=0

    b=0

    g=0

    if color=='red':

        r=1

        b=0

        c=0

    elif color=='green':

        r=0

        b=0

        g=1

    elif color=='blue':

        r=0

        b=1

        g=0

    elif color=='white':

        r=1

        b=1

        g=1

    elif color=='black':

        r=0

        b=0

        g=0

    return r,g,b


#function to draw rectangle

def draw_rectangle(length,height,color):

    turtle.up()

    turtle.speed(1000)

    r,g,b = get_color(color)

    turtle.color(r,g,b)

    turtle.begin_fill()

    turtle.setpos(-150,150)

    turtle.down()

    turtle.forward(length)

    turtle.right(90)

    turtle.forward(height)

    turtle.right(90)

    turtle.forward(length)

    turtle.right(90)

    turtle.forward(height)

    turtle.end_fill()



    starbox_height = height*0.5385

    starbox_width = (length*0.76)/2

    redStripes_height = float(round(height/13,1))



    newyPos = 150-redStripes_height

    for i in range(1,14):

        turtle.setpos(-150,newyPos)

        if i%2!=0:

            r,g,b = get_color('white')

            turtle.color(r,g,b)

            turtle.begin_fill()

            turtle.right(90)

            turtle.forward(length)

            turtle.right(90)

            turtle.forward(redStripes_height)

            turtle.right(90)

            turtle.forward(length)

            turtle.right(90)

            turtle.forward(redStripes_height)

            turtle.end_fill()

        else:

            r,g,b=get_color('red')

        newyPos = newyPos - redStripes_height



    r,g,b = get_color('blue')

    turtle.setpos(-150,150)

    turtle.color(r,g,b)

    turtle.begin_fill()

    turtle.up()

    turtle.right(90)

    turtle.forward(starbox_width)

    turtle.right(90)

    turtle.forward(starbox_height)

    turtle.right(90)

    turtle.forward(starbox_width)

    turtle.right(90)

    turtle.forward(starbox_height)

    turtle.end_fill()

    createstar()

    



def createstar():

    size =8

    defxpos = -135

    defypos = 135

    for j in range(0,5):

        defxpos = -135

        for i in range(0,6):

            draw_star(size,'white',defxpos,defypos)

            defxpos = defxpos+22

        defypos = defypos-21



    defxpos = -135

    defypos = 125.5

    for j in range(0,4):

        defxpos = -124

        for i in range(0,5):

            draw_star(size,'white',defxpos,defypos)

            defxpos = defxpos+22

        defypos = defypos-21

    turtle.up()

    turtle.goto(-200,200)

    

#function to draw a star

def draw_star(size,color,xpos,ypos):

    turtle.up()

    r,g,b = get_color(color)

    turtle.color(r,g,b)

    turtle.setpos(xpos,ypos)

    turtle.begin_fill()

    turtle.down()

    for i in range(0,5):

        turtle.forward(size)

        turtle.left(144)

    turtle.end_fill()

    

#function to draw a flag

def draw_flag(height):

    draw_rectangle(height*1.9,height,'red')



draw_flag(1.0*200)










 

