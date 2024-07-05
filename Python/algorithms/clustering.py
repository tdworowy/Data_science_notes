from sklearn import cluster
import pandas as pd
from random import randint
import matplotlib.pyplot as plt


def generate_data_clusters():
    x = [randint(1, 150) for _ in range(80)]
    y = [randint(50, 100) if x[y] < 75 else randint(1, 50) for y in range(80)]
    return pd.DataFrame({"x": x, "y": y})


def plot(x: int, y: int, centers: list, colors):
    plt.scatter(x, y, s=10, c=colors)
    for point in centers:
        plt.scatter(point[0], point[1], s=100)
    plt.show()


if __name__ == "__main__":
    """K Means"""
    data = generate_data_clusters()
    k_means = cluster.KMeans(n_clusters=2)
    k_means.fit(data)

    centroids = k_means.cluster_centers_
    labels = k_means.labels_

    plot(data["x"], data["y"], centroids, labels)

    """hierarchical clustering"""
    hclust = cluster.AgglomerativeClustering(
        n_clusters=2, affinity="euclidean", linkage="ward"
    )
    hclust.fit(data)
    plot(data["x"], data["y"], [], hclust.labels_)
