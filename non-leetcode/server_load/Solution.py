import sys
# WON't GIVE PERFECT SOLUTION
def solution(A):
  A.sort()
  A = A[::-1]
  sum1 = 0
  sum2 = 0
  for load in A:
    if sum1 == 0 and sum2 == 0:
      sum1 = sum1 + load
      continue
    if sum1 > sum2:
      sum2 = sum2 + load
    elif sum2 > sum1:
      sum1 = sum1 + load
    elif sum2 == sum1:
      sum1 = sum1 + load
  return abs(sum1-sum2)

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
#   input = sys.stdin.readline().split()
#   A = [int(x) for x in input[0].split(",")]
  A = [1,2,3,4,5,5,6,7]
  sys.stdout.write(str(solution(A)))

if __name__ == "__main__":
  main()
