import itertools
import string
#A generator is pre-build thing to create data
def nums():
    yield 1
    yield 2
    yield 3

#for x in nums():
    #print(x)
def letters():
    for c in string.ascii_lowercase:
        yield c
#for x in letters():
    #print(x)


def prime_numbers():
    yield 2
    prime_cache=[2]
    for n in itertools.count(3,2):
        is_prime=True
        
        for p in prime_cache:
            if n % p ==0:
                is_prime=False
                break
        if is_prime:
            prime_cache.append(n)
            yield n
#for x in prime_numbers():
#    print(x)
#    if x>100:
#        break
squares=(x**2 for x in itertools.count(1))




for x in squares:
    print(x)
    if x>500:
        squares.close()

print(type(squares))