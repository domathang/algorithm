
import sys

input = sys.stdin.readline
t = int(input())
x = [0, 1, 0, -1]
y = [1, 0, -1, 0]
for i in range(t):
    command = input()
    direction = 0
    north, east, west, south = 0, 0, 0, 0
    cur = [0, 0]
    for j in command:
        if j == "F":
            cur[0] += x[direction]
            cur[1] += y[direction]
        elif j == "B":
            cur[0] -= x[direction]
            cur[1] -= y[direction]
        elif j == "L":
            direction = (direction - 1) % 4
        elif j == "R":
            direction  = (direction + 1) % 4
        north = max(north, cur[0])
        east = max(east, cur[1])
        west = min(west, cur[1])
        south = min(south, cur[0])
    print((north - south) * (east - west))