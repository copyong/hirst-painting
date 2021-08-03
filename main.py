# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle
import turtle as turtle_module

turtle.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(145, 86, 47), (212, 157, 94), (64, 25, 9), (242, 219, 68), (16, 32, 52), (45, 107, 145), (9, 42, 22), (238, 215, 183), (41, 126, 88), (29, 179, 138), (62, 15, 26), (95, 173, 222), (194, 148, 31), (127, 69, 84), (195, 238, 213), (159, 18, 32), (148, 26, 13), (219, 80, 64), (231, 208, 217), (225, 70, 83), (199, 219, 237), (21, 164, 213), (119, 185, 147), (15, 95, 62), (211, 133, 143), (92, 75, 15), (52, 57, 87), (241, 159, 171), (245, 219, 4), (143, 221, 183)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()