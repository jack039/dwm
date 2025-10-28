import matplotlib.pyplot as plt

# Sample dataset
x = [5, 7, 8, 10, 12, 15, 18, 20, 23, 25]
y = [15, 17, 18, 21, 24, 25, 28, 30, 32, 35]

# Create scatter plot
plt.scatter(x, y, color='blue', marker='o')

# Add labels and title
plt.title("Scatter Plot of Sample Dataset")
plt.xlabel("X - Values")
plt.ylabel("Y - Values")

# Display plot
plt.show()
'''A scatter plot is a type of data visualization that displays values for two numerical variables using dots.
Each dot represents a data point, where:

The x-axis shows one variable.

The y-axis shows another variable.

It helps in identifying patterns, correlations, and outliers in the dataset.'''