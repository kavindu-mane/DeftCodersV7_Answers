def find(lines):
    row , col = 0 ,0
    for line in lines:
        for charactor in line:
            if(charactor == "X"):
                return str(row) + "," + str(col)
            col += 1
        row += 1
        col = 0

lines_count = int(input())
lines = []
for _ in range(lines_count):
    lines.append(list(input()))
print(find(lines))
