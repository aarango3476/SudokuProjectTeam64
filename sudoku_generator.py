import random

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [["-" for i in range(row_length)] for j in range(row_length)]
        self.box_length = int(self.row_length ** 0.5)

    def get_board(self):

        return self.board

    def print_board(self):
        r=0
        for row in self.board:

            for index,num in enumerate(row):
                if index==3 or index==6:
                    print(" ", end=" ")

                print(num, end=" ")

            if r==2 or r==5:
                print()


            print()
            r+=1


    def valid_in_row(self,row,num):
        if num in self.board[row]:
            return False
        else:
            return True
    def valid_in_col(self,col,num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True
    def valid_in_box(self,row_start,col_start,num):
        for row in range(row_start,row_start+3):
            for col in range(col_start,col_start+3):
                if self.board[row][col] == num:
                    return False
        return True
#0-2, 3-5, 6-8
    def is_valid(self, row,col,num):
        if 0<=row<=2:
            rowstart=0
        elif 3<=row<=5:
            rowstart=3
        elif 6<=row<=8:
            rowstart=6

        if 0<=col<=2:
            colstart=0
        elif 3<=col<=5:
            colstart=3
        elif 6<=col<=8:
            colstart=6
        if self.valid_in_row(row,num) and self.valid_in_col(col,num):
            if self.valid_in_box(rowstart,colstart,num):
                return True
        return False
    def fill_box(self,row_start,col_start):
        banned=[]
        for row in range(row_start,row_start+3):
            for col in range(col_start,col_start+3):
                i=random.randint(1,9)
                while i in banned:
                    i=random.randint(1,9)

                self.board[row][col] = i

                banned.append(i)
    def fill_diagonal(self):
        self.fill_box(0,0)
        self.fill_box(3,3)
        self.fill_box(6,6)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
    def remove_cells(self):
        rc=0
        while rc<self.removed_cells:
            row=random.randint(0,self.row_length-1)
            col=random.randint(0,self.row_length-1)
            while self.board[row][col] == 0:
                row=random.randint(0,self.row_length-1)
                col=random.randint(0,self.row_length-1)
            self.board[row][col]=0
            rc+=1

def generate_sudoku(size, removed):
        sudoku = SudokuGenerator(size, removed)
        sudoku.fill_values()
        board = sudoku.get_board()
        sudoku.remove_cells()
        board = sudoku.get_board()
        return board


#board = generate_sudoku(9, 30)


