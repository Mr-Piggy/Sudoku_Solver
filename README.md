# Sudoklu
A sudoku solver that can also give hints about one of the squares.
# How To Install
Run the Linux command ```curl https://raw.githubusercontent.com/Mr-Piggy/Sudoku_Solver/main/install | bash```
# Manual Installation
If you want to see what happens under the hood, run the following commands in a terminal:
```
sudo curl https://github.com/Mr-Piggy/Sudoku_Solver/raw/main/binary/sudokusolver > /usr/bin/sudokusolver
sudo curl https://raw.githubusercontent.com/Mr-Piggy/Sudoku_Solver/main/binary/sudoku.jpg > /usr/share/icons/sudoku.jpg
sudo curl https://raw.githubusercontent.com/Mr-Piggy/Sudoku_Solver/main/binary/SudokuSolver.desktop > /usr/share/applications/sudokusolver.desktop
sudo ln -s /usr/share/applications/sudokusolver.dekstop $HOME/Desktop
```
# Source code
The source code for this is in the ```code``` directory. It is one python file that relies on Tkinter.
