import random
import math


def fermat_primal_test(n):
    for _ in range(5):
        a = random.randint(2, n-2)
        if pow(a, n-1) % n == 1:
            return True


def miller_rabin_test(n):
    if n == 2 and n == 3:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    check = n-1
    s = 0
    d = 0
    while check % 2 != 1:
        s += 1
        check = check/2
    d = (n-1)//(2**s)

    a = random.randint(2, n-2)
    x = pow(a, d, n)
    if x == 1 or x == n-1:
        return True
    for i in range(s):
        x = pow(x, 2, n)
        if x == n-1:
            break
        else:
            return False
    return True


def miller_rabin_test(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n == 4:
        return False

    # Write n-1 as 2^s * d
    check = n-1
    s, d = 0, 0
    while check % 2 != 1:
        s += 1
        check = check/2
    d = (n-1)//(2**s)
    if s == 0:
        return False
    # Witness loop
    a = random.randint(2, n - 2)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True

    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            break
        else:
            return False
    if x != n - 1:
        return False
    return True


if __name__ == "__main__":
    if (miller_rabin_test(561)):
        print("The number is prime.")
    else:
        print("Composite number")

to_be_tested = 13
print(fermat_primal_test(to_be_tested))
print(miller_rabin_test(to_be_tested))
if __name__ == "__main__":
    if (fermat_primal_test(561)):
        print("The number is prime.")
    else:
        print("Composite number")
    if (miller_rabin_test(561)):
        print("The number is prime.")
    else:
        print("Composite number")
