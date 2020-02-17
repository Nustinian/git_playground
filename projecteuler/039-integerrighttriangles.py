import numpy as np

u = np.array([[1, 2, 2], [-2, -1, -2], [2, 2, 3]])
a = np.array([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
d = np.array([[-1, -2, -2], [2, 1, 2], [2, 2, 3]])
starter = np.array([3, 4, 5])

next_iteration = [starter]
triangles = [starter]
for i in range(14):
    new_triangles = []
    for triangle in next_iteration:
        if triangle.sum() < 1000:
            triangles.append(triangle.dot(u))
            triangles.append(triangle.dot(a))
            triangles.append(triangle.dot(d))
            new_triangles.append(triangle.dot(u))
            new_triangles.append(triangle.dot(a))
            new_triangles.append(triangle.dot(d))
    next_iteration = new_triangles

sums = [triangle.sum() for triangle in triangles if triangle.sum() < 1000]

answer = 0
for i in range(1, 1000):
    counter = 0
    for num in sums:
        if i % num == 0:
            counter += 1
    if counter > answer:
        answer = counter

print(answer)