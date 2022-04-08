class Drawing:
    def __init__(self, lines, columns, symbol):
        a = [symbol] * columns
        self.image = [a.copy() for i in range(lines)]


    def print(self):
        for line in self.image:
            print(' '.join(line))

    def setPoint(self, x, y, char):
        self.image[x][y] = char

    def drawVerticalLine(self, column, line1, line2, symb):
        for i in range(line1, line2+1):
            self.setPoint(i, column, symb)

    def drawHorizontalLine(self, line, column1, column2, symb):
        for i in range(column1, column2+1):
            self.image[line][i] = symb

    def drawRectangle(self, column1, line1, column2, line2, symb):
        minline = min(line1, line2)
        maxline = max(line1, line2)
        mincolumn = min(column1, column2)
        maxcolumn = max(column1, column2)
        self.drawHorizontalLine(line1, mincolumn, maxcolumn, symb)
        self.drawHorizontalLine(line2, mincolumn, maxcolumn, symb)
        self.drawVerticalLine(column1, minline, maxline, symb)
        self.drawVerticalLine(column2, minline, maxline, symb)

    def drawAnyLine(self, line1, column1, line2, column2, symb):
        deltaline = abs(line2-line1)
        deltacolumn = abs(column2-column1)
        error = 0
        deltaerror = deltaline + 1
        line = line1
        dirline = line2 - line1
        if dirline > 0:
            dirline = 1
        if dirline < 0:
            dirline = -1
        for column in range (column1, column2+1):
            self.setPoint(column, line, symb)
            error = error + deltaerror
            if error >= (deltacolumn +1):
                line = line + dirline
                error = error - (deltacolumn +1)


img = Drawing(5, 6, "*")
img.setPoint(0, 0, "&")
img.drawHorizontalLine(2, 0, 2, "%")
img.drawVerticalLine(2,1,4, "@")
img.print()
print("Это прямоугольник")
img.drawRectangle(5, 4, 1, 1, "#")
img.print()
print("Это линия")
img2 = Drawing(10, 10, "*")
img2.drawAnyLine(1, 1, 5, 8, "!")
img2.print()
