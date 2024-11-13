import csv

def read_csv(filename):
    dataset = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        transactions = [row for row in reader]

    
    unique_items = set(item for transaction in transactions for item in transaction)
    unique_items = list(unique_items)
    unique_items.sort()

    for transaction in transactions:
        row = [1 if item in transaction else 0 for item in unique_items]
        dataset.append(row)

    return dataset, unique_items

def probability(binary_column):
    return sum(binary_column) / len(binary_column)

def joint_probability(column_A, column_B):
    count_union = 0

    for a, b in zip(column_A, column_B):
        if a == 1 or b == 1:
            count_union += 1
    return count_union / len(column_A)

def correlation(column_A, column_B):
    prob_A = probability(column_A)
    prob_B = probability(column_B)
    prob_A_union_B = joint_probability(column_A, column_B)

    if prob_A * prob_B == 0:
        return 0
    
    return prob_A_union_B / (prob_A * prob_B)

def calcCorrMat(dataset):
    num_columns = len(dataset[0])
    correlation_matrix = []

    for i in range(num_columns):
        row = []
        for j in range(num_columns):
            if i == j:
                row.append(1)
            else:
                column_i = [row[i] for row in dataset] 
                column_j = [row[j] for row in dataset]
                corr_value = correlation(column_i, column_j)
                row.append(corr_value)

        correlation_matrix.append(row)

    return correlation_matrix

# def print_correlation_matrix(matrix, item_names):
#     print("Correlation Matrix: ")
#     print("\t" + "\t".join(item_names))
#     for i, row in enumerate(matrix):
#         print(item_names[i] + "\t" + "\t".join(f"{val:.2f}" for val in row))

def print_correlation_matrix(matrix, item_names):
    # Define column width for better alignment
    column_width = max(len(name) for name in item_names) + 2
    header = " " * column_width + "".join(f"{name:<{column_width}}" for name in item_names)
    
    print("Correlation Matrix:\n")
    print(header)  # Print header with item names
    
    for i, row in enumerate(matrix):
        row_name = f"{item_names[i]:<{column_width}}"  # Format row name
        row_values = "".join(f"{val:<{column_width}.2f}" for val in row)  # Format values in the row
        print(row_name + row_values)


if __name__ == "__main__":
    filename = 'data.csv'
    dataset, item_names = read_csv(filename)
    correlation_matrix = calcCorrMat(dataset)
    print_correlation_matrix(correlation_matrix, item_names)