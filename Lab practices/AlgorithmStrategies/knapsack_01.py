import unittest


def knapsack_01_brute_force(weight, values, capacity):
    n = len(weight)
    binary_sequence = []
    weight_sequence = []
    total_weight_sequence = []
    total_profit_sequence = []
    accepted_weight = []
    accepted_profit = []
    for i in range(pow(2, n)):
        current_binary_sequence = []
        current_weight_sequence = []
        current_weight = 0
        current_profit = 0
        temp = i
        index = 0
        for j in range(n):
            bin = temp % 2
            current_binary_sequence.append(bin)
            if bin == 1:
                current_weight_sequence.append(weight[index])
                current_weight += weight[index]
                current_profit += values[index]
            index = index+1
            temp = temp//2
        binary_sequence.append(current_binary_sequence)
        weight_sequence.append(current_weight_sequence)
        total_weight_sequence.append(current_weight)
        total_profit_sequence.append(current_profit)
        # print(
        #     f"{i}==> {binary_sequence[i]}==>{weight_sequence[i]}==>{total_weight_sequence[i]}==>{total_profit_sequence[i]}")

        for i in range(len(total_weight_sequence)):
            if (total_weight_sequence[i] <= capacity):
                accepted_weight.append(total_weight_sequence[i])
                accepted_profit.append(total_profit_sequence[i])
    optimal_index = total_profit_sequence.index(max(accepted_profit))
    return {"max_value": total_profit_sequence[optimal_index],
            "weight_sequence": weight_sequence[optimal_index],
            "binary_sequence": binary_sequence[optimal_index],
            }


def knapsack_fractional_brute_force(weight, values, capacity):
    n = len(weight)
    binary_sequence = []
    weight_sequence = []
    total_weight_sequence = []
    total_profit_sequence = []
    accepted_weight = []
    accepted_profit = []
    for i in range(pow(2, n)):
        current_binary_sequence = []
        current_weight_sequence = []
        current_weight = 0
        current_profit = 0
        temp = i
        index = 0
        for j in range(n):
            bin = temp % 2
            current_binary_sequence.append(bin)
            if bin == 1:
                current_weight_sequence.append(weight[index])
                current_weight += weight[index]
                current_profit += values[index]
            index = index+1
            temp = temp//2

        if current_weight < capacity:
            for j in range(n):
                if current_binary_sequence[j] == 0 and current_weight < capacity:
                    remaining_capacity = capacity-current_weight
                    if remaining_capacity >= weight[j]:
                        current_binary_sequence[j] = 1
                        current_weight_sequence.append(weight[j])
                        current_weight += weight[j]
                        current_profit += values[j]
                    else:
                        ratio = remaining_capacity/weight[j]
                        current_binary_sequence[j] = 1*ratio
                        # current_weight_sequence.append(weight[j]*ratio)
                        current_weight += weight[j]*ratio
                        current_profit += values[j]*ratio

        binary_sequence.append(current_binary_sequence)
        weight_sequence.append(current_weight_sequence)
        total_weight_sequence.append(current_weight)
        total_profit_sequence.append(current_profit)
        # print(
        #     f"{i}==> {binary_sequence[i]}==>{weight_sequence[i]}==>{total_weight_sequence[i]}==>{total_profit_sequence[i]}")

        for i in range(len(total_weight_sequence)):
            if (total_weight_sequence[i] <= capacity):
                accepted_weight.append(total_weight_sequence[i])
                accepted_profit.append(total_profit_sequence[i])
    optimal_index = total_profit_sequence.index(max(accepted_profit))
    return {"max_value": total_profit_sequence[optimal_index],
            "weight_sequence": weight_sequence[optimal_index],
            "binary_sequence": binary_sequence[optimal_index],
            }


def knapsack_fractional_greedy(weights, values, capacity):
    n = len(weights)
    item = []
    for i in range(len(weights)):
        item.append([weights[i], values[i], values[i]/weights[i], i])
    item.sort(key=lambda x: x[2], reverse=True)
    total_weight = 0
    total_profit = 0
    binary_sequence = [0 for _ in range(n)]
    weight_sequence = []
    for weight, value, density, index in item:
        if (total_weight+weight) <= capacity:
            total_weight += weight
            total_profit += value
            binary_sequence[index] = 1
            weight_sequence.append(weight)
        else:
            ratio = (capacity-total_weight)/weight
            total_weight += weight*ratio
            total_profit += value*ratio
            binary_sequence[index] = 1*ratio

    return {"max_value": total_profit,
            "weight_sequence": weight_sequence,
            "binary_sequence": binary_sequence,
            }


def knapsack_01_dynamic(weights, values, capacity):
    n = len(weights)

    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if (weights[i-1] <= w):
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]]+values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    # for i in range(len(dp)):
    #     print(dp[i])

    maxs = dp[n][capacity]
    binary_seq = []
    weight_seq = []

    w = capacity
    for i in range(n, 0, -1):
        if (dp[i-1][w] != dp[i][w]):
            binary_seq.append(1)
            weight_seq.append(weights[i-1])
            w -= weights[i-1]
        else:
            binary_seq.append(0)

    binary_seq.reverse()
    weight_seq.reverse()

    return {
        "max_value": maxs,
        "weight_sequence": weight_seq,
        "binary_sequence": binary_seq
    }


weights = [2, 3, 6, 5]
values = [1, 2, 5, 8]
capacity = 8

print(knapsack_01_dynamic(weights, values, capacity))
# class TestKnapsackBruteForce(unittest.TestCase):

#     def test_one(self):
#         weights = [10, 20, 30]
#         values = [60, 100, 120]
#         capacity = 50
#         result = knapsack_01_brute_force(weights, values, capacity)
#         self.assertEqual(result["max_value"], 220)
#         self.assertEqual(result["weight_sequence"], [20, 30])
#         self.assertEqual(result["binary_sequence"], [0, 1, 1])

#     def test_two(self):
#         weights = [1, 2, 3]
#         values = [10, 15, 40]
#         capacity = 6
#         result = knapsack_01_brute_force(weights, values, capacity)
#         self.assertEqual(result["max_value"], 65)
#         self.assertEqual(result["weight_sequence"], [1, 2, 3])
#         self.assertEqual(result["binary_sequence"], [1, 1, 1])

#     def test_zero_capacity(self):
#         weights = [10, 20, 30]
#         values = [60, 100, 120]
#         capacity = 0
#         result = knapsack_01_brute_force(weights, values, capacity)
#         self.assertEqual(result["max_value"], 0)
#         self.assertEqual(result["weight_sequence"], [])
#         self.assertEqual(result["binary_sequence"], [0, 0, 0])

#     def test_empty_weights_and_values(self):
#         weights = []
#         values = []
#         capacity = 50
#         result = knapsack_01_brute_force(weights, values, capacity)
#         self.assertEqual(result["max_value"], 0)
#         self.assertEqual(result["weight_sequence"], [])
#         self.assertEqual(result["binary_sequence"], [])

#     def test_single_item_fits(self):
#         weights = [10]
#         values = [60]
#         capacity = 15
#         result = knapsack_01_brute_force(weights, values, capacity)
#         self.assertEqual(result["max_value"], 60)
#         self.assertEqual(result["weight_sequence"], [10])
#         self.assertEqual(result["binary_sequence"], [1])

#     def test_single_item_does_not_fit(self):
#         weights = [10]
#         values = [60]
#         capacity = 5
#         result = knapsack_01_brute_force(weights, values, capacity)
#         self.assertEqual(result["max_value"], 0)
#         self.assertEqual(result["weight_sequence"], [])
#         self.assertEqual(result["binary_sequence"], [0])

#     def test_items_with_same_value(self):
#         weights = [10, 20, 30]
#         values = [100, 100, 100]
#         capacity = 50
#         result = knapsack_01_brute_force(weights, values, capacity)
#         self.assertEqual(result["max_value"], 200)
#         self.assertEqual(result["weight_sequence"], [10, 20])
#         self.assertEqual(result["binary_sequence"], [1, 1, 0])


# class TestKnapsackFractionalBruteForce(unittest.TestCase):
#     def test_one(self):
#         weights = [10, 20, 30]
#         values = [60, 100, 120]
#         capacity = 50
#         result = knapsack_fractional_brute_force(weights, values, capacity)
#         self.assertEqual(result["max_value"], 240.0)
#         self.assertEqual(result["weight_sequence"], [10, 20])
#         self.assertEqual(result["binary_sequence"], [1, 1, 0.6666666666666666])

#     def test_two(self):
#         weights = [1, 2, 3]
#         values = [10, 15, 40]
#         capacity = 6
#         result = knapsack_fractional_brute_force(weights, values, capacity)
#         self.assertEqual(result["max_value"], 65.0)
#         self.assertEqual(result["weight_sequence"], [1, 2, 3])
#         self.assertEqual(result["binary_sequence"], [1, 1, 1])

#     def test_zero_capacity(self):
#         weights = [10, 20, 30]
#         values = [60, 100, 120]
#         capacity = 0
#         result = knapsack_fractional_brute_force(weights, values, capacity)
#         self.assertEqual(result["max_value"], 0.0)
#         self.assertEqual(result["weight_sequence"], [])
#         self.assertEqual(result["binary_sequence"], [0, 0, 0])

#     def test_empty_weights_and_values(self):
#         weights = []
#         values = []
#         capacity = 50
#         result = knapsack_fractional_brute_force(weights, values, capacity)
#         self.assertEqual(result["max_value"], 0.0)
#         self.assertEqual(result["weight_sequence"], [])
#         self.assertEqual(result["binary_sequence"], [])

#     def test_single_item_fits(self):
#         weights = [10]
#         values = [60]
#         capacity = 15
#         result = knapsack_fractional_brute_force(weights, values, capacity)
#         self.assertEqual(result["max_value"], 60.0)
#         self.assertEqual(result["weight_sequence"], [10])
#         self.assertEqual(result["binary_sequence"], [1])

#     def test_single_item_does_not_fit(self):
#         weights = [10]
#         values = [60]
#         capacity = 5
#         result = knapsack_fractional_brute_force(weights, values, capacity)
#         self.assertEqual(result["max_value"], 30.0)
#         self.assertEqual(result["weight_sequence"], [])
#         self.assertEqual(result["binary_sequence"], [0.5])

#     def test_items_with_same_value(self):
#         weights = [10, 20, 30]
#         values = [100, 100, 100]
#         capacity = 50
#         result = knapsack_fractional_brute_force(weights, values, capacity)
#         self.assertEqual(result["max_value"],  266.66666666666663)
#         self.assertEqual(result["weight_sequence"], [10, 20])
#         self.assertEqual(result["binary_sequence"], [1, 1, 0.6666666666666666])

# class TestKnapsackFractionalGreedy(unittest.TestCase):
#     def test_one(self):
#         weights = [10, 20, 30]
#         values = [60, 100, 120]
#         capacity = 50
#         result = knapsack_fractional_greedy(weights, values, capacity)
#         self.assertEqual(result["max_value"], 240.0)
#         self.assertEqual(result["weight_sequence"], [10, 20])
#         self.assertEqual(result["binary_sequence"], [1, 1, 0.6666666666666666])

#     def test_two(self):
#         weights = [1, 2, 3]
#         values = [10, 15, 40]
#         capacity = 6
#         result = knapsack_fractional_greedy(weights, values, capacity)
#         self.assertEqual(result["max_value"], 65.0)
#         self.assertEqual(result["weight_sequence"], [3, 1, 2])
#         self.assertEqual(result["binary_sequence"], [1, 1, 1])

#     def test_zero_capacity(self):
#         weights = [10, 20, 30]
#         values = [60, 100, 120]
#         capacity = 0
#         result = knapsack_fractional_greedy(weights, values, capacity)
#         self.assertEqual(result["max_value"], 0.0)
#         self.assertEqual(result["weight_sequence"], [])
#         self.assertEqual(result["binary_sequence"], [0, 0, 0])

#     def test_empty_weights_and_values(self):
#         weights = []
#         values = []
#         capacity = 50
#         result = knapsack_fractional_greedy(weights, values, capacity)
#         self.assertEqual(result["max_value"], 0.0)
#         self.assertEqual(result["weight_sequence"], [])
#         self.assertEqual(result["binary_sequence"], [])

#     def test_single_item_fits(self):
#         weights = [10]
#         values = [60]
#         capacity = 15
#         result = knapsack_fractional_greedy(weights, values, capacity)
#         self.assertEqual(result["max_value"], 60.0)
#         self.assertEqual(result["weight_sequence"], [10])
#         self.assertEqual(result["binary_sequence"], [1])

#     def test_single_item_does_not_fit(self):
#         weights = [10]
#         values = [60]
#         capacity = 5
#         result = knapsack_fractional_greedy(weights, values, capacity)
#         self.assertEqual(result["max_value"], 30.0)
#         self.assertEqual(result["weight_sequence"], [])
#         self.assertEqual(result["binary_sequence"], [0.5])

#     def test_items_with_same_value(self):
#         weights = [10, 20, 30]
#         values = [100, 100, 100]
#         capacity = 50
#         result = knapsack_fractional_greedy(weights, values, capacity)
#         self.assertEqual(result["max_value"],  266.66666666666663)
#         self.assertEqual(result["weight_sequence"], [10, 20])
#         self.assertEqual(result["binary_sequence"], [1, 1, 0.6666666666666666])

class TestKnapsackDynamic(unittest.TestCase):

    def test_one(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50
        result = knapsack_01_dynamic(weights, values, capacity)
        self.assertEqual(result["max_value"], 220)
        self.assertEqual(result["weight_sequence"], [20, 30])
        self.assertEqual(result["binary_sequence"], [0, 1, 1])

    def test_two(self):
        weights = [1, 2, 3]
        values = [10, 15, 40]
        capacity = 6
        result = knapsack_01_dynamic(weights, values, capacity)
        self.assertEqual(result["max_value"], 65)
        self.assertEqual(result["weight_sequence"], [1, 2, 3])
        self.assertEqual(result["binary_sequence"], [1, 1, 1])

    def test_zero_capacity(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 0
        result = knapsack_01_dynamic(weights, values, capacity)
        self.assertEqual(result["max_value"], 0)
        self.assertEqual(result["weight_sequence"], [])
        self.assertEqual(result["binary_sequence"], [0, 0, 0])

    def test_empty_weights_and_values(self):
        weights = []
        values = []
        capacity = 50
        result = knapsack_01_dynamic(weights, values, capacity)
        self.assertEqual(result["max_value"], 0)
        self.assertEqual(result["weight_sequence"], [])
        self.assertEqual(result["binary_sequence"], [])

    def test_single_item_fits(self):
        weights = [10]
        values = [60]
        capacity = 15
        result = knapsack_01_dynamic(weights, values, capacity)
        self.assertEqual(result["max_value"], 60)
        self.assertEqual(result["weight_sequence"], [10])
        self.assertEqual(result["binary_sequence"], [1])

    def test_single_item_does_not_fit(self):
        weights = [10]
        values = [60]
        capacity = 5
        result = knapsack_01_dynamic(weights, values, capacity)
        self.assertEqual(result["max_value"], 0)
        self.assertEqual(result["weight_sequence"], [])
        self.assertEqual(result["binary_sequence"], [0])

    def test_items_with_same_value(self):
        weights = [10, 20, 30]
        values = [100, 100, 100]
        capacity = 50
        result = knapsack_01_dynamic(weights, values, capacity)
        self.assertEqual(result["max_value"], 200)
        self.assertEqual(result["weight_sequence"], [10, 20])
        self.assertEqual(result["binary_sequence"], [1, 1, 0])


if __name__ == '__main__':
    unittest.main()
