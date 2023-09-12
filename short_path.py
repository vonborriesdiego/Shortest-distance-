import math
import itertools
import matplotlib.pyplot as plt

#function to calculate distance between all points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

#find the shortest path 
def find_shortest_path(points):
    num_points = len(points)
    indices = list(range(num_points))
    shortest_path = None
    shortest_distance = float('inf')

    for perm in itertools.permutations(indices):
        path_distance = sum(euclidean_distance(points[perm[i]], points[perm[i + 1]]) for i in range(num_points - 1))
        path_distance += euclidean_distance(points[perm[-1]], points[perm[0]])  # Return to the starting point

        if path_distance < shortest_distance:
            shortest_distance = path_distance
            shortest_path = perm

    return shortest_path, shortest_distance

#add coordinates from the mapping track 
L = [(250, 300), (150, 260), (270, 500), (120,240)] #the first point is the starting point 
shortest_path, shortest_distance = find_shortest_path(L)

# Extract the coordinates of the points in the shortest path
shortest_path_points = [L[i] for i in shortest_path]

#Variable that finds the last node
last = shortest_path[-1]
for i, j in enumerate(L):
    if i == last:
        en = L[i]


# Plot the points and the shortest path
x, y = zip(*L)
plt.scatter(x, y, label='Points')
plt.plot(*zip(*shortest_path_points), 'r--', label='Shortest Path')

# Add text labels to the first and last nodes
plt.text(L[0][0], L[0][1], 'Start', fontsize=12, ha='right')
plt.text(en[0], en[1], 'End', fontsize=12, ha='right')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Shortest Path Visualization')
plt.grid(True)
plt.show()

print("Shortest path:", shortest_path)
print("Shortest distance:", shortest_distance)



