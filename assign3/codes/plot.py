import matplotlib.pyplot as plt
import numpy as np

def read_points_from_file(filename):
    """Read points and center from the specified file and return them as tuples."""
    points = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("Point"):
                parts = line.split('(')[1].split(')')[0].split(',')
                x, y = float(parts[0]), float(parts[1])
                points.append((x, y))
            elif line.startswith("Center"):
                parts = line.split('(')[1].split(')')[0].split(',')
                x, y = float(parts[0]), float(parts[1])
                center = (x, y)
    return points, center

def calculate_radius(center, point):
    """Calculate the radius of the circle given the center and a point on the circle."""
    return np.sqrt((point[0] - center[0])**2 + (point[1] - center[1])**2)

def plot_circle(ax, center, radius):
    """Plot a circle given the center and radius."""
    circle = plt.Circle(center, radius, color='green', fill=False, linestyle='--', linewidth=1.5)
    ax.add_patch(circle)

def plot_points(points, center):
    """Plot points, center, and circle on a scatter plot."""
    x_vals, y_vals = zip(*points)
    radius = calculate_radius(center, points[0])  # Assuming all points are on the circle

    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Plot points
    ax.scatter(x_vals, y_vals, color='blue', label='Points')
    
    # Plot center
    ax.scatter(center[0], center[1], color='red', label='Center', marker='x', s=100)
    
    # Plot the circle
    plot_circle(ax, center, radius)
    
    # Annotate points and center
    for (x, y) in points:
        ax.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(0,10), ha='center')
    
    ax.annotate(f'Center\n({center[0]:.2f}, {center[1]:.2f})', center, textcoords="offset points", xytext=(0,10), ha='center')
    
    # Labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Plot of Points, Center, and Circle')
    ax.legend()
    ax.grid(True)
    
    # Set equal scaling
    ax.set_aspect('equal', 'box')
    
    # Show plot
    plt.show()

if __name__ == "__main__":
    # Read points and center from file
    points, center = read_points_from_file('circle_data.txt')
    
    # Plot the points, center, and circle
    plot_points(points, center)


