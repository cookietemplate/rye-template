import random


def fermat_primality_test(n: int, k: int = 100) -> bool:
    if n == 2:  # noqa: PLR2004
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(1, n - 1)  # noqa: S311
        if pow(a, n - 1, n) != 1:
            return False

    return True
