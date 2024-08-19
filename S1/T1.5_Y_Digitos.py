
from math import log

### Formula de legendre para para multiplicidad de primos en factoriales
def legendre(n, p):
    count = 0
    while(n > 0):
        n //= p
        count += n
    return int(count)


### Suma de los logaritmos de cada miembro del factorial
def numDigits(n, b):
    sum = 0
    for i in range(1, n+1):
        sum += log(i) / log(b)
    return sum


### Factores primo más grande y sus apariciones
def bigFactor(n):
    factor = 1
    count = 0
    i = 2
    while i*i <= n: 
        while(n % i == 0):
            count = 1 if factor != i else count + 1 
            factor = i
            n /= i
        i += 1

    if(n > 1):
        factor = n
        count = 1
    
    return factor, count


### Entrada de datos

args = input()
inp = []

while(args):
    args = args.split()
    inp.append(args)
    args = input()

for i in inp:
    num = int(i[0])
    base = int(i[1])

    f, c = bigFactor(base)
    zeros = legendre(num, f)
    zeros //= c

    digits = int(numDigits(num, base)) + 1

    print(str(zeros) + " " + str(digits))

print("")

