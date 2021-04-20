# Later squares might not be smaller than earlier ones, nor the first square
# has a scale parameter of 1.

# Part of the problem is to ensure that whatever scale parameters are given,
# my representation fits, and nearly fills, a reasonably sized window.

# Read in all input.
# calculate the 1.0 scale to fit everything in a 500 * 500 window.
# Draw each square

import sys, graphics, math

size = 0.0

def newRectangle(x, y, scale, r, g, b):
    rect = graphics.Rectangle(x, y)
    return rect


def main():
    win = GraphWin("My Rectangle!", 500, 500)
    c = Rectangle(Point(10,10), Point(200,200))
    c.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done


in_list = list()
for line in sys.stdin:
    line = line.strip()
    in_list.append(line.split(" "))

for line in in_list:
    size += float(line[0])

size = math.floor(500 / size)
# squares = list()
# print(size)

previous_x = start_x = graphics.Point(round(250-(size/2)), round(250-(size/2)))
previous_y = start_y = graphics.Point(round(250+(size/2)), round(250+(size/2)))W

window = graphics.GraphWin("QUILT!", 500, 500)

r = newRectangle(start_x, start_y, float(in_list[0][0]), int(in_list[0][1]), int(in_list[0][2]), int(in_list[0][3]))
r.draw(window)

# for square in in_list:
#     squares.append()
window.getMouse()
window.close()
