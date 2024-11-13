import math
import csv

def read_csv(filename):
    pts = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # next(reader)
        for row in reader:
            pts.append([float(value) for value in row])
    return pts

def calcCentroid(pts):
    ndims = len(pts[0])
    centroid = []
    for dim in range(ndims):
        total = sum(x[dim] for x in pts)
        centroid.append(round(total / len(pts), 3))

    return centroid

def eucDist(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def calcArr(pts, centroid):
    n = len(pts)
    arr = [[0] * n for x in range(n)]

    for i in range(n):
        for j in range(i + 1):
            arr[i][j] = eucDist(pts[i], centroid)
    
    return arr

if __name__ == "__main__":
    filename = 'data.csv'
    pts = read_csv(filename)

    centroid = calcCentroid(pts)
    print("Cluster Centroid: ", centroid)

    arr = calcArr(pts, centroid)

    print("\nlower triangular distance matrix: ")

    for i in range(len(arr[0])):
        for j in range(i+1):
            print(round(arr[i][j], 2), end = " ")
        print("\n")