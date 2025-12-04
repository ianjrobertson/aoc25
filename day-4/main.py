rolls = []

with open('input.txt') as f:
    for line in f:
        rolls.append(list(line.strip()))

good_rolls = 0

dr = [(-1,1), (-1,0), (-1,-1), (1,0), (1,-1), (1,1), (0,1), (0,-1)]


while True:
    changed_roll = False
    for row in range(len(rolls)):
        for col in range(len(rolls[0])):
            if rolls[row][col] != '@':
                continue
            num_rolls = 0
            #visited = []
            for r,c in dr:
                nr = row + r
                nc = col + c
                if nr < 0 or nr >= len(rolls) or nc < 0 or nc >= len(rolls[0]):
                    continue
                if rolls[nr][nc] == '@':
                    num_rolls += 1
                    #visited.append((nr,nc))
            
            if num_rolls < 4:
                good_rolls += 1
                rolls[row][col] = '.'
                changed_roll = True
    
    if not changed_roll:
        break

print(good_rolls)