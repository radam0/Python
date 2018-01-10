
#Nikhil Vemula
#cs61002:Alogrithm and Programming 1
#05/03/2016
#project2.py



import turtle

# It consists a minimum of seven classes

class Shape(object):
    def __init__(self, pencolor="black", pensize=1):
        self.pencolor = pencolor
        self.pensize = pensize

class Line(Shape):
    """ this class contains the definitions for creating a line """
    def __init__(self,start=(0.0, 0.0),end=(0.0, 0.0),pencolor="black",pensize=1):
        Shape.__init__(self,pencolor,pensize)
        self.start = start
        self.end = end

    def __str__(self):
        return "Line from:{},to:{}".format(self.start,self.end)

    def draw(self,pen):
        pen.pensize(self.pensize)
        pen.pencolor(self.pencolor)
        pen.up()
        pen.goto(self.start)
        pen.down()
        pen.goto(self.end)
        
# It draws the rectangle
class Rectangle(Shape):
    """ this class contains the definitions for creating a Rectangle """
    def __init__(self,pos=(0.0, 0.0),size=20,fillcolor="white",pencolor="black",pensize=1):
        Shape.__init__(self,pencolor,pensize)
        self.pos = pos
        x,y = pos
        self.size = size
        offset = size/3.0
        self.side_lines = [Line((x,y),(x,y-size)),
                           Line((x,y-size),(x+size,y-size)),
                           Line((x+size,y-size),(x+size,y)),
                           Line((x+size,y),(x,y))
                           ]
        self.fillcolor = fillcolor

    def __str__(self):
        return "Rectangle pos:{},size:{}".format(self.pos,self.size)

    def draw(self,pen):
        pen.penup()
        pen.goto(self.pos)
        pen.pendown()
        pen.fillcolor(self.fillcolor)
        pen.begin_fill()
        for l in self.side_lines:
            l.draw(pen)
        pen.end_fill()
        
# Drawing the hat
    def draw_hat_line(self,pen):
        size = self.size
        x,y = self.pos
        self.side_hat_lines = [Line((x,y),(x,y+size)),
                       Line((x,y),(x+150,y)),
                       Line((x+150,y),(x+150,y+size)),
                       Line((x+150,y+size),(x,y+size))
                       ]
        pen.penup()
        pen.goto(self.pos)
        pen.pendown()
        pen.fillcolor(self.fillcolor)
        pen.begin_fill()
        for l in self.side_hat_lines:
            l.draw(pen)
        pen.end_fill()

# Drawing the snowman body
class Circle(Shape):
    """ this class contains the definitions for creating a Circle """
    def __init__(self,pos=(0.0, 0.0),radius=20,fillcolor="white",pencolor="black",pensize=1):
        Shape.__init__(self,pencolor,pensize)
        self.pos = pos
        self.radius = radius
        self.fillcolor = fillcolor
        self.pencolor=pencolor
        self.pensize=pensize

    def __str__():
        return "Circle pos:{},radius:{}".format(self.pos,self.radius)

    def draw(self,pen):
        pen.color(self.pencolor)
        pen.pensize(self.pensize)
        pen.penup()
        x,y = self.pos
        pen.goto(x,y)
        pen.pendown()
        pen.fillcolor(self.fillcolor)
        pen.begin_fill()
        pen.circle(self.radius)
        pen.end_fill()
        pen.penup()
        pass

# Drawing the hat for snowlady
class Triangle(Shape):
    """ this class contains the definitions for creating a Triangle """
    def __init__(self,pos=(0.0,0.0),fillcolor='yellow',pencolor="black",pensize=1, angle1=120, angle2=120, angle3=120, length1=80, length2=80, length3=80):
        Shape.__init__(self,pencolor,pensize)
        self.pos = pos
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        self.length1 = length1
        self.length2 = length2
        self.length3 = length3
        self.fillcolor=fillcolor

    def __str__():
        return "Traingle pos:{},angle1:{},angle2:{},angle3:{}".format(self.pos,self.angle1,self.angle2,self.angle3)

    def draw(self,pen):
        pen.penup()
        pen.goto(self.pos)
        pen.pendown()
        pen.fillcolor(self.fillcolor)
        pen.begin_fill()
        pen.forward(self.length1)
        pen.left(self.angle1)
        pen.forward(self.length2)
        pen.left(self.angle2)
        pen.forward(self.length3)
        pen.left(self.angle3)
        pen.end_fill()

class Snow_person(object):
    """ this class contains the definitions for creating a Snow_person """
    def __init__(self,pos=(0.0,0.0)):
        self.pos = pos
        pass

    def top_circle(self,pen, *args):# first circle of snow person
        x,y = self.pos
        '''draws the top circle'''
        bc = Circle((x,y-100),40)
        bc.draw(pen)

    def middle_circle(self,pen, *args): #second circle of snow person
        x,y = self.pos
        '''draws the middle circle'''
        mc = Circle((x,y-220),60)
        mc.draw(pen)

    def bottom_circle(self,pen, *args): #second circle of snow person
        x,y = self.pos
        '''draws the bottom circle'''
        lc = Circle((x,y-380),80)
        lc.draw(pen)

    def draweyes(self,pen,color):
        x,y = self.pos
        mc = Circle((x-20,y-65),5,color)
        mc.draw(pen)

        x,y = self.pos
        mc = Circle((x+20,y-65),5,color)
        mc.draw(pen)

# This contains all the definitions for the class
class Snow_man(Snow_person):
    """ this class contains the definitions for creating a Snow_man """
    def __init__(self,pos=(0.0,0.0)):
        Snow_person.__init__(self,pos)
        self.givenpos = pos

    def draw(self,pen):
        self.top_circle(pen)
        self.middle_circle(pen)
        self.bottom_circle(pen)
        self.draweyes(pen,'blue')
        self.draw_hat(pen)
        self.drawbuttons(pen)
        self.drawarms(pen)
        self.drawmouth(pen)

    def draw_hat(self,pen):   # drawing the hat
        x,y = self.givenpos
        mc = Rectangle((x-35,y+30),70,'brown')
        mc.draw(pen)

        mc = Rectangle((x-70,y-50),10,'brown')
        mc.draw_hat_line(pen)

    def drawbuttons(self,pen):  #drawing the buttons
        x,y = self.pos
        mb=Circle((x,y-150),7,"Grey")
        mb.draw(pen)

        x,y = self.pos
        mb=Circle((x,y-185),7,"Grey")
        mb.draw(pen)
        
        x,y = self.pos
        mb=Circle((x,y-285),7,"Grey")
        mb.draw(pen)

        x,y = self.pos
        mb=Circle((x,y-325),7,"Grey")
        mb.draw(pen)

    def drawarms(self,pen):  # drawing the arms
        x,y=self.pos
        dh=Line((x-50,y-150),(x-150,y-140),"brown",5)
        dh.draw(pen)

        x,y=self.pos
        dh=Line((x+50,y-150),(x+140,y-100),"brown",5)
        dh.draw(pen)

    def drawmouth(self,pen): # drawing the mouth
        x,y=self.pos
        dh=Line((x-10,y-85),(x-20,y-80),"red",5)
        dh.draw(pen)

        x,y=self.pos
        dh=Line((x+10,y-85),(x-10,y-85),"Red",5)
        dh.draw(pen)

        x,y=self.pos
        dh=Line((x+10,y-85),(x+20,y-80),"Red",5)
        dh.draw(pen)

# This contains definitions for snowlady
class Snow_lady(Snow_person):
    """ this class contains the definitions for creating a Snow_lady """
    
    def __init__(self,pos=(0.0,0.0)):
            Snow_person.__init__(self,pos)
            self.givenpos = pos

    def draw(self,pen):
        self.top_circle(pen)
        self.middle_circle(pen)
        self.bottom_circle(pen)
        self.draweyes(pen,'green')
        self.draw_hat(pen)
        self.drawbuttons(pen)
        self.drawarms(pen)
        self.drawmouth(pen)
        self.drawhair(pen)

    def draw_hat(self,pen):  # drawing the hat
        x,y = self.givenpos
        mc = Triangle((x-40,y-40),'yellow')
        mc.draw(pen)

    def drawbuttons(self,pen): # drawing the buttons
        x,y = self.pos
        mb=Circle((x,y-150),8,"yellow")
        mb.draw(pen)

        x,y = self.pos
        mb=Circle((x,y-185),8,"purple")
        mb.draw(pen)
        
        x,y = self.pos
        mb=Circle((x,y-285),8,"yellow")
        mb.draw(pen)

        x,y = self.pos
        mb=Circle((x,y-325),8,"purple")
        mb.draw(pen)

    def drawarms(self,pen):  # drawing the arms
        x,y=self.pos
        dh=Line((x-50,y-150),(x-150,y-140),"brown",5)
        dh.draw(pen)

        x,y=self.pos
        dh=Line((x+50,y-150),(x+140,y-190),"brown",5)
        dh.draw(pen)

        x,y=self.pos
        dh=Line((x+140,y-190),(x+60,y-250),"brown",5)
        dh.draw(pen)

    def drawhair(self,pen):  #drawing the hair
        x,y=self.pos
        dh=Line((x-30,y-42),(x-45,y-75),"brown",5)
        dh.draw(pen)

        x,y=self.pos
        dh=Line((x-35,y-42),(x-55,y-85),"brown",5)
        dh.draw(pen)

        x,y=self.pos
        dh=Line((x+30,y-42),(x+45,y-75),"brown",5)
        dh.draw(pen)

        x,y=self.pos
        dh=Line((x+35,y-42),(x+55,y-85),"brown",5)
        dh.draw(pen)

    def drawmouth(self,pen): # drawing the mouth
         x,y=self.pos
         dh=Line((x-10,y-85),(x-20,y-80),"Red",5)
         dh.draw(pen)

         x,y=self.pos
         dh=Line((x+10,y-85),(x-10,y-85),"Red",5)
         dh.draw(pen)

         x,y=self.pos
         dh=Line((x+10,y-85),(x+20,y-80),"Red",5)
         dh.draw(pen)

         x,y = self.pos
         mb=Circle((x,y-90),6,"red")
         mb.draw(pen)

def main():
    canvas = turtle.Screen()
    canvas.setup(800, 600)
    pen = turtle.Turtle()
    pen.speed(100)
    snowman = Snow_man((-150.0,200.0))
    snowman.draw(pen)
    snowlady = Snow_lady((150.0,200.0))
    snowlady.draw(pen)
    pen.hideturtle()
    #canvas.exitonclick()
main()
