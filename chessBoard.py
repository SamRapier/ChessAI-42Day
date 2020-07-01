from graphics import *
def main():
    width = 600
    height = 600
    win = GraphWin("Chess", width, height)
    win.setBackground("white")
    for i in range (8):
        p1 = Point((width/8) * i, height)
        p2 = Point((width/8) * i, 0)
        L1 = Line(p1, p2)
        L1.setOutline("Black")
        L1.draw(win)

        p3 = Point(width, (height/8)*i)
        p4 = Point(0, (height/8)*i)
        L2 = Line(p3, p4)
        L2.setOutline("Black")
        L2.draw(win)

    
    win.getMouse() # Pause to view result, otherwise the window will disappear
    win.close()
main()