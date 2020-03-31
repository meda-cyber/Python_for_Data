
import seaborn
import numpy as np
import matplotlib.pyplot as plt
# Finish writing the draw_secant() function, which accepts 2 x-values as a list and draws the secant line connecting those 2 points. This function should:
# Determine the y-values for those 2 x-values using our nonlinear function.
# Calculate the slope between those 2 points.
# Calculate the y-intercept using arithmetic.
# Plot the secant line using the color "green".
# Display all of the plots in the function.
# Use the draw_secant() function to generate 3 plots:
# One visualizing the secant line between the x-values 3 and 5.
# One visualizing the secant line between the x-values 3 and 10.
# One visualizing the secant line between the x-values 3 and 15.

seaborn.set(style='darkgrid')


def draw_secant(x_values):
    x = np.linspace(-20, 30, 100)
    y = -1*(x**2) + x*3 - 1
    plt.plot(x, y)
    # Add your code here.
    x_0 = x_values[0]
    x_1 = x_values[1]
    y_0 = -1*(x_0**2) + 3*x_0 - 1
    y_1 = -1*(x_1**2) + 3*x_1 - 1
    m = (y_1 - y_0)/(x_1 - x_0)
    b = y_1 - m*x_1

    y_secant = x*m + b
    plt.plot(x, y_secant, c="green")

    plt.show()


draw_secant([3, 5])
draw_secant([3, 10])
draw_secant([3, 15])
