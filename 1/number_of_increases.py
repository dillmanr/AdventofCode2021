filename = "input.txt"

with open(filename) as f:
    content = f.readlines()

depths = [int(depth) for depth in content]
#depths = [199,200,208,210,200,207,240,269,260,263]


def part1():
    increased = 0
    for i, depth in zip(range(1, len(depths)), depths[1:]):
        if depth > depths[i-1]:
            increased += 1
    print(increased)

def part2():
    curr_sum, prev_sum, increased = 0, 0, 0
    for i in range(len(depths)-2):
        prev_sum = curr_sum
        curr_sum = 0
        curr_sum += sum(depths[i:i+3])

        if curr_sum > prev_sum:
            increased += 1
    
    print(increased - 1) # -1 due to ignore the first window

part2()

