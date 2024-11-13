import csv
from itertools import combinations

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        items = list(set(item.strip() for row in reader for item in row))

        file.seek(0) # Re-read the file to build the txns
        txns = []
        for row in reader:
            transaction = [item.strip() for item in row]
            txns.append(set(transaction))
    
    return items, txns

def get_itemsets(size, items):
    return list(combinations(items, size))

def calculate_support(itemset, txns):
    count = sum(1 for txn in txns if set(itemset).issubset(txn))
    return count / len(txns) if txns else 0

def apriori(items, txns, min_support):
    all_freq_items = []

    for size in range(1, len(items) + 1):
        itemsets = get_itemsets(size, items)
        freq_items = []

        for itemset in itemsets:
            support = calculate_support(itemset, txns)
            if support >= min_support:
                freq_items.append((itemset, support))

        if not freq_items:
            break
        
        all_freq_items.extend(freq_items)

    return all_freq_items


if __name__ == "__main__":
    filename = 'data.csv'

    items, txns = read_csv(filename=filename)
    

    min_support = float(input("Enter the minimum support(0-1): "))

    freq_items = apriori(items, txns, min_support)
    
    print("\nFrequent itemsets:")

    for itemset, support in freq_items:
        print(f"{list(itemset)}: {support:.2f}")

