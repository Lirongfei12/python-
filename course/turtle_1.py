import turtle as t
import time as ti
# t.shape('arrow')
# t.forward(100)
# ti.sleep(1)
# t.right(90)
# t.fd(100)
# ti.sleep(1)
# t.right(90)
# t.fd(100)
# ti.sleep(1)
# t.right(90)
# t.fd(100)
# ti.sleep(3)
##for 循环
# for i in range(4):
#     t.fd(100)
#     t.right(90)
#     ti.sleep(1)
##while 循环
# a = 0
# while a<4:
#     t.fd(100)
#     t.right(90)
#     ti.sleep(1)
#     a += 1
# #图形填充
# t.fillcolor('blue')
# t.begin_fill()
# t.goto(0,0)
# ti.sleep(1)
# t.goto(100,100)
# ti.sleep(1)
# t.goto(200,0)
# ti.sleep(1)
# t.goto(0,0)
# t.end_fill()
# ti.sleep(2)
# #画圆
# t.reset()
# t.penup()
# t.circle(-100,90)
# ti.sleep(0.1)
# t.pendown()
# t.circle(100,360)
# ti.sleep(0.1)
#填充颜色
# t.pensize(10)
# t.pencolor('yellow')
# t.bgcolor('black')
# t.fillcolor('white')
# t.begin_fill()
# t.penup()
# t.goto(0,0)
# t.pendown()
# for i in range(4):
#     t.forward(100)
#     t.right(90)
# t.end_fill()
# ti.sleep(2)
# #作业 01
# j =int(120)
# number= 0
# for i in range(3):
#     if number == 0:
#         color = str('blue')
#         number  += 1
#     elif number == 1:
#         color = str('green')
#         number += 1
#     else:
#         color = str('yellow')
#     t.fillcolor(color)
#     t.begin_fill()
#     t.circle(j,360)
#     t.end_fill()
#     j -=30
# ti.sleep(2)
#作业02
#10笔画
# t.penup()
# t.goto(-200,30)
# t.pencolor('red')
# t.pendown()
# t.fillcolor('red')
# t.begin_fill()
# for i in range(5):
#     t.fd(100)
#     t.left(72)
#     t.fd(100)
#     t.right(144)
# t.end_fill()
# ti. sleep(2)
# # #5笔画
# t.penup()
# t.goto(200, 30)
# t.pencolor('red')
# t.pendown()
# t.begin_fill()
# for i in range(5):
#     t.forward(262)
#     t.right(144)
# t.end_fill()
# t.done()

#导入库
# import turtle

#导入库并导入所有类
# from turtle import *

#导入库并重命名库
import turtle as t
# t.shape('classic')
# t.bgcolor('yellow')
# t.fillcolor('red')
#
# t.pencolor('blue')
# t.pensize(10)
# t.begin_fill()
# for i in range(4):
#
#     t.forward(150)
#     t.left(90)
# t.end_fill()
# t.done()

t.forward(100)
t.left(90)
t.forward(100)
t.left(135)
t.forward(145)
t.done()
t.penup()
t.goto(0,0)
t.bgcolor('yellow')
t.pencolor('blue')
t.pensize(20)
t.fillcolor('red')
t.begin_fill()
for i in range(3):
    t.forward(200)
    t.left(120)
t.end_fill()
t.done()