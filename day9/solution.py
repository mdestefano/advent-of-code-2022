import numpy as np

class Rope:
    def __init__(self, width, height, start=(0,0), knots=2):
        self.width = width
        self.height = height
        self.board = np.full((height, width),".", dtype=str)
        self.start = start
        self.knots = [self.start for i in range(knots)]
        self.visited = set()

    def move(self, direction, amout):
        for i in range(amout):
            # print("=== HEAD MOVED ===")
            self.move_head(direction)
            #self.print_board()
            #print("=== TAIL MOVED ===")
            self.visited.add(self.knots[-1])
            for i in range(1, len(self.knots)):
                self.update_tail(i-1, i)
            #self.print_board()


    def update_tail(self, H, T):
        # if head and tail are on the same row and 
        if self.knots[H][0] == self.knots[T][0]:
            distance = self.knots[H][1] - self.knots[T][1]
            if abs(distance) > 1:
                self.knots[T] = (self.knots[T][0], self.knots[T][1] + np.sign(distance))

        # if head and tail are on the same column
        elif self.knots[H][1] == self.knots[T][1]:
            distance = self.knots[H][0] - self.knots[T][0]
            if abs(distance) > 1:
                self.knots[T] = (self.knots[T][0] + np.sign(distance), self.knots[T][1])

        # if head and tail are on different rows or columns
        else:
            # print("Diagonal")
            # print("H", self.H)
            # print("T", self.T)
            if abs(self.knots[H][0] - self.knots[T][0]) > 1 or abs(self.knots[H][1] - self.knots[T][1]) > 1:
                self.knots[T] = (self.knots[T][0] + np.sign(self.knots[H][0] - self.knots[T][0]), self.knots[T][1] + np.sign(self.knots[H][1] - self.knots[T][1]))

    def move_head(self, direction, head=0):
        H = self.knots[head]
        if direction == "U":
            self.knots[head] = (H[0] + 1, H[1])
        elif direction == "D":
            self.knots[head] = (H[0] - 1, H[1])
        elif direction == "L":
            self.knots[head] = (H[0], H[1] - 1)
        elif direction == "R":
            self.knots[head] = (H[0], H[1] + 1)
        else:
            raise ValueError("Invalid direction")

    def get_number_of_visited(self):
        self.visited.add(self.knots[-1])
        return len(self.visited)

    def print_board(self):
        board_copy = self.board.copy()

        for i in self.visited:
            board_copy[i] = "#"

        board_copy[self.start] = "s"
        for i in range(1,len(self.knots)-1):
            board_copy[self.knots[i]] = i
        
        board_copy[self.knots[0]] = "H"
        board_copy[self.knots[-1]] = "T"

        for i,row in enumerate(reversed(board_copy)):
            print(" ".join(row))


if __name__ == "__main__":

    board = Rope(6,5)
    # board.move("R", 4)
    # board.move("U", 4)
    # board.move("L", 3)

    with open("test.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    
    for line in lines:
        direction, amout = line.split(" ")
        amout = int(amout)
        board.move(direction, amout)
    
    board.print_board()
    print("Visited", board.get_number_of_visited())
    print("=== PART 2 ===")

    big_rope = Rope(30,30, knots=10, start=(5,11))

    with open("input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    for line in lines:
        direction, amout = line.split(" ")
        amout = int(amout)
        big_rope.move(direction, amout)

    #big_rope.print_board()
    print("Visited", big_rope.get_number_of_visited())

