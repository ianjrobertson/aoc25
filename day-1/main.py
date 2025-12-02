def apply(starting, movement):
    times_pass_zero = 0
    direction = movement[0]
    magnitude = int(movement[1:])

    if direction == 'R':
        magnitude *= -1
    
    l_to_zero = abs(starting)
    r_to_zero = 100 - abs(starting)
    num_rotations = abs(magnitude) // 100
    times_pass_zero += num_rotations
    
    if direction == "L":
        if starting != 0 and abs(magnitude) % 100 > l_to_zero:
            times_pass_zero += 1
    else:
        if starting != 0 and abs(magnitude) % 100 > r_to_zero:
            times_pass_zero += 1

    return ((starting - magnitude + 100) % 100, times_pass_zero)


def run(moves):
    current = 50
    times_0 = 0
    for move in moves:
        if move != '':
            #print(f"{current} + {move}")
            current, times_pass_zero = apply(current, move)
            times_0 += times_pass_zero
            if current == 0:
                times_0 += 1
                #print('hit a 0', move, times_0)
    return times_0

moves = []

with open('input.txt') as f:
    for line in f:
        moves.append(line.strip())
    #print(len(moves))
    
print(run(moves))


# if during the rotation, the dial passes 0, that counts. 
# how can you tell? 
# magnitude / 100 -> number of rotations.   


# if you go right and the number is smaller
# if you go 

