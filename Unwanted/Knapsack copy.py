import math


def knapsack_01_brute_force(weights, values, capacity):
    n = len(weights)
    max_value = 0
    all_accepted_weight_sequence = []
    all_accepted_binary_sequence = []
    sequences_values = []

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
            temp = math.floor(temp/2)

        if (weight <= capacity):
            temp = x
            for j in range(n):
                current_binary_sequence.append(temp % 2)
                if temp % 2 != 0:
                    current_weight_sequence.append(weights[j])
                temp = math.floor(temp/2)
            sequences_values.append(value)
            all_accepted_weight_sequence.append(current_weight_sequence)
            all_accepted_binary_sequence.append(current_binary_sequence)

            print(
                f"Total Weight: {weight},\t Total Value: {value},\t Binary form: {current_binary_sequence},\t Total Weight: {weight}, \t Weights Seqences: {current_weight_sequence} ")
    # print(all_accepted_binary_sequence)
    # print(all_accepted_weight_sequence)

    max_value = max(sequences_values)
    max_value_index = sequences_values.index(max(sequences_values))
    return {"max_value": max_value,
            "weight_sequence": all_accepted_weight_sequence[max_value_index],
            "binary_sequence": all_accepted_binary_sequence[max_value_index],
            }
    # return max_value


def knapsack_fractional_greedy(weights, values, capacity):
    n = len(weights)

    # Create a list of items with their weight, value, and value-to-weight ratio
    items = []
    for i in range(n):
        items.append((weights[i], values[i], values[i] / weights[i], i))

    # Sort the items based on their value-to-weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0
    total_weight = 0
    chosen_weights = []
    binary_sequence = [0] * n

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
                chosen_weights.append(remaining_capacity)
                binary_sequence[index] = fraction
            break

    return {"max_value": total_value,
            "weight_sequence": chosen_weights,
            "binary_sequence": binary_sequence,
            }


def knapsack_fractional_brute_force(weights, values, capacity):
    n = len(weights)
    max_value = 0
    all_accepted_weight_sequence = []
    all_accepted_binary_sequence = []
    sequences_values = []

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
                    can_add_weight = remaining_capacity
                    ratio = can_add_weight / weights[j]
                    value += values[j]*ratio
                    weight += weights[j] if weights[j] < remaining_capacity else remaining_capacity
                    current_binary_sequence.append(ratio)
            else:
                current_binary_sequence.append(temp % 2)
            temp = math.floor(temp/2)

        if (weight <= capacity):
            temp = x
            for j in range(n):
                if temp % 2 != 0:
                    current_weight_sequence.append(weights[j])
                temp = math.floor(temp/2)
            sequences_values.append(value)
            all_accepted_weight_sequence.append(current_weight_sequence)
            all_accepted_binary_sequence.append(current_binary_sequence)
            # print("----------------------------------------------------------------")
            # print(
            #     f"==Total Weight: {weight},\t Total Value: {value},\t Binary form: {current_binary_sequence}, \t Weights Seqences: {current_weight_sequence} ")

        if weight < capacity:
            for j in range(n):
                if current_binary_sequence[j] == 0 and weight < capacity:
                    remaining_capacity = capacity-weight
                    if weights[j] < remaining_capacity:
                        ratio = remaining_capacity/capacity if remaining_capacity/capacity < 1 else 1
                        current_binary_sequence[j] = ratio
                        value += values[j]*ratio
                        sequences_values.append(value)
                        weight += weights[j] if weights[j] < remaining_capacity else remaining_capacity
                    else:
                        can_add_weight = remaining_capacity
                        ratio = can_add_weight / weights[j]
                        current_binary_sequence[j] = ratio
                        value += values[j]*ratio
                        sequences_values.append(value)
                        weight += weights[j] if weights[j] < remaining_capacity else remaining_capacity
                    if weight >= capacity:
                        break

            # print(
            #     f"<<Total Weight: {weight},\t Total Value: {value},\t Binary form: {current_binary_sequence}, \t Weights Seqences: {current_weight_sequence} ")

    max_value = max(sequences_values)
    max_value_index = sequences_values.index(max(sequences_values))
    return {"max_value": max_value,
            "weight_sequence": all_accepted_weight_sequence[max_value_index],
            "binary_sequence": all_accepted_binary_sequence[max_value_index],
            }


def knapsack_fractional_dynamic(weights, values, capacity):
    n = len(weights)
    # Initialize DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1]
                               [w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]
    weight_sequence = []
    binary_sequence = []

    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            weight_sequence.append(weights[i - 1])
            binary_sequence.append(1)
            w -= weights[i - 1]
        else:
            binary_sequence.append(0)

    binary_sequence.reverse()
    return {
        "max_value": max_value,
        "weight_sequence": weight_sequence,
        "binary_sequence": binary_sequence
    }


if __name__ == "__main__":
    weights = [56, 60, 23, 56, 12]
    values = [23, 45, 46, 9, 36]
    capacity = 50

    max_value = knapsack_01_brute_force(weights, values, capacity)
    print(
        f"\nThe maximum value that can be put in the knapsack (Brute Force) is {max_value}")

    max_value = knapsack_fractional_dynamic(weights, values, capacity)
    print(
        f"\nThe maximum value that can be put in the knapsack (Dynamic) is {max_value}")

    max_value = knapsack_fractional_greedy(weights, values, capacity)
    print(
        f"\nThe maximum value that can be put in the knapsack (Greedy) is {max_value}")

    max_value = knapsack_fractional_brute_force(weights, values, capacity)
    print(
        f"\nThe maximum value that can be put in the knapsack (Fractional) is {max_value}")


# import math


# def knapsack_01_brute_force(weights, values, capacity):
#     n = len(weights)
#     current_weight_sequence = []
#     current_binary_sequence = []
#     all_accepted_current_weight_sequence = []
#     all_accepted_current_binary_sequence = []
#     sequences_values = []

#     for x in range(int(math.pow(2, len(weights)))):
#         current_weight_sequence = []
#         current_binary_sequence = []
#         value = 0
#         weight = 0
#         temp = x
#         for j in range(n):
#             if temp % 2 != 0:
#                 value = value+values[j]
#                 weight = weight+weights[j]
#             temp = math.floor(temp/2)

#         if (weight <= capacity):

#             temp = x
#             for j in range(n):
#                 current_binary_sequence.append(temp % 2)
#                 if temp % 2 != 0:
#                     current_weight_sequence.append(weights[j])
#                 temp = math.floor(temp/2)
#                 sequences_values.append(value)
#                 all_accepted_current_weight_sequence.append(current_weight_sequence)
#                 all_accepted_current_binary_sequence.append(current_binary_sequence)

#             print(
#                 f"Total Weight: {weight},\t Total Value: {value},\t Binary form: {current_binary_sequence},\t Total Weight: {weight}, \t Weights Seqences: {current_weight_sequence} ")

#     max_value = max(sequences_values)
#     max_value_index = sequences_values.index(max(sequences_values))
#     return {"max_value": max_value,
#             "weight_sequence": all_accepted_current_weight_sequence[max_value_index],
#             "binary_sequence": all_accepted_current_binary_sequence[max_value_index],
#             }

#     # def knapsack_recursive(index, current_weight, current_value, sequence):

#     #     # Base case: no items left
#     #     if index == n:
#     #         all_accepted_sequences.append((sequence, current_weight, current_value))
#     #         return current_value if current_weight <= capacity else 0
#     #     # Case 1: Exclude the current item
#     #     exclude_value = knapsack_recursive(index + 1, current_weight, current_value, sequence.copy())
#     #     # Case 2: Include the current item
#     #     include_value = 0
#     #     if current_weight + weights[index] <= capacity:
#     #         sequence_with_current = sequence.copy()
#     #         sequence_with_current.append(index)
#     #         include_value = knapsack_recursive(index + 1, current_weight + weights[index], current_value + values[index], sequence_with_current)
#     #     # Return the maximum value of the two cases
#     #     return max(exclude_value, include_value)
#     # max_value = knapsack_recursive(0, 0, 0, [])
#     # print("all_accepted sequences of items (0-indexed) and their total weights and values:")
#     # for seq, weight, value in all_accepted_sequences:
#     #     print(f"Items: {seq}, Total Weight: {weight}, Total Value: {value}")
#     # return max_value


# if "__name__" == "__main__":
#     weights = [56, 60, 23, 56, 12]
#     values = [23, 45, 46, 9, 36]
#     capacity = 50

#     max_value = knapsack_01_brute_force(weights, values, capacity)
#     print(
#         f"\nThe maximum value that can be put in the knapsack is {max_value}")
