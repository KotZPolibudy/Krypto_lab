import random
import math
import socket

# Pierwiastek pierwotny modulo n to taka liczba, że jej potęgi dają wszystkie możliwe reszty modulo n,
# które są względnie pierwsze z n.


def is_prime(pp):
    if pp == 2 or pp == 3:
        return True
    if pp < 2 or pp % 2 == 0:
        return False
    if pp < 9:
        return True
    if pp % 3 == 0:
        return False
    r = int(math.sqrt(pp))
    f = 5
    while f <= r:
        # print('\t', f)  # Wykomentować sprawdzanie czy pierwsza!
        if pp % f == 0:
            return False
        if pp % (f + 2) == 0:
            return False
        f += 6
    return True


def sieve_of_eratosthenes(num):
    prime = [True for _ in range(num + 1)]
    # boolean array
    pp = 2
    while pp * pp <= num:
        # If prime[p] is not
        # changed, then it is a prime
        if prime[pp]:

            # Updating all multiples of p
            for i in range(pp * pp, num + 1, pp):
                prime[i] = False
        pp += 1

    # Print all prime numbers
    wyn = []
    for pp in range(2, num + 1):
        if prime[pp]:
            # print(p)
            wyn.append(pp)
    # print(wyn)
    return wyn


def primitive_check(g, p):
    L=[]
    for i in range(1, p):
        L.append(pow(g, i, p))
    for i in range(1, p):
        if L.count(i) > 1:
            L.clear()
            return False
        return True


if __name__ == '__main__':
    size = 4
    Tajna_pierwszego = random.randint(10**(size-1), 10**size)
    Tajna_drugiego = random.randint(10 ** (size - 1), 10 ** size)
    primes = [prime for prime in sieve_of_eratosthenes(10 ** size) if prime > 10 ** (size - 1)]

    n = random.choice(primes)
    print("n = ", n)
    g = 2

    for i in range(100):  # 100 prób na wylosowanie, jak nie to szukaj sekwencyjnie
        g = random.randint(1, n-1)
        if primitive_check(g, n):
            break

    if not(primitive_check(g, n)):
        for g in range(n):
            if primitive_check(g, n):
                break

    print("g = ", g)

    Publiczna_pierwszego = pow(g, Tajna_pierwszego, n)
    Publiczna_drugiego = pow(g, Tajna_drugiego, n)

    # przesyłają je sobie (unikam sieci, znowu)
    # send_message(Publiczna)


    # Pierwszy oblicza:
    klucz_pierwszy = pow(Publiczna_drugiego, Tajna_pierwszego, n)
    klucz_drugi = pow(Publiczna_pierwszego, Tajna_drugiego, n)

    print(f"Klucz sesji u pierwszego to: {klucz_pierwszy}")
    print(f"Klucz sesji u drugiego to: {klucz_drugi}")


# komentarze do sprawozdania:
"""
1. screen - wyżej jest kod :)
2.  ograniczenia dla użytych parametrów  (co dla równych? albo bliskich? albo małych?)
3. Komunikacja jest narażona na atak man in the middle, gdzie człowiek w środku ustanowi osobne sesje zarówno z jedną
jak i z drugą stroną. 
4. Dodatkowe wnioski.

"""
