import csv

def load_input():
	list_of_reports = []
	with open('day2input.csv', 'r') as file:
		csv_reader = csv.reader(file)
		for report in csv_reader:
			report_entry = []
			for level in report:
				report_entry = level.split()
				report_entry = [int(x) for x in report_entry]
			list_of_reports.append(report_entry)
		
		return list_of_reports

def is_increasing(report, bad_level):
	for i in range (1,len(report)):
		if report[i-1] > report[i] or 1 > abs(report[i] - report[i-1]) or abs(report[i] - report[i-1]) > 3:
			if bad_level > 0:
				return False
			if i+1 < len(report):
				if report[i-1] > report[i+1] or 1 > abs(report[i-1] - report[i+1]) or abs(report[i-1] - report[i+1]) > 3:
					return is_increasing(report[:i-1] + report[i:], 1)
				else:
					return is_increasing(report[:i] + report[i+1:], 1)
	return True

def is_decreasing(report, bad_level):
	for i in range (1,len(report)):
		if report[i-1] < report[i] or 1 > abs(report[i-1] - report[i]) or abs(report[i-1] - report[i]) > 3:
			if bad_level > 0:
				return False
			if i+1 < len(report):
				if report[i-1] < report[i+1] or 1 > abs(report[i-1] - report[i+1]) or abs(report[i-1] - report[i+1]) > 3:
					return is_decreasing(report[:i-1] + report[i:], 1)
				else:
					return is_decreasing(report[:i] + report[i+1:], 1)

	return True

def solve(list_of_reports):
	total_safe_reports = 0
	
	for report in list_of_reports:
		if is_decreasing(report, 0) or is_increasing(report, 0):
			total_safe_reports += 1

	print(total_safe_reports)

list_of_reports = load_input()
solve(list_of_reports)