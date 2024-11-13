import csv

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data.append(row)
    return data

def conditional_Probability(feature_value, feature_column, target_value, data, target_column):
    count_feature_given_target = 0
    count_target = 0
    
    for row in data:
        if row[target_column] == target_value:
            count_target += 1
        if row[feature_column] == feature_value and row[target_column] == target_value:
            count_feature_given_target += 1

    return count_feature_given_target / count_target


def calcPrior(target, data, target_column):
    count = 0
    for row in data:
        if row[target_column] == target:
            count += 1
    prob = count / len(data)
    return prob

def bayesClassifier(new_instance_features, data, target_column):
    targets = set()
    for row in data:
        targets.add(row[target_column])
    print(targets)

    print("Targets : ", targets)
    target_probabilites = {}

    for target in targets:
        total_prob_target = calcPrior(target, data, target_column)
        print(f"\nP({target}) = {round(total_prob_target, 3)}")

        for feature_index in range(len(new_instance_features)):
            prob_feature_given_target = conditional_Probability(
                feature_value = new_instance_features[feature_index],
                feature_column = feature_index,
                target_value = target,
                data = data,
                target_column = target_column
            )

            print(f"P(Feature[{feature_index}] = {new_instance_features[feature_index]} | {target}) = {round(prob_feature_given_target, 3)}")
            total_prob_target *= prob_feature_given_target

        target_probabilites[target] = total_prob_target
        print(f"Final Probability for '{target}' : {round(total_prob_target, 3)}")

    predicted_target = max(target_probabilites, key=target_probabilites.get)
    return predicted_target

if __name__ == "__main__":
    filename = "data.csv"

    data = read_csv(filename)
    new_instance_features = ['Rainy', 'Mild']

    target_column = 2

    predicted = bayesClassifier(new_instance_features, data, target_column)

    print(f"\nPredicted class for test data {new_instance_features} : {predicted}")