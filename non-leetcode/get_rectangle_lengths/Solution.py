import sys
from collections import Counter

def solution(A):
  min = 4294967295
  sides = []
  count = Counter(A)
  occurences = Counter(A).items()
  for key,value in occurences:
    if value > 1:
      sides.append(key)
  if len(sides) == 1:
    if count[sides[0]] > 3:
      return 0
    else: return -1
  else:
    for i in range(len(sides)):
      for j in range(len(sides)):
        if i == j:
          continue
        if abs(sides[i]-sides[j]) < min:
          min = abs(sides[i]-sides[j])
  return min

def main():
  print(solution([2,2,2]))
  print(solution([2,2,2,2,2]))
  print(solution([911,1,3,1000,1000,2,2,999,1000,911]))

if __name__ == "__main__":
  main()
      