# Later squares might not be smaller than earlier ones, nor the first square
# has a scale parameter of 1.

# Part of the problem is to ensure that whatever scale parameters are given,
# my representation fits, and nearly fills, a reasonably sized window.

# Read in all input.
# calculate the 1.0 scale to fit everything in a 500 * 500 window.
# Draw each square

import sys, graphics, math

windowSize = 500

size = 0.0

def newRectangle(x, y, r, g, b):
    rect = graphics.Rectangle(x, y)
    rect.setFill("red")
    rect.setOutline("blue")
    return rect


def main():
    win = GraphWin("My Rectangle!", windowSize, windowSize)
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

size = math.floor(windowSize / size)
squares = list()
print(size)

prev_x = rect_x = graphics.Point(windowSize/2, windowSize/2)
prev_y = rect_y = graphics.Point(windowSize/2, windowSize/2)

window = graphics.GraphWin("QUILT!", 500, 500)
r = newRectangle(rect_x, rect_y, int(in_list[0][1]), int(in_list[0][2]), int(in_list[0][3]))
r.draw(window)

# recursively draw each square?


    # move the Point.
#     # Create the Rectangle
#     # Draw the Rectangle
for(int i = 0; i < len(in_list)):
    scale = float(square[0])
    movement = round((scale*size)/2)
    print(movement)
    rect_x.move(-movement, -movement)
    rect_y.move(movement, movement)
    print(rect_x)
    print(rect_y)
        # draw each square.
        squares.append(newRectangle(rect_x, rect_y, int(square[1]), int(square[2]), int(square[3])))

for square in squares:
    square.draw(window)

window.getMouse()
window.close()
