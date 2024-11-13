import csv

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = {header: [] for header in headers}

        for row in reader:
            for i, value in enumerate(row):
                try:
                    data[headers[i]].append(float(value))
                except ValueError:
                    data[headers[i]].append(value)

        # print(data)

    return headers, data

def BinByMean(arr, n):
    sarr = sorted(arr)
    bin_size = len(sarr) // n
    res = []

    for i in range(0, len(sarr), bin_size):
        subarr = arr[i:i+bin_size]
        mean = sum(subarr) / len(subarr)
        tempbin = []
        for _ in range(0, bin_size):
            tempbin.append(round(mean,3))
        res.append(tempbin)
    
    return res

def BinByBoundary(arr, n):
    sarr = sorted(arr)
    bin_size = len(sarr) // n
    res = []

    for i in range(0, len(sarr), bin_size):
        bin = sarr[i : i + bin_size]
        binMin = min(bin)
        binMax = max(bin)
        tempbin = []

        for x in bin:
            if abs(x - binMin) < abs(x - binMax):
                tempbin.append(binMin)
            else:
                tempbin.append(binMax)
        
        res.append(tempbin)

    return res

if __name__ == "__main__":
    header, arr = read_csv("data.csv")
    arr = arr[header[0]]
    n = int(input("Enter the number of bins : "))

    binned_mean = BinByMean(arr, n)
    print("Binned by mean: ", binned_mean)

    binned_boundary = BinByBoundary(arr, n)
    print("Binnned by boundary: ", binned_boundary)