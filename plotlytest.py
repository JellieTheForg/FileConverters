import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import gaussian_kde

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('iris.csv')

# Extract sepal length and sepal width
sepal_length = df['sepal length']
sepal_width = df['sepal width']

# Calculate kernel density estimation
kde = gaussian_kde([sepal_length, sepal_width])
density = kde([sepal_length, sepal_width])

# Create a figure and axis with 3D projection
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set up grid for plotting
x = np.linspace(sepal_length.min(), sepal_length.max(), 100)
y = np.linspace(sepal_width.min(), sepal_width.max(), 100)
X, Y = np.meshgrid(x, y)
Z = np.reshape(kde([X.ravel(), Y.ravel()]), X.shape)

# Create the 3D surface plot
ax.plot_surface(X, Y, Z, cmap="viridis")

# Set labels and title
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_zlabel('Density')
ax.set_title('Iris 3D Density Plot')

# Show the plot
plt.show()
