import turtle


# 爬行：
# forward(n); backward(n)
# 转向：
# left(a); right(a)
# 抬笔放笔：
# penup(); pendown()
# 笔属性：
# pensize(s); pencolor(c)

# t = turtle.Turtle()
# for i in range(4):
#     t.forward(100)
#     t.right(90)
#
# turtle.done()

#画五角星
# t2 = turtle.Turtle()
# t2.pencolor('red')
# t2.pensize(4)
# for i in range(5):
#     t2.forward(100)
#     t2.right(144)
# t2.hideturtle()
# turtle.done()

#螺旋
# t = turtle.Turtle()
# def drawSpriral(t,lineLen):
#     if lineLen > 0:
#         t.forward(lineLen)
#         t.right(90)
#         drawSpriral(t, lineLen - 5)
#
# drawSpriral(t,100)
# t.hideturtle()
# turtle.done()

#分形树

def tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len-15)
        t.left(40)
        tree(branch_len -15)
        t.right(20)
        t.backward(branch_len)

t = turtle.Turtle()
t.speed(1)
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(45)
t.hideturtle()
turtle.done()
