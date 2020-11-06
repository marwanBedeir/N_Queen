from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import spinbox
import time

import brute_force
import backtracking
import hill_climpin
import genetic
global flag
flag = 0

def Solve(N):
    # 'BackTrack', 'BruteForce', 'Heuristic', 'Genetic'
    text = algo.get()
    if text == "BackTrack":
        # wrapped = wrapper(backtracking, N)
        # print( timeit.timeit(wrapped, number=1000))
        a = time.perf_counter()
        Board = backtracking.backtracking(N)
        b = time.perf_counter()
        delta = b - a
        print("BackTrack {} elapsed time = {:.12f} seconds".format(N, delta))
        return Board

    elif text == "Heuristic":
        # wrapped = wrapper(my_hill_climpin_algorithm_Implementation, N)
        # print(timeit.timeit(wrapped, number=1000))
        a = time.perf_counter()
        Board = hill_climpin.hill_climpin(N)
        b = time.perf_counter()
        delta = b - a
        print("Heuristic {} elapsed time = {:.12f} seconds".format(N, delta))
        return Board
    elif text == "Genetic":
        a = time.perf_counter()
        Board = genetic.genetic(N)
        b = time.perf_counter()
        delta = b - a
        print("Genetic   {} elapsed time = {:.12f} seconds".format(N, delta))
        return Board
    elif text == "BruteForce":
        a = time.perf_counter()
        Board = brute_force.brute_force(N)
        b = time.perf_counter()
        delta = b - a
        print("BruteForce {} elapsed time = {:.12f} seconds".format(N, delta))
        return Board


def CreateBoard():
    global flag
    if flag == 1:
        global f2
        f2.destroy()

    num = int(Entry.get())

    global N
    N = num

    if N == 2 or N == 3:
        print("No solution")
        messagebox.showwarning('Board size error', 'No Solution For 2 or 3')
        return
    global photo
    if N >= 10:
        if N >= 15:
            inc = N * 0.25
            photo = PhotoImage(file="crown (1).PNG")
        else:
            inc = N
            photo = PhotoImage(file="crown.PNG")
    else:
        inc = 25
        photo = PhotoImage(file="crown (2).PNG")

    if N % 2 == 0:
        even = 1
        odd = 0
    else:
        even = 0
        odd = 1

    black = 0
    white = 1

    Board = Solve(N)
    if Board != []:

        f2 = ttk.Frame(root, style='My.TFrame')
        f2.grid(row=1, column=0, sticky='snew', )
        for i in range(N):
            for j in range(N):
                if Board[i][j] == 1:
                    if white == 1:
                        white = 0
                        black += 1
                        label1 = ttk.Label(f2, text=' ', background='white', image=photo)
                        label1.grid(row=i, column=j, sticky='snew')
                    elif black == 1:
                        black = 0
                        white = 1
                        label1 = ttk.Label(f2, text=' ', background='black', image=photo)
                        label1.grid(row=i, column=j, sticky='snew')
                else:
                    if white == 1:
                        white = 0
                        black += 1

                        label1 = ttk.Label(f2, text=' ', background='white')
                        label1.grid(row=i, column=j, sticky='snew', ipadx=inc, ipady=inc)
                    elif black == 1:
                        white = 1
                        black = 0

                        label1 = ttk.Label(f2, text=' ', background='black')
                        label1.grid(row=i, column=j, sticky='snew', ipadx=inc, ipady=inc)
            if even == 1:
                temp = black
                black = white
                white = temp
        flag = 1
    #    Entry.delete(0,END)


# root
root = Tk()

global photo
photo = PhotoImage(file="crown (2).PNG")

root.title("N Queen ")
root.config(background="#e1d8b2")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

# style
style = ttk.Style()
# style.theme_use('alt')
style.configure('TLabel', background="#e1d8b2")
style.configure('TButton', background="#e1d8b2")
style.configure('TRadiobutton', background="#e1d8b2")
style.configure('My.TFrame', background='#e1d8b2')

# Frame 1

f1 = ttk.Frame(root, style='My.TFrame')
f1.grid(row=0, column=0, sticky='snew')
# f1.config(width = 300, height = 300,relief = RIDGE)


# frame 2

global f2

f2 = ttk.Frame(root, style='My.TFrame')
f2.grid(row=1, column=0, sticky='snew', )
# f2.config(width = 500, height = 300,relief = RIDGE)

# Enter size label
label = ttk.Label(f1, text='Enter Board Size')
label.grid(row=0, column=0, columnspan=2, sticky='snew', padx=10, pady=10)

# button confirm
butt = ttk.Button(f1, text='Confirm')
butt.grid(row=1, column=0, padx=10, pady=10)
butt.configure(command=CreateBoard)

num = IntVar()
num.set(4)

# spinbox numbers
Entry = spinbox.Spinbox(f1, from_=1, to=19, width=5, textvariable=num, state="readonly")
Entry.grid(row=1, column=1, columnspan=2, pady=10, padx=5)

algo = StringVar()
algo.set("BackTrack")

# combobox
combo = ttk.Combobox(f1, state="readonly", textvariable=algo)
combo['values'] = ('BackTrack', 'BruteForce', 'Heuristic', 'Genetic')
combo.current(0)
combo.grid(row=2, column=0, columnspan=2, pady=10, padx=5)

root.mainloop()
