# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
# # import turtle
# # t = turtle.Turtle()
# # t.begin_fill()
# # t.shape("turtle")
# # t.color("green")
# # t.forward(100)
# # t.left(90)
# # t.forward(100)
# # t.left(90)
# # t.forward(100)
# # t.left(90)
# # t.forward(100)
# # t.end_fill()
# # print(input("What shape? "))
# #
#
#
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.color("green")
# t.forward(100)
# t.right(97)
# import
# import turtle
# t = turtle.Turtle()
# for i in range(4):
#     t.forward(100)
#     t.left(90)
#


money_at_first = int(input("money at first:"))
growth_rate1 = (float(input("growth rate:")))
times = (int(input("number of years:")))
a = money_at_first*growth_rate1**times/10000
print(a,"万")
import turtle
t = turtle.Turtle()
t.color("red")
t.pensize(1)
t.penup()
t.setposition(-200,-200)
t.pendown()
for i in range(times):
    t.left(90)
    t.forward(money_at_first/1000*growth_rate1**i)
    t.backward(money_at_first/1000*growth_rate1**i)
    t.rt(90)
    t.fd(10)

growth_rate2 = float(input("growth rate:"))
b = money_at_first*growth_rate2**times
print(b,"万")
t.color("green")
t.pensize(1)
t.penup()
t.setposition(-198,-200)
t.pendown()
for i in range(times):
    t.left(90)
    t.forward(money_at_first/1000*growth_rate2**i)
    t.backward(money_at_first/1000*growth_rate2**i)
    t.rt(90)
    t.fd(10)
turtle.done
