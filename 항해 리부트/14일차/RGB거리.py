n = int(input())
rgb = [0] * 3
for i in range(n):
    r, g, b = map(int, input().split())
    rgb = [r + min(rgb[1], rgb[2]), g + min(rgb[0], rgb[2]), b + min(rgb[0], rgb[1])]
print(min(rgb))