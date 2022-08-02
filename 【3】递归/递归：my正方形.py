
import turtle
t = turtle.Turtle()

def square(degree, points):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'orange']
    drawsquare(points,colormap[degree])
    if degree > 0:
        square(degree-1,{'rl':points['rl'],
                         'rr':getMid(points['rl'],points['rr']),
                         'lr':getMid(points['rl'],points['lr']),
                         'll':getMid(points['rl'],points['ll'])})
        # square(degree-1,{'ll':points['ll'],
        #                  'rl':getMid(points['ll'],points['rl']),
        #                  'rr':getMid(points['ll'],points['rr']),
        #                  'lr':getMid(points['ll'],points['lr'])})
        square(degree-1,{'lr':points['lr'],
                         'rl':getMid(points['rl'],points['lr']),
                         'rr':getMid(points['rr'],points['lr']),
                         'll':getMid(points['ll'],points['lr'])})
        # square(degree-1,{'rr':points['rr'],
        #                  'rl':getMid(points['rl'],points['rr']),
        #                  'lr':getMid(points['rr'],points['lr']),
        #                  'll':getMid(points['rr'],points['ll'])})

def drawsquare(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['rl'])
    t.pendown()
    t.begin_fill()
    t.goto(points['ll'])
    t.goto(points['lr'])
    t.goto(points['rr'])
    t.goto(points['rl'])
    t.end_fill()

def getMid(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

points = {'ll':(-200,-200),
          'rl':(200,-200),
          'rr':(200,200),
          'lr':(-200,200)}
square(5,points)
turtle.done()