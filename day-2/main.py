# okay so we get a csv of ranges. 
# from those ranges we need to return the count of invalid ids
# and invalid id is a number that has some sequence of digits repeated twice. 

# split the string in half, if first half is equal to second half, it's repeated. 

ranges = []

with open('input.txt') as f:
    content = f.read()
    values = content.split(',')
    for id_range in values:
        numbers = id_range.split('-')
        ranges.append(numbers)


def getInvalidIds(id_range):
    lower = id_range[0]
    upper = id_range[1]
    total = 0

    for num in range(int(lower), int(upper)+1):
        if isInvalid(str(num)):
            total += num
    
    return total


def isInvalid(num):
    if len(num) % 2 != 0:
        return False

    midpoint = len(num) // 2
    first_half = num[:midpoint]
    second_half = num[midpoint:]
    return first_half == second_half


total = 0
for id_range in ranges:
    total += getInvalidIds(id_range)

print(total)
