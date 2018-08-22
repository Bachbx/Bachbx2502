from turtle import *

width(0)

color_list = ['red', 'blue', 'brown', 'yellow', 'grey']
m = 0
n = 3
for c in color_list:
    m = m + 180
    color(c)
    for i in range(n):
        forward(100)
        left(180 - (m / n))
    n = n + 1









mainloop()