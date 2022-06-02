with open('input.txt') as fl:
    nums = fl.readline().split(',')
    nums = [int(x) for x in nums]
    rest = fl.read().splitlines()

# Setup
num_of_b = len(rest) // 6
boards = [rest[(i*6)+1:(i*6)+6] for i in range(num_of_b)]
boards = [[[int(x) for x in row.split()] for row in board] for board in boards]
marks = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]
b_has_won = [False for _ in range(len(boards))]
    
def run():
    for num in nums:

        # Make marks
        for b, board in enumerate(boards):
            for y, row in enumerate(board):
                for x, ent in enumerate(row):
                    if ent == num:
                        marks[b][y][x] = True

        # Check
        for b, board in enumerate(marks):
            for y, row in enumerate(board): # Vertical
                if False not in row:
                    b_has_won[b] = True
                    if False not in b_has_won:
                        return num, b
            for x in range(5): # Horizontal
                if False not in [row[x] for row in board]:
                    b_has_won[b] = True
                    if False not in b_has_won:
                        return num, b

w_num, w_b = run()

# Sum unmarked
sum = 0
for y, row in enumerate(boards[w_b]):
    for x, ent in enumerate(row):
        if not marks[w_b][y][x]:
            sum += ent

print(sum * w_num)

        

        

        

        

    






