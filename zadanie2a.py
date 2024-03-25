import random
import math


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


def szyfruj(jawny, e, n):
    # szyfrować każdy znak osobno? Bo cała wiadomość to mi zje procesor...
    return [pow(ord(znak), e, n) for znak in jawny]
    # ale nie jest to bezpieczne ze względu na analizę ilościową znaków i tym podobne


def odszyfruj(szyfrogram, d, n):
    wyn = ""
    return wyn.join([chr(pow(znak, d, n)) for znak in szyfrogram])
    # for znak in szyfrogram:
    #     znak = pow(znak, d, n)
    #     wyn += chr(znak)
    # return wyn



if __name__ == '__main__':
    # tutaj zmienne do ustawienia
    size = 4  # długość tych liczb pierwszych, na podstawie jakich generujemy
    primes_full = sieve_of_eratosthenes(10 ** size)
    primes = [prime for prime in primes_full if prime > 10 ** (size - 1)]

    p = random.choice(primes)
    q = random.choice(primes)
    n = p * q
    phi = (p - 1) * (q - 1)

    print("p = ", p)
    print("q = ", q)
    print("n = ", n)
    print("phi = ", phi)

    jawna = "To jest MOJA! wiadomość jawna, która ma 50 znaków."
    # jawna = "short"
    # jawna = "ab"
    print(jawna, "\nDługość wiadomości= ", len(jawna))

    g = 0
    e = 0
    while g != 1:
        e = random.choice(primes)   # nie musi być pierwsza, ale szkoda nie użyć, tutaj mógłbym je losować
        g = math.gcd(e, phi)
    print("e = ", e)

    """
    d = 0
    while g != 0:
        d = random.randint(2, 10 ** size)
        pom = e * d - 1
        g = pom % phi
        print("Nieudane: ", pom, "  ", g)
    print("d = ", d)
    """
    """
    d = 0
    for d in range(phi-1):
        if (e * d - 1) % phi == 0:
            break
    if (e * d - 1) % phi != 0:
        print("NIE ZNALEZIONO d")
    else:
        print("d = ", d)
    """
    d = pow(e, -1, phi)
    print("d = ", d)

    print("\n", jawna)
    zaszyfrowana = szyfruj(jawna, e, n)
    print(zaszyfrowana)
    odszyfrowana = odszyfruj(zaszyfrowana, d, n)
    print(odszyfrowana)

    if jawna == odszyfrowana:
        print("Działa!")
    else:
        print("No niestety, nie tym razem")

    # No, na moje działa, ale teraz pytanie i wnioski:
    # zaszyfrowanie jest  łatwe i przyjemne, biega szybko, ale ODSZYFROWANIE, oh boy...
    # najpewniej to przez potęgowanie 7-mio cyfrowych liczb do 4-cyfrowej potęgi... ale co ja tam wiem...
    # w samej implementacji nie ma trudnych rzeczy, założenie jest dość proste.
    # Jedynie obliczeniowo odszyfrowywanie zajmuje "chwilkę"
    # O bezpieczeństwie stanowi trudność w faktoryzacji (czyli rozkładowi na czynniki) dużych liczb.

    """# Pytania do sprawka:
    1. Jak duże liczby mogą być użyte w programie:
    W mojej implementacji ogranicza mnie język programowania i sprzęt na jakim będzie wykonywana
    ta konkretna implementacja, ale dla większego bezpieczeństwa oczywiście jak największe!
    2. Opis metod użytych do wyznaczania e i d.
    e jest pseudolosowo losowane spośród liczb pierwszych wygenerowanych Sitem Eratostenesa
    d jest ustalane jako pierwsza znaleziona (szukając od 0) liczba spełniająca warunek względnej pierwszości
    3. Opis realizacji zadań (programu i jego składowych) i wartości uzyskane podczas ich realizacji.
    Wartości są printowane na bieżąco, wystarczy z konsoli sczytać (albo zczytać, heh)
    opis realizacji zadań #todo
    4. Odpowiedzi na pytania
    Odp na pytania są powyżej, ostatnie komentarze kodu
    5.Wnioski    
    
    Tak, są wnioski
    Jakie?
    ...ehhh nooooooo
    tak. #todo
    """
