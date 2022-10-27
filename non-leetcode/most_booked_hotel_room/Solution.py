import sys
from collections import Counter

def solution(arr):
  return list(Counter(arr).keys())[0].replace("+", "")

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  sys.stdout.write(str(solution(["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"])))

if __name__ == "__main__":
	main()