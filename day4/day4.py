f = open("day4input.txt","r")
f_string = f.read()
crossword = f_string.split("\n")

def solvePartOne(crossword):
	totalXmas = 0

	for i in range(0,len(crossword)):
		for j in range(0,len(crossword[i])):
			if crossword[i][j] == "X":
				if i >= 3 and j >= 3:
					#topLeft
					if crossword[i-1][j-1] == "M":
						if crossword[i-2][j-2] == "A":
							if crossword[i-3][j-3] == "S":
								totalXmas += 1
	
				if i >= 3:
					#top
					if crossword[i-1][j] == "M":
						if crossword[i-2][j] == "A":
							if crossword[i-3][j] == "S":
								totalXmas += 1
	
				if i >= 3 and j <= len(crossword[i]) - 4:
					#topRight
					if crossword[i-1][j+1] == "M":
						if crossword[i-2][j+2] == "A":
							if crossword[i-3][j+3] == "S":
								totalXmas += 1
	
				if j <= len(crossword[i]) - 4:
					#right
					if crossword[i][j+1] == "M":
						if crossword[i][j+2] == "A":
							if crossword[i][j+3] == "S":
								totalXmas += 1
	
				if i <= len(crossword) - 4 and j <= len(crossword[i]) - 4:
					#bottomRight
					if crossword[i+1][j+1] == "M":
						if crossword[i+2][j+2] == "A":
							if crossword[i+3][j+3] == "S":
								totalXmas += 1
	
				if i <= len(crossword) - 4:
					#bottom
					if crossword[i+1][j] == "M":
						if crossword[i+2][j] == "A":
							if crossword[i+3][j] == "S":
								totalXmas += 1
	
				if i <= len(crossword) - 4 and j >= 3:
					#bottomLeft
					if crossword[i+1][j-1] == "M":
						if crossword[i+2][j-2] == "A":
							if crossword[i+3][j-3] == "S":
								totalXmas += 1
	
				if j >= 3:
					#left
					if crossword[i][j-1] == "M":
						if crossword[i][j-2] == "A":
							if crossword[i][j-3] == "S":
								totalXmas += 1
	
			else:
				continue

	return totalXmas

def solvePartTwo(crossword):
	totalXmas = 0

	for i in range(0,len(crossword)):
		for j in range(0,len(crossword[i])):
			if crossword[i][j] == "A" and len(crossword) - 1 > i > 0 and len(crossword[i]) - 1 > j > 0:
				
				if crossword[i-1][j-1] == "M" and crossword[i+1][j-1] == "M":
					if crossword[i-1][j+1] == "S" and crossword[i+1][j+1] == "S":
						totalXmas += 1

				if crossword[i-1][j-1] == "M" and crossword[i-1][j+1] == "M":
					if crossword[i+1][j-1] == "S" and crossword[i+1][j+1] == "S":
						totalXmas += 1
					
				if crossword[i-1][j+1] == "M" and crossword[i+1][j+1] == "M":
					if crossword[i-1][j-1] == "S" and crossword[i+1][j-1] == "S":
						totalXmas += 1

				if crossword[i+1][j-1] == "M" and crossword[i+1][j+1] == "M":
					if crossword[i-1][j-1] == "S" and crossword[i-1][j+1] == "S":
						totalXmas += 1
	
			else:
				continue

	return totalXmas

print("Part One:", solvePartOne(crossword))
print("Part Two:", solvePartTwo(crossword))