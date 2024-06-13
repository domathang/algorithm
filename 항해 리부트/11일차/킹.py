a, b, n = input().split()
n = int(n)
move = [input() for _ in range(n)]
row = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
command_x = {"R": 1, "L": -1, "B": 0, "T": 0, "RT": 1, "LT": -1, "RB": 1, "LB": -1}
command_y = {"R": 0, "L": 0, "B": -1, "T": 1, "RT": 1, "LT": 1, "RB": -1, "LB": -1}
king = [int(a[1]), row[a[0]]]
stone = [int(b[1]), row[b[0]]]

def safe(i, j, c):
    if 1<= i <= 8 and 1 <= j <= 8:
        if i == stone[0] and j == stone[1]:
            return safe(i + command_y[c], j + command_x[c], "")
        return True
    return False

for i in move:
    next_y, next_x = king[0] + command_y[i], king[1] + command_x[i]
    if safe(next_y, next_x, i):
        if next_y == stone[0] and next_x == stone[1]:
            stone = [stone[0] + command_y[i], stone[1] + command_x[i]]
        king = [next_y, next_x]

print("0ABCDEFGH"[king[1]] + str(king[0]))
print("0ABCDEFGH"[stone[1]] + str(stone[0]))
