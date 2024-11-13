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
    return headers, data

def write_csv(filename, headers, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for i in range(len(data[headers[0]])):
            writer.writerow([data[header][i] for header in headers])

def min_max(data, new_min, new_max):
    old_min = min(data)
    old_max = max(data)
    print(f"Old Min: {old_min}, Old Max: {old_max}")
    res = []
    for x in data:
        ans = ((x - old_min) * (new_max - new_min) / (old_max - old_min) + new_min)
        res.append(round(ans, 3))
    print(f"New Min: {min(res)}, New Max: {max(res)}")
    return res

def z_score(data):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    res = []
    for x in data:
        ans = (x - mean) / std_dev
        res.append(round(ans, 3))
    return res

def normalize_data(input_file, output_file, method, new_min=0, new_max=1):
    headers, data = read_csv(input_file)

    for header in headers:
        try:
            col_data = [float(x) for x in data[header]]
        except ValueError:
            continue

        if method == 'minmax':
            print(f"\nApplying Min-Max Normalization on column '{header}'")
            data[header] = min_max(col_data, new_min, new_max)
        elif method == 'zscore':
            print(f"\nApplying Z-score Normalization on column '{header}'")
            data[header] = z_score(col_data)

    write_csv(output_file, headers, data)
    print(f"\nNormalization complete! Output saved to {output_file}")

if __name__ == "__main__":
    input_file = 'data.csv'
    output_file = 'normalized_output.csv'
    
    method = input("Choose normalization method (minmax/zscore): ").strip().lower()
    if method == 'minmax':
        new_min = float(input("Enter new min value for Min-Max normalization: "))
        new_max = float(input("Enter new max value for Min-Max normalization: "))
        normalize_data(input_file, output_file, method=method, new_min=new_min, new_max=new_max)
    elif method == 'zscore':
        normalize_data(input_file, output_file, method=method)
    else:
        print("Invalid normalization method chosen.")
