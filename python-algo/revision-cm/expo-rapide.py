# algorithme pour calculer l'exponentiation rapide d'un nombre a^n

def expo_rapide(a: int, n: int) -> int:
    res = 1
    while n > 0:
        if n % 2 == 1:
            res *= a
        a *= a
        n //= 2
    return res

def expo_rapide_2(a: int, n: int) -> int:
    exp = a
    res = 1
    for i in range(n):
        res *= exp
    return res


# Test
print(expo_rapide(2, 10))
print(eval('2**10'))
