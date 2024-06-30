import unittest


def activity_selection_recursion(s, f, k, n, selected):
    if n == 0:
        return []
    selected.append((s[k], f[k]))
    m = k+1
    while m < n and s[m] < f[k]:
        m = m+1
    if m < n:
        activity_selection_recursion(s, f, m, n, selected)
    return selected


def activity_selection_iterative(s, f, n):
    if n == 0:
        return []
    selected = []
    selected.append((s[0], f[0]))
    for i in range(n):
        if s[i] > selected[-1][1]:
            selected.append((s[i], f[i]))
    return selected


s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
selected = []
activity_selection_recursion(s, f, 0, len(s), selected)
print(selected)
selected = []
activity_selection_iterative(s, f, len(s))
print(selected)


class TestActivitySelectionGreedyIterative(unittest.TestCase):

    def test_general(self):
        start_times = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
        finish_times = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
        expected = [(1, 4), (5, 7), (8, 11), (12, 16)]
        result = activity_selection_iterative(
            start_times, finish_times, len(start_times))
        self.assertListEqual(result, expected)

    def test_no_activities(self):
        start_times = []
        finish_times = []
        expected = []
        result = activity_selection_iterative(
            start_times, finish_times, len(start_times))
        self.assertListEqual(result, expected)

    def test_one_activity(self):
        start_times = [1]
        finish_times = [2]
        expected = [(1, 2)]
        result = activity_selection_iterative(
            start_times, finish_times, len(start_times))
        self.assertListEqual(result, expected)


class TestActivitySelectionGreedyRecursive(unittest.TestCase):

    def test_general(self):
        start_times = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
        finish_times = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
        expected = [(1, 4), (5, 7), (8, 11), (12, 16)]
        result = activity_selection_recursion(
            start_times, finish_times, 0, len(start_times), [])
        self.assertListEqual(result, expected)

    def test_no_activities(self):
        start_times = []
        finish_times = []
        expected = []
        result = activity_selection_recursion(
            start_times, finish_times, 0, len(start_times), [])
        self.assertListEqual(result, expected)

    def test_one_activity(self):
        start_times = [1]
        finish_times = [2]
        expected = [(1, 2)]
        result = activity_selection_recursion(
            start_times, finish_times, 0, len(start_times), [])
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
