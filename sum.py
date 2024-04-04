def sum(A):
    """
    This function calculates the sum of all elements in a given list.

    Parameters:
    A (list): The input list whose elements will be summed.

    Returns:
    int: The sum of all elements in the list.
    """
    sum = 0
    for i in A:
        sum += i
    return sum
