from tkinter import *
import random, time, copy
from threading import Thread

wx = 900
wy = 900
size = 15

dx = wx // size
dy = wy // size

window = Tk()
cav = Canvas(window, width = wx, height = wy)
cav.pack()

def getColor(x, y):
    if mmap[x][y] == 0:
        return 'black'
    elif mmap[x][y] == 1:
        return 'yellow'
    elif mmap[x][y] == 2:
        return 'blue'
    elif mmap[x][y] == 3:
        return 'red'
    else:
        mmap[x][y] = 0
        return 'black'

def setColor(x, y):
    cav.create_rectangle(x * size, y * size, x * size + size, y * size - size, outline = 'white', fill = getColor(x, y))

def change(event):
    x = event.x // size
    if x < 0:
        x = 0
    elif x >= dx:
        x = dx - 1
    y = event.y // size
    y += 1
    if y < 0:
        y = 0
    elif y >= dy:
        y = dy - 1
    mmap[x][y] += 1
    setColor(x, y)
    cav.update()

alive = True
def work():
    while alive:
        tmap = copy.deepcopy(mmap)
        for x in range(dx):
            for y in range(dy):
                if tmap[x][y] == 2:
                    mmap[x][y] = 3
                    setColor(x, y)
                    cav.update()
                elif tmap[x][y] == 3:
                    mmap[x][y] = 1
                    setColor(x, y)
                    cav.update()
                elif tmap[x][y] == 1:
                    sum = 0
                    if x - 1 >= 0 and y - 1 >= 0 and tmap[x - 1][y - 1] == 2:
                        sum += 1
                    if y - 1 >= 0 and tmap[x][y - 1] == 2:
                        sum += 1
                    if x + 1 < dx and y - 1 >= 0 and tmap[x + 1][y - 1] == 2:
                        sum += 1
                    if x - 1 >= 0 and tmap[x - 1][y] == 2:
                        sum += 1
                    if x + 1 < dx and tmap[x + 1][y] == 2:
                        sum += 1
                    if x - 1 >= 0 and y + 1 < dy and tmap[x - 1][y + 1] == 2:
                        sum += 1
                    if y + 1 < dy and tmap[x][y + 1] == 2:
                        sum += 1
                    if x + 1 < dx and y + 1 < dy and tmap[x + 1][y + 1] == 2:
                        sum += 1
                    if sum == 1 or sum == 2:
                        mmap[x][y] = 2
                        setColor(x, y)
                        cav.update()
                else:
                    pass

th = []
ptr = 0
def run(event):
    global ptr
    global alive
    alive = True
    t = Thread(target = work)
    t.start()
    th.append(t)
    ptr += 1

def stop(event):
    global alive
    alive = False

mmap = [[0 for i in range(dy)] for j in range(dx)]
for i in range(dx):
    for j in range(dy):
        setColor(i, j)

cav.bind('<Button-1>', change)
cav.bind('<Button-3>', run)
cav.bind('<Double-Button-3>', stop)
window.mainloop()
