# import colorgram
#
# colors_extracted = colorgram.extract('hirst_dots.jpg', 30)
#
# list_of_colors = []
# for color in colors_extracted:
#     rgb_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     list_of_colors.append(rgb_tuple)
#
# print(list_of_colors)

# 10 x 10 rows of spots
# dots = 20 in size, spaces = 50

from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

screen.colormode(255)
color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61),
              (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39),
              (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202),
              (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84), (120, 41, 33), (170, 203, 205),
              (223, 178, 169)]


def draw_dots(no_of_columns, no_of_rows, size_of_dots, space_between_dots):
    """ Creates the painting of dots in different colors.
    Requires number of columns and rows, size of the dots, and size of spaces between them."""
    start_position_x = -300
    start_position_y = -300
    for i in range(no_of_rows):
        tim.penup()
        tim.setposition(x=start_position_x,
                        y=start_position_y + (i * (size_of_dots + space_between_dots)))
        for column in range(no_of_columns):
            random_color = random.choice(color_list)
            tim.pendown()
            tim.dot(size_of_dots, random_color)
            tim.penup()
            tim.forward(size_of_dots + space_between_dots)


draw_dots(10, 10, 20, 50)
screen.exitonclick()
