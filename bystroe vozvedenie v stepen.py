def pow(a, n):
    if n % 2 == 0:
        return (a ** 2) ** (n / 2)
    if n % 2 != 0:
        return a * pow(a, n-1)
    return a

a = float(input())
n = int(input())
print(pow(a, n))
