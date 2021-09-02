import random
import tkinter as tk

import field


def setupMaze(mymaze, NA, MA):
    try:
        NA = int(NA)
        MA = int(MA)
        if (NA >= 4) and (NA <= 30) and (MA >= 4) and (MA <= 30):
            mymaze.N = NA
            mymaze.M = MA
            mymaze.generated = False
            for i in mymaze.mazeButtons:
                for j in i:
                    j.destroy()

            mymaze.mazeButtons = [
                [tk.Button(width=2, height=1, command=lambda mymaze=mymaze, i=i, j=j :clickMazeButton( i, j, mymaze), bg='white') for i in range(mymaze.N)]
                for j in range(mymaze.M)]
            for i in range(mymaze.N):
                for j in range(mymaze.M):
                    mymaze.mazeButtons[j][i].place(x=110 + i * 22, y=j * 22)
            mymaze.wybierzWejWyj = 0
            mymaze.entryCords = None
            mymaze.escapeCords = None
            # buttonGenerate.place(x=5, y=120)
        else:
            print("Rozmiar kazdej sciany labiryntu musi byc wieksza lub równa cztery i mniejsza, badz rowna 30")
    except:
        print("Podaj poprawny rozmiar labiryntu")
        return

def clickMazeButton(x, y, mymaze):
    if mymaze.generated:
        if (mymaze.entry != mymaze.getField(x, y)) and (mymaze.escape != mymaze.getField(x, y)) and (mymaze.getField(x, y).wall == False):
            if mymaze.getField(x, y) in mymaze.imdPoint:
                mymaze.mazeButtons[y][x].config(bg='white')
                mymaze.imdPoint.remove(mymaze.getField(x, y))
            else:
                mymaze.mazeButtons[y][x].config(bg='lightblue')
                mymaze.imdPoint.append(mymaze.getField(x, y))

            for i in mymaze.maze:
                for j in i:
                    j.path = False

            origin = mymaze.entry
            path = []
            for i in mymaze.imdPoint:
                destination = i
                path.extend(bfs(origin, destination, mymaze))
                origin = destination

            path.extend(bfs(origin, mymaze.escape, mymaze))

            for i in path:
                i.path = True
            for i in mymaze.maze:
                for j in i:
                    if j.wall != False or j in {mymaze.entry, mymaze.escape} or j in mymaze.imdPoint:
                        continue
                    if j.path:
                        mymaze.mazeButtons[j.y][j.x].config(bg='yellow')
                    else:
                        mymaze.mazeButtons[j.y][j.x].config(bg='white')
    else:
        if (x == 0) or (x == mymaze.N - 1) or (y == 0) or (y == mymaze.M - 1):
            if mymaze.wybierzWejWyj == 0:
                if (x, y) == mymaze.escapeCords:
                    print("Wejscie i wyjscie nie moze być na jednym polu")
                    return
                if mymaze.entryCords is None:
                    pass
                else:
                    mymaze.mazeButtons[mymaze.entryCords[1]][mymaze.entryCords[0]].config(bg='white')
                mymaze.entryCords = (x, y)
                mymaze.mazeButtons[y][x].config(bg='red')
                mymaze.wybierzWejWyj = 1
            elif mymaze.wybierzWejWyj == 1:
                if (x, y) == mymaze.entryCords:
                    print("Wejscie i wyjscie nie może być na jednym polu")
                    return
                if mymaze.escapeCords != None:
                    mymaze.mazeButtons[mymaze.escapeCords[1]][mymaze.escapeCords[0]].config(bg='white')
                mymaze.escapeCords = (x, y)
                mymaze.mazeButtons[y][x].config(bg='green')
                mymaze.wybierzWejWyj = 0


def generateMaze(mymaze, testingMode = False):
    if (mymaze.entryCords is None) or (mymaze.escapeCords is None):
        print("Nalezy wybrac wejscie i wyjscie")
        return
    mymaze.maze = [[field.Field(i, j) for i in range(mymaze.N)] for j in range(mymaze.M)]
    mymaze.entry = mymaze.getField(mymaze.entryCords[0], mymaze.entryCords[1])
    mymaze.escape = mymaze.getField(mymaze.escapeCords[0], mymaze.escapeCords[1])
    if mymaze.escape in mymaze.entry.adjacentField(mymaze):
        print("Wejscie nie moze znajdowac sie kolo wyjscia")
        return
    mymaze.wybierzWejWyj = -1
    mymaze.escape.wall = False
    mymaze.escape.visited = True
    mymaze.entry.visited = True
    mymaze.frontier = [mymaze.entry]
    while len(mymaze.frontier) > 0:
        drawPath(mymaze.frontier[random.randint(0, len(mymaze.frontier) - 1)], mymaze)

    mymaze.generated = True

    mymaze.imdPoint = []

    origin = mymaze.entry
    path = []
    for i in mymaze.imdPoint:
        destination = i
        path.extend(bfs(origin, destination, mymaze))
        origin = destination

    path.extend(bfs(origin, mymaze.escape, mymaze))

    for i in path:
        i.path = True

    if not testingMode:
        for i in mymaze.maze:
            for j in i:
                if j.wall:
                    mymaze.mazeButtons[j.y][j.x].config(bg='purple')
                elif j not in {mymaze.entry, mymaze.escape}:
                    if j.path:
                        mymaze.mazeButtons[j.y][j.x].config(bg='yellow')
                    else:
                        mymaze.mazeButtons[j.y][j.x].config(bg='white')


def drawPath(x, mymaze):
    mymaze.frontier.remove(x)
    if x.isPath(mymaze):
        x.wall = False
        unvisitedAdjacent = x.unvisitedField(mymaze)
        if mymaze.entry == x:
            if mymaze.entry.x == mymaze.escape.x:
                if mymaze.entry.y > mymaze.escape.y:
                    unvisitedAdjacent.remove(mymaze.getField(mymaze.entry.x, mymaze.entry.y - 1))
                else:
                    unvisitedAdjacent.remove(mymaze.getField(mymaze.entry.x, mymaze.entry.y + 1))
            elif mymaze.entry.y == mymaze.escape.y:
                if mymaze.entry.x > mymaze.escape.x:
                    unvisitedAdjacent.remove(mymaze.getField(mymaze.entry.x - 1, mymaze.entry.y))
                else:
                    unvisitedAdjacent.remove(mymaze.getField(mymaze.entry.x + 1, mymaze.entry.y))

        for i in unvisitedAdjacent:
            i.visited = True
            mymaze.frontier.append(i)


def bfs(origin, destination, mymaze):
    result = []

    mymaze.frontier = []
    mymaze.frontier.append(origin)
    cameFrom = dict()
    cameFrom[origin] = None

    while len(mymaze.frontier) > 0:
        for i in mymaze.frontier[0].adjacentOpen(mymaze):
            if i not in cameFrom:
                mymaze.frontier.append(i)
                cameFrom[i] = mymaze.frontier[0]
        del mymaze.frontier[0]
    head = destination
    while head != origin:
        result.append(head)
        if head in cameFrom:
            head = cameFrom[head]
        else:
            break
    result.append(origin)
    return result
