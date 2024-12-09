import csv

def load_input():
	with open('day1input.csv', 'r') as file:
		csv_reader = csv.reader(file)
		for row in csv_reader:
			return row
	
def solve(input_l):
	left_list = []
	right_list = []
	for i in range(0,len(input_l)):
		if (i % 2 == 0):
			left_list.append(int(input_l[i]))
		else:
			right_list.append(int(input_l[i]))
		
	left_list.sort()
	right_list.sort()

	calculate_total_difference(left_list, right_list)
	calculate_similarity(left_list, right_list)
	
def calculate_total_difference(left_list, right_list):
	total_difference = 0
	for i in range(0,len(left_list)):
		total_difference += abs(left_list[i] - right_list[i])

	print(total_difference)
	
def calculate_similarity(left_list, right_list):
	similarity = 0
	for i in range(0,len(left_list)):
		similarity += left_list[i] * right_list.count(left_list[i])

	print(similarity)

input_list = load_input()
solve(input_list)