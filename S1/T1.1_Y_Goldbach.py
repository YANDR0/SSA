

### Creación de la criba y obtención de primos

primes = []
max = 0

def fill_sieve(size):
    sieve = [0] * size
    for i in range(2, size, 1):
        if(sieve[i]):
            continue
        for j in range(i*2, size, i):
            sieve[j] = 1
        primes.append(i)
    return sieve


### Verificación de conjetura de goldbach

def goldbach(result):

    for p1 in range(max):
        sum = result - primes[p1]
        if(sieve[sum] == 0):
            return "{} = {} + {}".format(result, primes[p1], sum)

    return "Goldbach's conjecture is wrong."
            

### Obtener y devolver datos

numbers = []
result = int(input())

while(result != 0):
    max = max if max > result else result 
    numbers.append(result)
    result = int(input())

sieve = fill_sieve(max)

for i in numbers:
    print(goldbach(i))


