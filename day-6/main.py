rows = []
with open('input.txt') as f:
    for line in f:
        rows.append(line.split())


full_total = 0
for col in range(len(rows[0])):
    op = rows[len(rows)-1][col]
    total = 0
    if op == '*':
        total = 1
    for row in range(len(rows)-1):
        if op == '*':
            total *= int(rows[row][col])
        else:
            total += int(rows[row][col])
    full_total += total

print(full_total)