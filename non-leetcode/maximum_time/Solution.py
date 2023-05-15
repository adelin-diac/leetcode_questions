import sys

def solution(A):
  if(A.count("?") == 4):
    return "23:59"

  A = A.split(":")
  if A[0].count("?") == 2:
    A[0] = "23"
  elif A[0].count("?") == 0:
    pass
  else:
    pos1 = A[0].find("?")
    match pos1:
      case 0:
        if int(A[0][1]) < 4:
          A[0] = A[0].replace("?", "2")
        else:
          A[0] = A[0].replace("?", "1")
      case 1:
        if int(A[0][0]) == 2:
          A[0] = A[0].replace("?", "3")
        else:
          A[0] = A[0].replace("?", "9")

  if A[1].count("?") == 2:
    A[1] = "59"
  elif A[1].count("?") == 0:
    pass
  else:
    pos1 = A[1].find("?")
    match pos1:
      case 0:
        A[1] = A[1].replace("?", "5")
      case 1:
        A[1] = A[1].replace("?", "9")

  return A[0] + ":" + A[1]

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  sys.stdout.write(str(solution("?4:5?")) + "\n\n")
  sys.stdout.write(str(solution("23:5?"))  + "\n\n")
  sys.stdout.write(str(solution("2?:22"))  + "\n\n")
  sys.stdout.write(str(solution("0?:??"))  + "\n\n")
  sys.stdout.write(str(solution("??:??"))  + "\n\n")

if __name__ == "__main__":
	main()