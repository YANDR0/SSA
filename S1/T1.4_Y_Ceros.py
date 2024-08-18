

### Legendre específico para 5

def trailingZeroes(n):
    count = 0
    while(n > 0):
        n //= 5
        count += n
    return count

a = trailingZeroes(10)
print(a)