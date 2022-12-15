# 这是通过变量与键盘输入来绘制的图形
# import turtle as t
# x = int(input('x坐标为：'))
# y = int(input('x坐标为：'))
# pensize = int(input('请设置画笔大小:'))
# bjcolor_1 = str(input('请设置背景颜色英文输入'))
# fc= str(input('请设置填充颜色英文输入'))
# t.penup()
# t.goto(x,y)
# t.pensize(pensize)
# t.pencolor('blue')
# t.bgcolor(bjcolor_1)
# t.fillcolor(fc)
# t.begin_fill()
# t.pendown()
# for i in range(4):
#     t.forward(100)
#     t.left(90)
# t.end_fill()
# t.done()
# 下面程序是绘制圆的
from turtle import *
radius = int(255)
fc = 'green'#设置填充颜色变量
penup()
goto(0,-200)
pensize(4)
pendown()
for i in range(4):
    fillcolor(fc)
    begin_fill()
    circle(radius,360)
    radius -= 50
    if radius ==205:
        fc = 'blue'
    if radius ==155:
        fc = 'white'
    if radius == 105:
        fc = 'pink'
    end_fill()
done()