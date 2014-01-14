odd = lambda n: 3*n+1
even = lambda n: n/2

current_value = 2
max_value = 0

current_step_value = 0
current_step_count = 0
maximum_step_count = 0

while current_value < 1e6:
	current_step_value = current_value
	while True:
		if current_step_value == 1: break
		if current_step_value%2 == 0: current_step_value = even(current_step_value)
		else: current_step_value = odd(current_step_value)
		current_step_count+=1
	if current_step_count > maximum_step_count:
		maximum_step_count = current_step_count
		max_value = current_value
	current_value += 1
	current_step_count = 0
	print current_value, max_value, maximum_step_count

