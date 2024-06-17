import math

# Define the knapsack problem


def knapsack_01_brute_force(weights, values, capacity):
    # Initialize variables
    n = len(weights)
    max_value = 0
    all_accepted_weight_sequence = []
    all_accepted_binary_sequence = []
    sequences_values = []

    # Iterate over all possible combinations of items
    for x in range(1 << n):
        value = 0
        weight = 0
        current_binary_sequence = []
        current_weight_sequence = []
        temp = x
        for j in range(n):
            if temp % 2 != 0:
                value += values[j]
                weight += weights[j]
            current_binary_sequence.append(temp % 2)
            temp = math.floor(temp/2)

        # Check if the total weight is within the knapsack capacity
        if (weight <= capacity):
            temp = x
            for j in range(n):
                if temp % 2 != 0:
                    current_binary_sequence.append
                    current_weight_sequence.append(weights[j])
                temp = math.floor(temp/2)
            sequences_values.append(value)
            all_accepted_weight_sequence.append(current_weight_sequence)
            all_accepted_binary_sequence.append(current_binary_sequence)

    # Find the maximum value
    max_value = max(sequences_values)
    max_value_index = sequences_values.index(max(sequences_values))
    return {"max_value": max_value,
            "weight_sequence": all_accepted_weight_sequence[max_value_index],
            "binary_sequence": all_accepted_binary_sequence[max_value_index],
            }


# Define the fractional dynamic programming algorithm
def knapsack_01_dynamic(weights, values, capacity):
    n = len(weights)

    # Initialize the dynamic programming table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the dynamic programming table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1]
                               [w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Find the maximum value
    max_value = dp[n][capacity]
    weight_sequence = []
    binary_sequence = []

    # Reconstruct the optimal solution
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            weight_sequence.append(weights[i - 1])
            binary_sequence.append(1)
            w -= weights[i - 1]
        else:
            binary_sequence.append(0)

    binary_sequence.reverse()
    weight_sequence.reverse()
    return {
        "max_value": max_value,
        "weight_sequence": weight_sequence,
        "binary_sequence": binary_sequence
    }


# Define the fractional greedy algorithm
def knapsack_fractional_greedy(weights, values, capacity):
    n = len(weights)

    # Sort items by value-to-weight ratio
    items = []
    for i in range(n):
        items.append((weights[i], values[i], values[i] / weights[i], i))

    items.sort(key=lambda x: x[2], reverse=True)

    # Initialize variables
    total_value = 0
    total_weight = 0
    chosen_weights = []
    binary_sequence = [0] * n

    # Select items until the knapsack capacity is reached
    for weight, value, ratio, index in items:
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value
            chosen_weights.append(weight)
            binary_sequence[index] = 1
        else:
            remaining_capacity = capacity - total_weight
            if remaining_capacity > 0:
                fraction = remaining_capacity / weight
                total_value += value * fraction
                total_weight += remaining_capacity
                binary_sequence[index] = fraction
            break

    return {"max_value": total_value,
            "weight_sequence": chosen_weights,
            "binary_sequence": binary_sequence,
            }


# Define the fractional brute force algorithm
def knapsack_fractional_brute_force(weights, values, capacity):
    n = len(weights)
    max_value = 0
    all_accepted_weight_sequence = []
    all_accepted_binary_sequence = []
    sequences_values = []

    # Iterate over all possible combinations of items
    for x in range(1 << n):
        value = 0
        weight = 0
        current_binary_sequence = []
        current_weight_sequence = []
        temp = x
        for j in range(n):
            if temp % 2 != 0:
                remaining_capacity = capacity-weight
                if weights[j] < remaining_capacity:
                    value += values[j]
                    weight += weights[j]
                    current_binary_sequence.append(temp % 2)
                else:
                    ratio = remaining_capacity / weights[j]
                    value += values[j]*ratio
                    weight += weights[j] if weights[j] < remaining_capacity else remaining_capacity
                    current_binary_sequence.append(ratio)
            else:
                current_binary_sequence.append(temp % 2)
            temp = temp//2

        # Check if the total weight is within the knapsack capacity
        if (weight <= capacity):
            temp = x
            for j in range(n):
                if temp % 2 != 0:
                    current_weight_sequence.append(weights[j])
                temp = math.floor(temp/2)

        # Check if there is remaining capacity
        if weight < capacity:
            for j in range(n):
                if current_binary_sequence[j] == 0 and weight < capacity:
                    remaining_capacity = capacity-weight
                    if weights[j] <= remaining_capacity:
                        ratio = remaining_capacity/capacity if remaining_capacity/capacity < 1 else 1
                        current_binary_sequence[j] = ratio
                        current_weight_sequence.append(weights[j])
                        value += values[j]*ratio
                        weight += weights[j] if weights[j] < remaining_capacity else remaining_capacity
                    else:
                        can_add_weight = remaining_capacity
                        ratio = can_add_weight / weights[j]
                        current_binary_sequence[j] = ratio
                        # current_weight_sequence.append(weights[j])
                        value += values[j]*ratio
                        weight += weights[j] if weights[j] < remaining_capacity else remaining_capacity
                    if weight >= capacity:
                        break

        if weight <= capacity:
            sequences_values.append(value)
            all_accepted_weight_sequence.append(current_weight_sequence)
            all_accepted_binary_sequence.append(current_binary_sequence)
    if sequences_values:
        # Find the maximum value
        max_value = max(sequences_values)
        max_value_index = sequences_values.index(max(sequences_values))
        return {"max_value": max_value,
                "weight_sequence": all_accepted_weight_sequence[max_value_index],
                "binary_sequence": all_accepted_binary_sequence[max_value_index],
                }
    else:
        return {"max_value": 0,
                "weight_sequence": [],
                "binary_sequence": [],
                }


# Main function
if __name__ == "__main__":
    weights = [1, 2, 3]
    values = [10, 15, 40]
    capacity = 6
    # weights = [3, 4, 9]
    # values = [5, 10, 100]
    # capacity = 8
    # weights = [1, 3, 4, 5]
    # values = [1, 4, 5, 7]
    # capacity = 7
    # weights = [2, 2, 2]
    # values = [10, 20, 30]
    # capacity = 5
    # weights = [56, 60, 23, 56, 12]
    # values = [23, 45, 46, 9, 36]
    # capacity = 50

    # Run the algorithms
    max_value = knapsack_01_brute_force(weights, values, capacity)
    print(
        f"\nThe maximum value that can be put in the knapsack (Brute Force) is {max_value}")

    max_value = knapsack_01_dynamic(weights, values, capacity)
    print(
        f"\nThe maximum value that can be put in the knapsack (Dynamic) is {max_value}")

    max_value = knapsack_fractional_greedy(weights, values, capacity)
    print(
        f"\nThe maximum value that can be put in the knapsack (Greedy) is {max_value}")

    max_value = knapsack_fractional_brute_force(weights, values, capacity)
    print(
        f"\nThe maximum value that can be put in the knapsack (Fractional) is {max_value}")
