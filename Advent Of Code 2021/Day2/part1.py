with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

    horizontal = 0
    depth = 0

    for line in lines:
        command, movement = line.split(" ")

        if command == 'forward':
            horizontal += int(movement)
        elif command == 'up':
            depth -= int(movement)
        elif command == 'down':
            depth += int(movement)

    print(f'horizontal position: {horizontal}', f'depth: {depth}')
    print(f'product:{horizontal * depth}')