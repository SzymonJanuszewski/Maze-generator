import maze

def Test1(mymaze):
    mymaze.N = 10
    mymaze.M = 12
    mymaze.entryCords = (0, 7)
    mymaze.escapeCords = (9, 9)
    maze.generateMaze(mymaze, testingMode = True)
    print('test1')
    for i in mymaze.maze:
        print(i)


def Test2(mymaze):
    mymaze.N = 20
    mymaze.M = 10
    mymaze.entryCords = (4, 0)
    mymaze.escapeCords = (16, 0)
    maze.generateMaze(mymaze, testingMode = True)
    print('test2')
    for i in mymaze.maze:
        print(i)


def Test3(mymaze):
    mymaze.N = 10
    mymaze.M = 10
    mymaze.entryCords = (0, 5)
    mymaze.escapeCords = (0, 7)
    maze.generateMaze(mymaze, testingMode = True)
    print('test3')
    assert mymaze.getField(0, 6).wall


def Test4(mymaze):
    mymaze.N = 13
    mymaze.M = 17
    mymaze.entryCords = (0, 5)
    mymaze.escapeCords = (0, 7)
    maze.generateMaze(mymaze, testingMode = True)
    print('test4')
    for i in mymaze.maze:
        for j in i:
            if (j.wall == False) and (j != mymaze.entry) and (j != mymaze.escape):
                x = j.x
                y = j.x
                mymaze.imdPoint.append(mymaze.getField(x, y))
                break
        if len(mymaze.imdPoint) == 1:
            break

    origin = mymaze.entry
    path = []
    for i in mymaze.imdPoint:
        mymaze.endPoint = i
        path.extend(maze.bfs(origin, mymaze.endPoint, mymaze))
        origin = mymaze.endPoint

    path.extend(maze.bfs(origin, mymaze.escape, mymaze))

    for i in path:
        i.path = True

    assert mymaze.getField(x, y).path


def Test5(mymaze):
    mymaze.N = 13
    mymaze.M = 17
    mymaze.entryCords = (0, 5)
    mymaze.escapeCords = (0, 7)
    maze.generateMaze(mymaze, testingMode = True)
    print('test5')
    for i in mymaze.maze:
        for j in i:
            if (j.wall == False) and (j != mymaze.entry) and (j != mymaze.escape):
                x = j.x
                y = j.x
                mymaze.imdPoint.append(mymaze.getField(x, y))
                break
        if len(mymaze.imdPoint) == 2:
            break

    mymaze.imdPoint.remove(mymaze.imdPoint[0])

    for i in mymaze.maze:
        for j in i:
            if (j.wall == False) and (j != mymaze.entry) and (j != mymaze.escape) and (j not in mymaze.imdPoint):
                x = j.x
                y = j.x
                mymaze.imdPoint.append(mymaze.getField(x, y))
                break
        if len(mymaze.imdPoint) == 1:
            break

    origin = mymaze.entry
    path = []
    for i in mymaze.imdPoint:
        destination = i
        path.extend(maze.bfs(origin, destination, mymaze))
        origin = destination

    path.extend(maze.bfs(origin, mymaze.escape, mymaze))

    for i in path:
        i.path = True

    assert mymaze.getField(x, y).path
