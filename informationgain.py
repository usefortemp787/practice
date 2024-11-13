import csv
import math

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            data.append(row)
    return data

def Entropy(probs):
    print(f"probability : {probs}")
    entp = 0
    for p in probs:
        if p != 0:
            entp -= p * math.log2(p)
    print(f"entropy calculated : {round(entp,3)}")
    return entp

def get_entropy(data, tgtI):
    tgtV = [row[tgtI] for row in data]
    print(f"target values : {tgtV}")
    
    total = len(tgtV)
    print(f"total entries : {total}")
    
    val_counts = {}
    for val in set(tgtV):
        val_counts[val] = tgtV.count(val)
    print(f"value counts : {val_counts}")
    
    probs = []
    for count in val_counts.values():
        probs.append(round((count / total),2))
    
    return Entropy(probs)

def Gain(data, attr_idx, tgtI):
    print(f"\n Gain for attribute {attr_idx}")
    total_entropy = get_entropy(data, tgtI)
    print(f"total entropy: {total_entropy}")
    
    attr_vals = [row[attr_idx] for row in data]
    print(f"attribute values : {attr_vals}")
    
    unique_vals = set(attr_vals)
    print(f" unique attribute vals : {unique_vals}")
    
    weighted_entropy = 0
    for val in unique_vals:
        subset = [row for row in data if row[attr_idx] == val]
        print(f"\n subset for attr Value '{val}': {subset}")
        
        weight = len(subset) / len(data)
        print(f"wt. of subset : {round(weight,3)}")
        
        subset_entropy = get_entropy(subset, tgtI)
        print(f"subset entropy: {round(subset_entropy,3)}")
        
        weighted_entropy += weight * subset_entropy
        print(f"updated weight entropy: {round(weighted_entropy,3)}")
    
    info_gain = total_entropy - weighted_entropy
    print(f"Information Gain: {round(info_gain,3)}\n")
    return info_gain


filename = 'data.csv'
data = read_csv(filename)

# Attribute indices
attr_weather = 0  # Weather column
attr_temp = 1     # Temperature column
tgtI = 2          # Target column (Play)

# Calculate Information Gain
info_gain_weather = Gain(data, attr_weather, tgtI)
info_gain_temp = Gain(data, attr_temp, tgtI)

# Output results
print(f"Info Gain for 'Weather': {info_gain_weather:.4f}")
print(f"Info Gain for 'Temperature': {info_gain_temp:.4f}")
