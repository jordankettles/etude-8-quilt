# Etude 8 Quilt
# Jordan Kettles 2147684
# 22 April 2021

# Uses graphics.py under GPL.

import sys, graphics, math, copy

windowSize = 500

# Square class for holding information on each type of square.
class Square:

    size = 0.0
    MaxScale = 0.0

    def __init__(self, scale, red, green, blue):
        self.scale = scale
        self.red = red
        self.green = green
        self.blue = blue
        Square.size += scale
        if scale > Square.MaxScale:
            Square.MaxScale = scale

    def setCentre(self, point):
        self.centre = point

    def getCentre(self):
        return self.centre

    def moveCentre(self, x, y):
        self.centre.move(x, y)

    def getLength(self):
        # Almost fit the window.
        return round((self.scale*(Square.size / Square.MaxScale))/1.1)

    def drawSquare(self, window):
        if self.centre is not None:
            p1 = copy.deepcopy(self.centre)
            p2 = copy.deepcopy(self.centre)
            p1.move(-self.getLength() / 2, -self.getLength() / 2) # point 1.
            p2.move(self.getLength() / 2, self.getLength() / 2) # point 2.
            sq = graphics.Rectangle(p1, p2) # square.
            sq.setFill(graphics.color_rgb(self.red, self.green, self.blue))
            sq.setOutline(graphics.color_rgb(self.red, self.green, self.blue))
            sq.draw(window)

# queue holds the next square to draw, and the type of square.
queue = list()
# squares hold each type of square.
squares = list()

# read input
for line in sys.stdin:
    line = line.strip()
    s = line.split(" ")
    squares.append(Square(float(s[0]), int(s[1]), int(s[2]), int(s[3])))

Square.size = math.floor(windowSize / (Square.size / Square.MaxScale))

window = graphics.GraphWin("Quilt", windowSize, windowSize, autoflush=False)
squares[0].setCentre(graphics.Point(windowSize / 2, windowSize / 2));
queue.append([squares[0], 1])

# draw squares
while len(queue) > 0:
    current = queue.pop(0)
    depth = current[1]
    current_square = current[0]
    current_square.drawSquare(window)
    if depth < len(squares):
        tl = copy.deepcopy(squares[depth]) # top left.
        tl.setCentre(copy.deepcopy(current_square.getCentre()))
        tl.moveCentre(-current_square.getLength() / 2, -current_square.getLength() / 2)
        queue.append([tl, depth+1])
        tr = copy.deepcopy(squares[depth]) # top right.
        tr.setCentre(copy.deepcopy(current_square.getCentre()))
        tr.moveCentre(current_square.getLength() / 2, -current_square.getLength() / 2)
        queue.append([tr, depth+1])
        bl = copy.deepcopy(squares[depth]) # bottom left.
        bl.setCentre(copy.deepcopy(current_square.getCentre()))
        bl.moveCentre(-current_square.getLength() / 2, current_square.getLength() / 2)
        queue.append([bl, depth+1])
        br = copy.deepcopy(squares[depth]) # bottom right.
        br.setCentre(copy.deepcopy(current_square.getCentre()))
        br.moveCentre(current_square.getLength() / 2, current_square.getLength() / 2)
        queue.append([br, depth+1])

window.flush()

print("Click the window to close.")
window.getMouse()
window.close()
