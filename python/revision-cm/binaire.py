def binaire(n: int) -> int:
    i = 0
    k = 1
    while k <= n:
        b_i = n % 2
        n = (n - b_i) / 2
        i = i + 1
        k = k * 2
    i_max = i - 1
    return i_max


# Example:
# n = 5
val = 5
print(binaire(val))  # Expected: 2
