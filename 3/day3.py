filename = "input.txt"

with open(filename) as f:
    content = f.readlines()
content = [line.strip() for line in content]
n = len(content[0])
gamma_str = ""
epsilon_str = ""

# sum each column of bits, if the sum is greater than the num of numbers/2, 1 is the most common bit
for i in range(n):
    sum = 0
    for string in content:
        sum += int(string[i])
    gamma_str += str(int(sum > len(content) / 2))
    epsilon_str += str(int(sum <= len(content) / 2))

gamma_rate = int(gamma_str, 2)
epsilon_rate = int(epsilon_str, 2)

print(gamma_rate*epsilon_rate)



