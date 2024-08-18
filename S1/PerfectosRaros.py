

### Creación de la criba

def fillSieve(size):
    sieve = [0] * size
    for i in range(2, size, 1):
        if(sieve[i]):
            continue
        for j in range(i*2, size, i):
            sieve[j] = 1
    return sieve


### Verificación de las reglas del número

def isPerfect(p):
    p = int(p)
    if(p < 2): return 'No'
    p2 = 2**p-1
    return 'No' if sieve[p] or sieve[p2] else 'Yes'


### Entrada de datos

n = int(input())
numbers = input().split(",")
sieve = fillSieve(2**19)

for i in range(n):
    r = isPerfect(numbers[i])
    print(r)


