

### Formula de legendre para para multiplicidad de primos en factoriales
def legendre(n, p):
    count = 0
    while(n > 0):
        n //= p
        count += n
    return int(count)


### Cantidad de digitos, casi igual que legendre
### trabaja sobre el resultado, tons no sirve :v 
def digits(n, b):
    count = 0
    while(n > 0):
        n //= b
        count += 1
    return count


### Factores primo más grande y sus apariciones
def bigFactor(n):
    factor = 1
    count = 0
    i = 2
    while i*i <= n: 
        while(n % i == 0):
            factor = i
            count = 1 if factor != i else count + 1 
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

    print(zeros)