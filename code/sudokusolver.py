#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

count = 0

def find_next_empty(puzzle):
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == -1:
                return row, column
    return None, None
def find_next_full(puzzle):
    for row in range(9):
        for column in range(9):
            if not(puzzle[row][column] == -1):
                return row, column
    return None, None
def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True
    
def solve_sudoku(puzzle):
    global count
    row, col = find_next_empty(puzzle)
    if row is None and col is None:
        #print("Solved")
        return True
    for guess in range(1,10):
        count += 1
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            #print("Square ", row, col, " is valid with ", guess)
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col] = -1
    return False
def is_impossible(puzzle):
    for i in range(9):
        row = {}
        column = {}
        block = {}
        row_cube = 3 * (i//3)
        column_cube = 3 * (i%3)
        for j in range(9):
            if puzzle[i][j]!= -1 and puzzle[i][j] in row:
                return False
            row[puzzle[i][j]] = 1
            if puzzle[j][i]!=-1 and puzzle[j][i] in column:
                return False
            column[puzzle[j][i]] = 1
            rc= row_cube+j//3
            cc = column_cube + j%3
            if puzzle[rc][cc] in block and puzzle[rc][cc]!=-1:
                return False
            block[puzzle[rc][cc]]=1
    return True
def handle_solve_click(event):
    #pylint: disable=unused-argument
    global count
    count = 0
    entryboard = [[],[],[],[],[],[],[],[],[]]
    for row in range(9):
        for item in range(9):
            if board[row][item].get() != "":
                entryboard[row].append(int(board[row][item].get())) 
            else:
                entryboard[row].append(-1)
    #print(entryboard)
    #extraboard = entryboard
    if not(is_impossible(entryboard)):
        showinfo(message="Impossible")
        return False
    solve_sudoku(entryboard)
    #print(count)
    time = count/2
    while time > 10000:
        time -= 1000
        print(time)
    #print(time)
    pb.start(round(time/100))
    #print(entryboard)
    window.after(round(time), show_solution, entryboard)
    window.after(10, update_progress_bar)
def show_solution(entryboard):
    pb.stop()
    pb['value'] = 100
    count = 0
    for row in range(9):
        for item in range(9):
            board[row][item].delete(0, tk.END)
            board[row][item].insert(0, entryboard[row][item])
    print("+" + "---+"*9)
    for i, row in enumerate(entryboard):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != -1 else " " for x in row]))
        if i % 3 == 2:
            print("+" + "---+"*9)
        else:
            print("+" + "   +"*9)
def handle_clear_click(event):
    for row in range(9):
        for item in range(9):
            board[row][item].delete(0, tk.END)
    pb['value'] = 0
    progress['text'] = "0.0%"
# def handle_save_click(event):
#     entryboard = [[],[],[],[],[],[],[],[],[]]
#     stringtowrite = ""
#     for row in range(9):
#         for item in range(9):
#             if board[row][item].get() != "":
#                 entryboard[row].append(int(board[row][item].get())) 
#             else:
#                 entryboard[row].append(-1)
#     stringtowrite += ("+" + "---+"*9)+"\n"
#     for i, row in enumerate(entryboard):
#         stringtowrite += ("|" + " {}   {}   {} |"*3).format(*[x if x != -1 else " " for x in row]) + "\n"
#         if i % 3 == 2:
#             stringtowrite += ("+" + "---+"*9) + "\n"
#         else:
#             stringtowrite += ("+" + "   +"*9) + "\n"
#     with open("file.txt", "a") as file:
#         file.write(stringtowrite)
#         file.write("\n\n")
def handle_hint_click(event):
    #pylint: disable=unused-argument
    entryboard = [[],[],[],[],[],[],[],[],[]]
    otherboard = [[],[],[],[],[],[],[],[],[]]
    for row in range(9):
        for item in range(9):
            if board[row][item].get() != "":
                entryboard[row].append(int(board[row][item].get()))
                otherboard[row].append(int(board[row][item].get()))
            else:
                entryboard[row].append(-1)
                otherboard[row].append(-1)
    #print(entryboard)
    #extraboard = entryboard
    if not(is_impossible(entryboard)):
        showinfo(message="Impossible")
        return False
    solve_sudoku(entryboard)
    #print(entryboard)
    #print(otherboard)
    for row in range(9):
        for item in range(9):
            if otherboard[row][item] != entryboard[row][item]:
                board[row][item].delete(0, tk.END)
                board[row][item].insert(0, entryboard[row][item])
                return True
    showinfo(message="Already solved")
    
def update_progress_bar():
    if pb['value'] < 100:
        progress['text'] =  f"{pb['value']}%"
        window.after(10, update_progress_bar)
    else:
        pb['value'] = 100
        progress['text'] = "Complete"

if __name__ == "__main__":
    window = tk.Tk()
    #title = tk.Label(text="WELCOME TO THE SUDOKU SOLVER", font=("Arial"))
    #title.grid(row=1, column=1)
    board = [[],[],[],[],[],[],[],[],[]]
    entryboard = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,]]
    sudoku_frame = tk.Frame(relief=tk.SUNKEN, borderwidth=5)
    for row in range(9):
        for item in range(9):
            myentry = tk.Entry(master=sudoku_frame, width=1)
            row_start = (row // 3)
            col_start = (item // 3)
            rowpos = row_start + row
            #print(rowpos)
            colpos = col_start + item + 1
            #print(col_start)
            myentry.grid(row=rowpos, column=colpos)
            board[row].append(myentry)
    sudoku_frame.pack()
    progress_frame = tk.Frame()
    pb = ttk.Progressbar(master=progress_frame, orient='horizontal', mode='determinate', length=280)
    pb.grid(row=0, column=0)
    progress = tk.Label(master=progress_frame, text="0.0%")
    progress.grid(row=1, column=0)
    progress_frame.pack(pady=15)
    button_frame = tk.Frame(relief=tk.RIDGE, borderwidth=5)
    solve_btn = tk.Button(master=button_frame, text="Solve", relief=tk.FLAT, borderwidth=2)
    solve_btn.bind("<Button-1>", handle_solve_click)
    solve_btn.grid(row=0,column=0)
    clear_btn = tk.Button(master=button_frame, text="Clear", relief=tk.FLAT, borderwidth=2)
    clear_btn.bind("<Button-1>", handle_clear_click)
    clear_btn.grid(row=0, column=1)
    #save_btn = tk.Button(master=button_frame, text="Save to file")
    #save_btn.bind("<Button-1>", handle_save_click)
    #save_btn.grid(row=0, column=0)
    hint_btn = tk.Button(master=button_frame, text="Hint", relief=tk.FLAT, borderwidth=2)
    hint_btn.bind("<Button-1>", handle_hint_click)
    hint_btn.grid(row=0, column=3)
    button_frame.pack()
    window.mainloop()
