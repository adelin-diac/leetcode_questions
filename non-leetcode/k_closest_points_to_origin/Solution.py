import ast

def solution(points, k):
  closest = []
  distances = {}
  for point in points:
    distances[str(point)] = round(((point[0]**2 + point[1]**2)**0.5), 5)
  sorted_distances = sorted(distances.items(), key=lambda item:item[1])
  for i in range(0, k):
    closest.append(ast.literal_eval(sorted_distances[i][0]))
  return closest

def main():
  print(solution(points = [[1,3],[-2,2]], k = 1))
  print(solution(points = [[3,3],[5,-1],[-2,4]], k = 2))

if __name__ == "__main__":
  main()