import sys
# SHOULD WORK FOR ALL ARRAYS, ONLY PROBLEM IS INNEFICIENCY
def solution(A):
	rows = []
	for height in A:
		added = False
		for row in rows:
			if height < min(row):
				row.append(height)
				added = True
				break
		if(added):
			continue
		rows.append([height])
	print(rows)
	return len(rows)

def main():
	"""Read from stdin, solve the problem, write answer to stdout."""
	# input = sys.stdin.readline().split()
	# A = [int(x) for x in input[0].split(",")]
	A = [5,4,3,6,1,4,3,3,2]
	sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
	main()
