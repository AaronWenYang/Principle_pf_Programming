input_str = 'ablccmdnneofffpg'

longest_length = 0
longest_start = None

current_start = 0
while current_start < len(input_str):
	current_length = 0
	step = 1
	for i in range(current_start + 1, len(input_str)):
		if ord(input_str[i]) - ord(input_str[current_start]) == step:
			current_length += 1
			step += 1
	print(current_length,current_start)	
	
	if current_length > longest_length:
		longest_length = current_length
		longest_start = current_start
	
	while (current_start + 1 < len(input_str)) and (ord(input_str[current_start + 1]) - ord(input_str[current_start]) == 1):
		current_start += 1
	current_start += 1
	
print('long',longest_start,longest_length)
for i in range(longest_length + 1):
	print(chr(ord(input_str[longest_start]) + i),end = '')
print()

