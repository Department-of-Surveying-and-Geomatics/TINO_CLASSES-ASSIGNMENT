import csv
import matplotlib.pyplot as plt

class Point:
    """
    A class representing a point in a 2-dimensional space.
    """

    def __init__(self, x, y):
        """
        Initialize the Point object with x and y coordinates.

        Args:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
        """
        self.x = float(x)  # Convert x to float
        self.y = float(y)  # Convert y to float

    def translate(self, dx, dy):
        """
        Move the point by a given displacement in the x and y directions.

        Args:
            dx (float): The displacement in the x direction.
            dy (float): The displacement in the y direction.
        """
        self.x += dx
        self.y += dy

def plot_points(points, color='blue'):
    """
    Plot a list of points on a scatterplot.

    Args:
        points (list): List of Point objects.
        color (str): Color of the plotted points. Default is 'blue'.
    """
    x_values = [point.x for point in points]
    y_values = [point.y for point in points]

    plt.scatter(x_values, y_values, color=color,s=60)

# Read coordinates from the CSV file
points = []
with open("coordinate_file.csv", 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots)  # Skip the header row
    for row in plots:
        try:
            x = float(row[0])
            y = float(row[1])
            points.append(Point(x, y))
        except ValueError:
            print("Skipping non-numeric values in the CSV file.")

# Plot the original points
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph', color='black')
plot_points(points, color='yellow')

# Translate the points by a given displacement
dx = 2.0
dy = 1.5
translated_points = [Point(point.x + dx, point.y + dy) for point in points]

# Plot the translated points
plot_points(translated_points, color='blue')

plt.show()