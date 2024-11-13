import csv

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            region, A, B = row[0], int(row[1]), int(row[2])
            data.append([region, A, B])
    return data

filename = r'data.csv'
data = read_csv(filename=filename)

sumA = sum(row[1] for row in data)
sumB = sum(row[2] for row in data)

tWt = {row[0]: {"A": 0, "B": 0} for row in data}
dWt = {row[0]: {"A": 0, "B": 0} for row in data}

for row in data:
    region, A, B = row
    rtotal = A + B

    tWt[region]["A"] = A / rtotal if rtotal != 0 else 0
    tWt[region]["B"] = B / rtotal if rtotal != 0 else 0

    print(f"A = {A} sumA = {sumA}")
    dWt[region]["A"] = A / sumA if A != 0 else 0
    dWt[region]["B"] = B / sumB if B != 0 else 0


print(f"{'Region':<10} {'A_Total':<10} {'t-weight_A':<15} {'d-weight_A':<15} {'B_Total':<10} {'t-weight_B':<15} {'d-weight_B':<15}")
print("-" * 90)

for row in data:
    region, A, B = row
    print(f"{region:<10} {A:<10} {tWt[region]['A']:<15.4f} {dWt[region]['A']:<15.4f} {B:<10} {tWt[region]['B']:<15.4f} {dWt[region]['B']:<15.4f}")

print("\n total for all regions:")
print(f"{'Total_A':<15} {'Total_B':<15}")
print(f"{sumA:<15} {sumB:<15}")