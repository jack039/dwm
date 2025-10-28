import numpy as np

# Dataset
dataset = np.array([1, 5, 9, 4, 7, 11, 14, 17, 13, 18, 19, 31, 33, 36, 42, 44, 46, 70, 74, 78, 77])
print("Dataset:", dataset)

# Input number of clusters
k = int(input("Enter the number of clusters (k): "))

# Input initial centroids
centroids = np.array([float(input(f"Enter initial centroid {i+1}: ")) for i in range(k)])

while True:
    # Calculate distances of each point from centroids
    distances = np.abs(dataset[:, np.newaxis] - centroids)

    # Assign each point to the nearest centroid
    labels = np.argmin(distances, axis=1)

    # Calculate new centroids as the mean of the clusters
    new_centroids = np.array([dataset[labels == i].mean() for i in range(k)])

    # If centroids do not change, stop
    if np.all(centroids == new_centroids):
        break

    centroids = new_centroids

print("\nFinal Centroids:", centroids)

#Display clusters
for i in range(k):
    cluster = dataset[labels == i]
    print(f"Cluster {i+1}: {cluster}")
    """Theory

K-Means Clustering is an unsupervised learning algorithm used to group a set of data points into K clusters, where each cluster is represented by its centroid (mean). The algorithm minimizes the variance within clusters and maximizes the variance between clusters.

Algorithm Steps

Initialize K centroids randomly from the dataset.

Assign each data point to the nearest centroid (based on Euclidean distance).

Recalculate centroids by taking the mean of all data points assigned to each cluster.

Repeat Steps 2 and 3 until centroids no longer change (convergence) or a maximum number of iterations is reached."""
