ranges = []
ids = []

switch = False

with open('input.txt') as f:
    for line in f:
        if line == '\n':
            switch = True
            continue
        line = line.strip()
        if not switch:
            range = line.split('-')
            ranges.append(range)
        else:
            ids.append(line)

#print(ranges)
#print(ids)

def isValid(id):
    for range in ranges:
        if int(range[0]) <= int(id) and int(id) <= int(range[1]):
            #print(id, range)
            return True
    return False

count = 0
for id in ids:
    if isValid(id):
        count += 1
    
print(count)