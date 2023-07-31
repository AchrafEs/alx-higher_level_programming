`0x0C-python-almost_a_circle`

"Almost a circle" is a popular Python programming challenge that involves drawing a shape that closely resembles
a circle using a specific pattern. The goal is to create an illusion of a circle by drawing a set of evenly spaced
points in such a way that, when connected, they appear to form a circular shape.

To achieve this, we use the Python programming language and its libraries to draw the shape on a canvas or a
graphical user interface (GUI). The most commonly used library for such tasks is `matplotlib`.

Here's a step-by-step explanation of how you can create an "almost a circle" shape in Python using `matplotlib`:

1.  Import the necessary libraries:
First, you need to import the required libraries. We will use matplotlib.pyplot for plotting.
```
import matplotlib.pyplot as plt
import numpy as np
```
2.  Define the number of points:
Decide the number of points that you want to use to draw the "almost a circle" shape. More points will make it
appear closer to a circle, but it will also take more time to compute.
```
num_points = 100
```
3.  Generate the points:
To create the points, we'll use trigonometric functions to calculate their positions around a circle. The x and y
coordinates of each point will be determined by the angle at which they are placed around the circle.
```
theta = np.linspace(0, 2 * np.pi, num_points)
x = np.cos(theta)
y = np.sin(theta)
```
4.  Plot the points:
Now, let's use matplotlib to plot the points on a graph. Each point will be represented by a small dot.
```
plt.scatter(x, y, s=10)  # s=10 sets the size of the dots to 10
plt.axis('equal')  # Ensure that the aspect ratio is equal, so the circle appears round
plt.show()
```
When you run this code, you will see a graph with points arranged in a circle-like pattern. By increasing the number
of points in `num_points`, the shape will appear more like a circle. However, be cautious, as using a very large
number of points can slow down the computation significantly.

Keep in mind that this is an approximation of a circle and not a perfect circle, as it is made up of discrete points
rather than a continuous line. The illusion of a circle comes from the density and even distribution of these points.
