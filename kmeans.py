import csv
import math
import random

def readCsv(filename):
    with open(filename, 'r') as file:
        reader = csv.reaader(file)
        next(reader)
        data  = []
        for row in reader:
            data.append([float(value) for value in row])

    return data

def eculidDistance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
                     
def kMeans(dataset, k, max_iter = 100):
    random.seed(42)
    centroids = random.sample(dataset, k)

    for _ in range(max_iter):

        labels = []
        for points in dataset:
            distances = [eculidDistance(points, centroid) for centroid in centroids]
            labels.append(distances.index(min(distances)))
            
        new_centroids = []
        for i in range(k):
            cluster_pts = []
            for j in range(len(dataset)):
                if labels[j] == i:
                    cluster_pts.append(dataset[j])

            if cluster_pts:
                new_centroid = []
                for dim in range(cluster_pts[0]):
                    sum_dim = sum([points[dim] for points in cluster_pts])
                    new_centroid.append(sum_dim / len(cluster_pts))
                new_centroids.append(new_centroid)
            else:
                new_centroids.append(centroids[i])

        if new_centroids == centroids:
            break
        else:
            centroids = new_centroids

    return labels, centroids

if __name__ == "__main__":

    filename = "data.csv"
    data = readCsv(filename)

    clusters = 3

    labels, centroids = kMeans(data, clusters)

    for i in range(clusters):
        print(f"Centroid {i} : {centroids[i]}")

    for i in len(data):
        data[i].append(labels[i])

    for row in data:
        print(row)