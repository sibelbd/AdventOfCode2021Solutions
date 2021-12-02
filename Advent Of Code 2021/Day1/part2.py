with open('input.txt') as f:
    lines = f.readlines()
    lines = [int(line.rstrip()) for line in lines]

    increased = 0

    prev_avg = (lines[0] + lines[1] + lines[2])/ 3

    i1 = 1
    i2 = 2 
    i3 = 3

    while i3 < len(lines):
        avg = (lines[i1] + lines[i2] + lines[i3])/ 3
        if avg > prev_avg:
            increased += 1
        prev_avg = avg

        i1 += 1 
        i2 += 1 
        i3 += 1
    
    print(f'increased: {increased}')