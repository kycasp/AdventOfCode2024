f = open("day3input.txt","r")
f_string = f.read()
mul_split = f_string.split("mul")

def generate_do_list(input_str):
	do_list_str = ''
	enabled = True
	for i in range(0,len(input_str)):
		if i + 7 < len(input_str):
			if input_str[i:i+7] == "don't()":
				enabled = False
		if enabled:
			do_list_str += input_str[i]
		elif i + 4 < len(input_str):
			if input_str[i:i+4] == "do()":
				enabled = True

	return do_list_str.split("mul")
	

def compile_muls(mul_list):
	sum_of_products = 0
	for split in mul_list:
		sum_of_products += compute_mul(split)
	print(sum_of_products)
		
		
def compute_mul(mul_str):
	first_num = ''
	second_num = ''
	passed_comma = False
	if mul_str[0] == "(":
		for char in mul_str[1:]:	
			if char == ")":
				break
			elif char == ",":
				passed_comma = True
			elif char.isdigit() and not passed_comma:
				first_num += char
			elif char.isdigit() and passed_comma:
				second_num += char
			else:
				return 0

		return int(first_num) * int(second_num)
	else: 
		return 0

compile_muls(generate_do_list(f_string))