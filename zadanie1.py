# dwie 4-cyfrowe liczby pierwsze p,q przystające do 3mod4
# 4-cyfrowa liczba x0 -> seed, bez NWD z n   -> NWD(x0, n) = 1
# funkcja potęgowania modulo  pow(a, b, c) a^b % c
# czytać od najmniej znaczącego bitu liczby xi, czyli x0 ^2 %n
# a potem badania czy jest to dobry ciąg pseudolosowy
# test bitów -> liczba jedynek około połowy
# test serii -> ile jest jakich serii (01110 jest serią trzech jedynek) //zakresy w prezentacji
# test długiej serii -> w 20 000 bitów nie powinno być żadnej o długości 26 lub więcej
# test pokerowy -> w prezentacji
import math
import random


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(math.sqrt(n))
    f = 5
    while f <= r:
        # print('\t', f)  # Wykomentować sprawdzanie czy pierwsza!
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def SieveOfEratosthenes(num):
    prime = [True for i in range(num + 1)]
    # boolean array
    p = 2
    while (p * p <= num):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Updating all multiples of p
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    wyn = []
    for p in range(2, num + 1):
        if prime[p]:
            # print(p)
            wyn.append(p)
    # print(wyn)
    return wyn


def main(p, q, seed_size, gen_length):
    if not(is_prime(p)):
        print("p nie jest liczbą pierwszą")
    elif not(is_prime(q)):
        print("q nie jest liczbą pierwszą")
    elif p % 4 != 3:
        print("p nie przystaje do 3 mod 4")
    elif q % 4 != 3:
        print("q nie przystaje do 3 mod 4")
    else:
        n = p * q
        g = 0
        x0 = 1234  # usuwa warning o potencjalnym sprawdzeniu x0 przed nadaniem wartości
        while g != 1:
            x0 = random.randint(10**(seed_size-1), 10**(seed_size)-1)
            g = math.gcd(n, x0)
        g = math.gcd(n, x0)

        print("p = ", p)
        print("q = ", q)
        print("n = ", n)
        print("x0 = ", x0)

        if g != 1:
            print("Wartości nie spełniają warunku GCD(x, n) == 1")

        x = pow(x0, 2, n)
        wynik = '1' if x % 2 == 1 else '0'
        # print(wynik)
        for i in range(gen_length-1):
            x = pow(x, 2, n)
            wynik += str(x % 2)
            # print(wynik)
        return wynik
    return "ERROR"


def test_bit(number):
    d = {'1': 0, '0': 0}
    for i in range(len(number)):
        d[str(number[i])] += 1
    print("TEST BITÓW")
    print("Jedynek: ", d['1'], "\nZer: ", d['0'])
    wyn = True
    if d['1'] < 9725 or d['1'] > 10275:
        wyn = False
    if d['0'] < 9725 or d['0'] > 10275:
        wyn = False
    return wyn


def test_series(number):
    dj = {}  # jedynek
    dz = {}  # zer
    s = number[0]  # jaka seria
    l = 1  # jej długość
    for i in range(1, len(number)):
        if number[i] == s:
            l += 1
        else:
            # zapis do dict'a
            if s == '1':
                if l in dj:
                    dj[l] += 1
                else:
                    dj[l] = 1
            else:
                if l in dz:
                    dz[l] += 1
                else:
                    dz[l] = 1
            s = number[i]
            l = 1

    klucze_j = dj.keys()
    klucze_z = dz.keys()
    print("TEST SERII")
    print("Ilości jedynek o wartościach:")
    print("1: ", dj[1])
    print("2: ", dj[2])
    print("3: ", dj[3])
    print("4: ", dj[4])
    print("5: ", dj[5])
    suma_j = sum(dj.values()) - dj[1] - dj[2] - dj[3] - dj[4] - dj[5]
    print("6 i więcej: ", suma_j)

    print("Ilości zer o wartościach:")
    print("1: ", dz[1])
    print("2: ", dz[2])
    print("3: ", dz[3])
    print("4: ", dz[4])
    print("5: ", dz[5])
    suma_z = sum(dz.values()) - dz[1] - dz[2] - dz[3] - dz[4] - dz[5]
    print("6 i więcej: ", suma_z)

    Czy_zdane = True
    if dj[1] < 2315 or dj[1] > 2685: Czy_zdane = False
    if dz[1] < 2315 or dz[1] > 2685: Czy_zdane = False
    if dj[2] < 1114 or dj[2] > 1386: Czy_zdane = False
    if dz[2] < 1114 or dz[2] > 1386: Czy_zdane = False
    if dj[3] < 527 or dj[3] > 723: Czy_zdane = False
    if dz[3] < 527 or dz[3] > 723: Czy_zdane = False
    if dj[4] < 240 or dj[4] > 384: Czy_zdane = False
    if dz[4] < 240 or dz[4] > 384: Czy_zdane = False
    if dj[5] < 103 or dj[5] > 209: Czy_zdane = False
    if dz[5] < 103 or dz[5] > 209: Czy_zdane = False
    if suma_j < 103 or suma_j > 209: Czy_zdane = False
    if suma_z < 103 or suma_z > 209: Czy_zdane = False

    if Czy_zdane:
        print("Test serii zakończony pomyślnie.")
    else:
        print("Test serii zakończony niepowodzeniem.")

    klucz_j = sorted(klucze_j)[-1]
    klucz_z = sorted(klucze_z)[-1]

    print("Najdłuższy podciąg jedynek: ", klucz_j)
    print("Najdłuższy podciąg zer:     ", klucz_z)

    Czy_zdane_long = True
    if klucz_j >= 26:
        Czy_zdane_long = False
    if klucz_z >= 26:
        Czy_zdane_long = False

    if Czy_zdane_long:
        print("Test długiej serii zakończony pomyślnie.")
    else:
        print("Test długiej serii zakończony niepowodzeniem.")

    return (Czy_zdane, Czy_zdane_long)


def test_poker(number):
    n = len(number)
    lim = n // 4
    if n % 4 != 0:
        print("Długość ciągu niepodzielna przez 4, możliwe błędy!")
    d = {}
    # ls = []
    i = 0
    while i < n:
        s = number[i:i+4]
        # ls.append(s)
        i += 4
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    # print(ls[:5])
    # print(ls[-2], ls[-1])
    # print(number)
    # print(number[-10:])

    sm = 0
    pom = 0
    print("Jaki ciąg -> wartość")
    for key in sorted(d.keys()):
        print(key, "  ", d[key])
        sm = d[key] * d[key]
        pom += sm
    print("TESTY")
    print(pom)
    pom = pom * 16 / lim
    pom -= lim
    print(pom)

        # statystyka:
    print(pom)
    if pom > 2.16 and pom < 47.17:
        print("Test pokerowy zakończony powodzeniem")
        return True
    else:
        print("Test pokerowy zakończony porażką")
        return False


if __name__ == '__main__':
    # do zmiany - testowe wartości
    p = 5167
    q = 4567
    s = 4  # seed_size (ile cyfr)
    ILE = 20000

    # generować listę pierwszych z zakresu, przystajacych do 3 mod 4
    primes = SieveOfEratosthenes(10**s)
    # print(primes)
    primes = [prime for prime in primes if prime > 10**(s-1)]
    primes = [prime for prime in primes if prime % 4 == 3]
    # print(primes)

    p = random.choice(primes)
    q = random.choice(primes)

    generated = main(p, q, s, ILE)
    print(generated)
    print(len(generated))
    if generated != "ERROR":
        bity = test_bit(generated)
        serie, long_serie = test_series(generated)
        poker = test_poker(generated)

        print("\n \n WYNIKI: \n")
        if bity:
            print("Test bitów zakończony pomyślnie.")
        else:
            print("Test bitów zakończony niepowodzeniem.")

        if serie:
            print("Test serii zakończony pomyślnie.")
        else:
            print("Test serii zakończony niepowodzeniem.")

        if long_serie:
            print("Test długiej serii zakończony pomyślnie.")
        else:
            print("Test długiej serii zakończony niepowodzeniem.")

        if poker:
            print("Test pokerowy zakończony powodzeniem")
        else:
            print("Test pokerowy zakończony porażką")

    print("\n koooooniec")
# wnioski:
# nie wszystkie wylosowane liczby pierwsze, nawet te spełniające warunek przystawania do 3 mod 4 wystarczają aby ten generator przeszedł testy.
# Czasami przechodzi tylko część z testów, czasami żadnego, a niekiedy wszystkie.
# Zauważyłem zależność, że dla dalekich od siebie liczb pierwszych większa szansa że przejdzie wszystkie testy, ale nie musi to być zasadą.
