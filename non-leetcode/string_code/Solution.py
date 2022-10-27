import sys

def solution(S):
  count = 0
  for i in range(len(S)-1):
    match(S[i] + S[i+1]):
      case "aa":
        count += 2
      case "ac":
        count += 1
      case "bb":
        count += 2
      case "ba":
        count += 1
      case "cc":
        count += 2
      case "cb":
        count += 1
  return count

# def solution(S):
#   count = 0
#   for i in range(len(S)-1):
#     if S[i] + S[i+1] == "aa":
#       count += 2
#     elif S[i] + S[i+1] == "ac":
#       count += 1
#     elif S[i] + S[i+1] == "bb":
#       count += 2
#     elif S[i] + S[i+1] == "ba":
#       count += 1
#     elif S[i] + S[i+1] == "cc":
#       count += 2
#     elif S[i] + S[i+1] == "cb":
#       count += 1
#   sys.stderr.write(str(count))
#   return count

def main():
  print(solution("aabcc"))

if __name__ == "__main__":
  main()
      