import csv

def read_csv_data(filename):
    x = []
    y = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))

    return x, y

def mean(values):
    return sum(values) / len(values)

def linearRegCoeff(x, y):

    data = list(zip(x, y))

    n = len(x)
    XY = 0
    X = 0
    Y = 0
    X2 = 0

    for x, y in data:
        XY += (x * y)
        X += x
        Y += y
        X2 += (x ** 2)

    meanXY = XY / n
    meanX = X / n
    meanY = Y / n
    meanX2 = X2 / n

    nr = meanXY - meanX * meanY
    dr = meanX2 - meanX ** 2

    m = nr / dr
    c = meanY - m * meanX

    m = round(m, 3)
    c = round(c, 3)

    return c, m

if __name__ == "__main__":
    filename = 'data.csv'

    x, y = read_csv_data(filename)

    intercept, slope = linearRegCoeff(x, y)
    print(f"slope (m): {slope}")
    print(f"Intercept (c): {intercept}")
