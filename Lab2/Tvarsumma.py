def tvarsumma(n):
    if n > 0:
        return n % 10 + tvarsumma((n - n % 10) / 10)
    if n == 0:
        return 0


def tvarsumma2(n):
    result = 0
    while n > 0:
        result = result + n % 10
        n = (n - n % 10) / 10
    return result


print(tvarsumma(513574))
print(tvarsumma2(513574))
