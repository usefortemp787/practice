import csv
import math

def read_csv(filename):
    dataset = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            dataset.append([float(value) for value in row])
    return dataset

def euclidDist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def compute_dist_mat(data):
    n = len(data)
    dist_mat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidDist(data[i], data[j])
            # print(f"{data[i]} , {data[j]} : {dist} , {round(dist, 2)}")
            dist_mat[i][j] = round(dist, 2)
            dist_mat[j][i] = round(dist, 2)

    return dist_mat

def find_closest_clusters(dist_mat):
    min_dist = float('inf')
    cluster_pair = (0, 1)
    n = len(dist_mat)
    for i in range(n):
        for j in range(i + 1, n):
            if dist_mat[i][j] < min_dist:
                min_dist = dist_mat[i][j]
                cluster_pair = (i, j)
    
    return cluster_pair

def merge(cluster1, cluster2):
    return cluster1 + cluster2

def updateDistMat(dist_mat, cluster1, cluster2):
    n = len(dist_mat)
    new_dist_mat = [[dist_mat[i][j] for j in range(n)] for i in range(n)]

    for i in range(n):
        if i not in (cluster1, cluster2):
            ## Use min for single linkage
            new_dist_mat[i][cluster1] = min(dist_mat[i][cluster1], dist_mat[i][cluster2])
            new_dist_mat[cluster1][i] = new_dist_mat[i][cluster1]

    del new_dist_mat[cluster2]
    for row in new_dist_mat:
        del row[cluster2]

    return new_dist_mat

def hierarchical_clustering(data):
    dist_mat = compute_dist_mat(data)
    clusters = [[i] for i in range(len(data))]

    iteration = 1
    while len(clusters) > 1:
        cluster1, cluster2 = find_closest_clusters(dist_mat)
        new_cluster = merge(clusters[cluster1], clusters[cluster2])
        
        print(f"Iter {iteration} : Merging clusters {clusters[cluster1]} and {clusters[cluster2]} into {new_cluster}")

        clusters.append(new_cluster)
        del clusters[max(cluster1, cluster2)]
        del clusters[min(cluster1, cluster2)]

        dist_mat = updateDistMat(dist_mat, cluster1, cluster2)
        iteration += 1

    print(f"\nFinal cluster: {clusters[0]}")
    return clusters[0]


if __name__ == "__main__":
    filename = 'data.csv'
    data = read_csv(filename)
    clusters = hierarchical_clustering(data)
    print(clusters)