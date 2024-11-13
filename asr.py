import csv
from itertools import combinations

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        items = next(reader)
        txns = []
        for row in reader:
            txns.append([int(val) for val in row])
    return items, txns

def gen_itemsets(items, size):
    return list(combinations(range(len(items)), size))

def support(itemset, txns):
    count = 0
    for txn in txns:
        if all(txn[item] == 1 for item in itemset):
            count += 1
    
    return count / len(txns)

def apriori(items, txns, minSupp):
    all_freq_items = []

    for size in range(1, len(items) + 1):
        freqItems = []
        itemsets = gen_itemsets(items, size)

        for itemset in itemsets:
            suppV = support(itemset, txns)
            if suppV >= minSupp:
                freqItems.append((itemset, suppV))
            
        if not freqItems:
            break

        all_freq_items.extend(freqItems)

    return all_freq_items

def confidence(A, B, txns):
    suppA = support(A, txns)
    suppA_B = support(A+B, txns)
    return suppA_B / suppA if suppA != 0 else 0

def gen_rules(freqItems, minConf, txns):
    rules = []

    max_length = 0
    lItemset = None

    for itemset, support in freqItems:
        if len(itemset) > max_length:
            max_length = len(itemset)
            lItemset = itemset
    
    for i in range(1, len(lItemset)):
        for subset in combinations(lItemset, i):
            S = list(subset)
            I_minus_S = list(set(lItemset) - set(S))
            confV = confidence(S, I_minus_S, txns)

            if confV >= minConf:
                rules.append((S, I_minus_S, confV))

    return rules


if __name__ == "__main__":
    filename = 'data.csv'
    items, txns = read_csv(filename)

    # print(items, txns)

    minSupp = float(input("enter the min Support: "))
    minConf = float(input("enter the min Confidence: "))

    freqItems = apriori(items, txns, minSupp)

    print("\n frequ ent Itemsets: ")
    for itemset, suppV in freqItems:
        print(f"{[items[i] for i in itemset]}: {suppV:.2f}")

    rules = gen_rules(freqItems, minConf, txns)

    print("\n association Rules:")
    for A, B, confV in rules:
        print(f"{[items[i] for i in A]} => {[items[i] for i in B]}: {confV:.2f}")