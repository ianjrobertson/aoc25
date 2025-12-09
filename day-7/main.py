rows = []
with open('test.txt') as f:
    for line in f:
        row = line.strip()
        rows.append(list(row))

