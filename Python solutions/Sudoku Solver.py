from collections import defaultdict

class Solution:
    def __init__(self):
        self.box_index = lambda row, col: (row // n ) * n + col // n   # lambda function to compute box index
        self.sudoku_solved = False
        n = 3
        self.N = n * n
        self.boxes , self.columns , self.rows = [defaultdict(int) for i in range(self.N)] , [defaultdict(int) for i in range(self.N)] , [defaultdict(int) for i in range(self.N)]

        
    def solveSudoku(self, board):
        self.board = board
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] != '.': 
                    d = int(self.board[i][j])
                    self.__place_number__(d, i, j)
        
        self.__backtrack__()

    def __backtrack__(self, row = 0 , col = 0):
        if self.board[row][col] == '.':
            for d in range(1,10):
                if self.__can_number_be_placed__(d, row, col):
                    self.__place_number__(d, row, col)
                    self.__place_next_numbers__(row, col)

                    if not self.sudoku_solved:
                        self.__remove_number__(d, row, col)
        else:
            self.__place_next_numbers__(row, col)
            
        
    def __can_number_be_placed__(self, d:int , row:int , col:int):
        return not (d in self.rows[row] or d in self.columns[col] or d in self.boxes[self.box_index(row, col)])

    def __place_number__(self, d:int, row:int, col:int):
        self.rows[row][d] += 1
        self.columns[col][d] += 1
        self.boxes[self.box_index(row, col)][d] += 1
        self.board[row][col] = str(d)

    def __remove_number__(self, d:int, row:int, col:int):
        del self.rows[row][d]
        del self.columns[col][d]
        del self.boxes[self.box_index(row, col)][d]
        self.board[row][col] = '.'

    def __place_next_numbers__(self, row:int , col:int):
        if col == self.N-1 and row == self.N-1:
            self.sudoku_solved = True
        elif col == self.N-1:
            self.__backtrack__(row + 1, 0)
        else:
            self.__backtrack__(row, col + 1)

dataSet = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]
sol = Solution()
sol.solveSudoku(dataSet)
print (dataSet)


        
