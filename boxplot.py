import matplotlib.pyplot as plt
import csv

def read_csv(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    data.append(float(row[0]))
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
    return data

def cal_stat(data):
    if not data:
        return None
    
    data_s = sorted(data)
    n = len(data_s)

    minVal = data_s[0]
    maxVal = data_s[-1]

    if n % 2 == 0:
        median = (data_s[n//2 - 1] + data_s[n//2]) / 2
    else:
        median = data_s[n//2]

    lPart = data_s[:n//2]

    if n % 2 == 0:
        rPart = data_s[n//2:]
    else:
        rPart = data_s[n//2 + 1:]


    if len(lPart) % 2 == 0:
        q1 = (lPart[len(lPart) // 2 - 1] + lPart[len(lPart) // 2]) / 2
    else:
        q1 = lPart[len(lPart) // 2]

    if len(rPart) % 2 == 0:
        q3 = (rPart[len(rPart) // 2 - 1] + rPart[len(rPart) // 2]) / 2
    else:
        q3 = rPart[len(rPart) // 2]

    iqr = q3 - q1

    return minVal, maxVal, q1, median, q3, iqr

if __name__ == "__main__":
    filename = 'data.csv'
    data = read_csv(filename)

    min, max, q1, median, q3, iqr = cal_stat(data)

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = [x for x in data if x < lower or x > upper]

    print(f"Min: {min}, Q1: {q1}, Median: {median}, Q3: {q3}, Max: {max}, IQR: {iqr:.2f}")
    print(f"Outliers: {outliers}")

    plt.figure(figsize=(8,6))
    box = plt.boxplot(data, patch_artist=True)

    colors = ['#FF9999']
    for patch in box['boxes']:
        patch.set_facecolor(colors[0])
        patch.set_edgecolor('black')
        patch.set_linewidth(1.5)

    plt.text(1, min, f'Min: {min:.2f}', verticalalignment='bottom', horizontalalignment='right')
    plt.text(1, max, f'Max: {max:.2f}', verticalalignment='top', horizontalalignment='right')
    plt.text(1, q1, f'Q1: {q1:.2f}', verticalalignment='bottom', horizontalalignment='right')
    plt.text(1, q3, f'Q3: {q3:.2f}', verticalalignment='top', horizontalalignment='right')
    plt.text(1, median, f'Median: {median:.2f}', verticalalignment='bottom', horizontalalignment='right')
    
    for outlier in outliers:
        plt.plot(1, outlier, 'ro')
    
    plt.title('Boxplot of First Column Data with Outliers')
    plt.xticks([1], ['First Column'])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()