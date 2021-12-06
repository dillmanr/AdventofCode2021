import copy

filename = "input.txt"
#filename = "example_input.txt"

with open(filename) as f:
    content = f.readlines()
content = [line.strip() for line in content]
n = len(content[0])
gamma_str = ""
epsilon_str = ""

def part1():
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

def most_common_bit(content, bit_posn):
	sum = 0
	for string in content:
		sum += int(string[bit_posn])
	return str(int(sum >= len(content) / 2)) # if equal number of 1 and 0 bits, choose 1

def generator_rating(content):
	i = 0
	while len(content) > 1:
		b = most_common_bit(content, i)
		content = list(filter(lambda bit_string: bit_string[i] == b, content))
		i += 1
	return content[0]

def least_common_bit(content, bit_posn):
	sum = 0
	for string in content:
		sum += int(string[bit_posn])
	return str(int(sum < len(content) / 2)) # if 0 and 1 are equally common, choose 0

def scrubber_rating(content):
	i = 0
	while len(content) > 1:
		b = least_common_bit(content, i)
		content = list(filter(lambda bit_string: bit_string[i] == b, content))
		i += 1
	return content[0]

generator_content = copy.deepcopy(content)
scrubber_content = copy.deepcopy(content)


g = generator_rating(generator_content)
s = scrubber_rating(scrubber_content)

life_support_rating = (int(g, 2) * int(s, 2))

print(life_support_rating)