import numpy as np

u = np.array([[1, 2, 2], [-2, -1, -2], [2, 2, 3]])
a = np.array([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
d = np.array([[-1, -2, -2], [2, 1, 2], [2, 2, 3]])
starter = np.array([3, 4, 5])

correct_triangle = []
next_iteration = [starter]

while len(correct_triangle) == 0:
  new_triangles = []
  for triangle in next_iteration:
    new_triangles.append(triangle.dot(u))
    new_triangles.append(triangle.dot(a))
    new_triangles.append(triangle.dot(d))
  for triangle in new_triangles:
    if 1000 % triangle.sum() == 0:
      correct_triangle.append(triangle * (1000 / triangle.sum()))
  next_iteration = new_triangles

print(correct_triangle)

