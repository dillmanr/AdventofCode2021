filename = "input.txt"

with open(filename) as f:
    content = f.readlines()

content = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def part1():
    position = (0, 0)
    for line in content:
        move = line.split(" ")

        if move[0] == "forward":
            position = (int(move[1]) + position[0], position[1])
        
        elif move[0] == "down":
            position = (position[0], position[1] + int(move[1]))

        else:
            position = (position[0], position[1] - int(move[1]))

    print(position[0]*position[1])

def part2():
    position = (0,0)
    aim = 0

    for line in content:
        move = line.split(" ")

        if move[0] == "forward":
            position = (int(move[1]) + position[0], position[1] + aim*int(move[1]))
        
        elif move[0] == "down":
            aim += int(move[1])

        else:
            aim -= int(move[1])
    print(position[0]*position[1])

part2()
