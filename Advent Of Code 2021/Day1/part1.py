with open('input.txt') as f:
    lines = f.readlines()
    lines = [int(line.rstrip()) for line in lines]

    prev_line = lines.pop(0)
    increased = 0

    for line in lines:
        if line > prev_line:
            increased += 1
        prev_line = line
    
    print(f'increased: {increased}')