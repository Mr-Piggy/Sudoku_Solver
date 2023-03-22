# Sudoklu
A sudoku solver that can also give hints about one of the squares.
# How To Install
Run the Linux command ```curl https://raw.githubusercontent.com/Mr-Piggy/Sudoku_Solver/main/install | bash```
# Manual Installation
If you want to see what happens under the hood, run the following commands in a terminal:
```
sudo apt update
sudo apt install git
mkdir ~/.sudokusolver
cd ~/.sudokusolver
git clone https://github.com/Mr-Piggy/Sudoku_Solver
cd Sudoku_Solver/binary
chmod +x sudokusolver
cp -r * ..
cd ..
sudo rm -r binary code .git
sed -i "s/^Icon.*/Icon=${HOME}/.sudokusolver/Sudoku_Solver/sudoku.jpg/" SudokuSolver.desktop
cp SudokuSolver.desktop ~/Desktop/
sudo cp SudokuSolver.desktop /usr/share/applications/
sudo cp sudokusolver /usr/bin/
```
# Source code
The source code for this is in the ```code``` directory. It is one python file that relies on Tkinter.
