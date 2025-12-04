def maxPair(num):
    print(len(num))
    max_pair = 0
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            pair = int(num[i] + num[j])
            if pair > max_pair:
                max_pair = pair
    
    return max_pair

def max12(num):
    max_num = 0

# the biggest 12 digit number you can make
# you still need to respect relative order of the numbers. 

# in one pass, can you compute the maximum 

nums = []

with open('input.txt') as f:
    for line in f:
        nums.append(line.strip())

jottage = 0
for num in nums:
    jottage += maxPair(num)

print(jottage)