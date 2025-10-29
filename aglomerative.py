import math


def euclidean_distance(a, b):
    return math.sqrt((a - b) ** 2)


def find_closest_clusters(clusters):
    min_distance = float('inf')
    pair = (0, 0)
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            
            distance = min(euclidean_distance(x, y) for x in clusters[i] for y in clusters[j])
            if distance < min_distance:
                min_distance = distance
                pair = (i, j)
    return pair

def agnes(data):
    clusters = [[x] for x in data]
    print("Initial Clusters:", clusters)

    step = 1
    while len(clusters) > 1:
        i, j = find_closest_clusters(clusters)
        print(f"\nMerging clusters: {clusters[i]} and {clusters[j]}")

        # Merge clusters i and j
        clusters[i].extend(clusters[j])
        del clusters[j]

        print(f"Updated clusters after step {step}: {clusters}")
        step += 1

    print("\nFinal Cluster:", clusters)

data_points = [18, 22, 25, 27, 42, 43]

agnes(data_points)
'''
Agglomerative Hierarchical Clustering (AGNES) is a bottom-up clustering approach.
Initially, each data point is treated as an individual cluster.
Then, pairs of clusters are merged step by step based on their similarity (or minimum distance) until all points belong to a single cluster or the desired number of clusters is formed.

It creates a hierarchical structure (a tree-like structure called a dendrogram) showing how clusters are merged.'''