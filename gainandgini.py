import csv
import math

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            data.append(row)
    return data

def entropy(probs):
    ent = 0
    for p in probs:
        ent -= p * math.log2(p)
    return ent

def get_entropy(data, tgtI):
    tgtV = [row[tgtI] for row in data]
    total = len(tgtV)
    valCnts = {val : tgtV.count(val) for val in set(tgtV)}
    probs = [count / total for count in valCnts.values()]
    return entropy(probs)



def gain(data, attr_idx, tgtI):
    entropyT = get_entropy(data, tgtI)
    attrV = [row[attr_idx] for row in data]
    uniqueV = set(attrV)

    entropyV = 0
    for val in uniqueV:
        subset = []
        for row in data:
            if row[attr_idx] == val:
                subset.append(row)
        weight = len(subset) / len(data)
        entropyV += weight * get_entropy(subset, tgtI)
    return entropyT - entropyV 

def gini_index(probs):
    return 1 - sum([p**2 for p in probs])


def get_gini_index(data, tgtI):
    tgtV = [row[tgtI] for row in data]
    total = len(tgtV)
    valCnts = {val : tgtV.count(val) for val in set(tgtV)}
    probs = [count / total for count in valCnts.values()]
    return gini_index(probs)

def gini_for_attribute(data, attr_idx, tgtI):
    
    attrV = [row[attr_idx] for row in data]
    uniqueV = set(attrV)

    weighted_gini = 0
    for val in uniqueV:
        subset = []
        for row in data:
            if row[attr_idx] == val:
                subset.append(row)
        weight = len(subset) / len(data)
        subset_gini = get_gini_index(subset, tgtI)
        weighted_gini += weight * subset_gini

    return weighted_gini

if __name__ == "__main__":
    filename = r'data.csv'
    data = read_csv(filename=filename)

    attr_weather = 0
    attr_temp = 1
    tgtI = 2
    
    gain_weather = gain(data, attr_weather, tgtI)
    gain_temp = gain(data, attr_temp, tgtI)

    gini_weather = gini_for_attribute(data, attr_weather, tgtI)
    gini_temp = gini_for_attribute(data, attr_temp, tgtI)

    print(f"gain  for 'weather': {gain_weather:.4f}")
    print(f"gain for 'Temperature': {gain_temp:.4f}")
    print(f"gini index for 'Weather': {gini_weather:.4f}")
    print(f"gini index for 'Temperature': {gini_temp:.4f}")
