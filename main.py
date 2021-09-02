import tkinter as tk
import maze
import tests

class MyMaze:
    def __init__(self):
        self.frontier = []
        self.wybierzWejWyj = -1
        self.entryCords = None
        self.escapeCords = None
        self.N = 0
        self.M = 0
        self.entry = None
        self.escape = None
        self.mazeButtons = []
        self.maze = []
        self.imdPoint = []
        self.generated = False

    def getField(self, x, y):
        return self.maze[y][x]

def testMaze():
    mymazeTest = MyMaze()
    tests.Test1(mymazeTest)
    tests.Test2(mymazeTest)
    tests.Test3(mymazeTest)
    tests.Test4(mymazeTest)
    tests.Test5(mymazeTest)

def main():

    mymaze = MyMaze()

    window = tk.Tk()

    window.geometry("800x680")
    window.resizable(False, False)

    labelWidth = tk.Label(text="Szerokosc:")
    inputWidth = tk.Entry(width=3)
    labelHight = tk.Label(text="Wysokosc:")
    inputHight = tk.Entry(width=3)
    buttonCheck = tk.Button(text="Sprawdz", width=10, command=lambda: maze.setupMaze(mymaze, inputWidth.get(),
                                                                                inputHight.get()))
    buttonGenerate = tk.Button(text="Generuj", width=10, command=lambda: maze.generateMaze(mymaze))
    buttonGenerate.place(x=5, y=120)
    buttonTest = tk.Button(text="Przetestuj", width=10, command=lambda: testMaze())
    buttonTest.place(x=5, y=160)

    labelWidth.place(x=0, y=0)
    inputWidth.place(x=65, y=0)
    labelHight.place(x=0, y=40)
    inputHight.place(x=65, y=40)
    buttonCheck.place(x=5, y=80)

    inputWidth.insert(0, "13")
    inputHight.insert(0, "12")

    mymaze.wybierzWejWyj = -1
    mymaze.generated = False

    window.mainloop()


main()