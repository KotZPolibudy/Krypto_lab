import hashlib
import time
import pandas as pd
import matplotlib as plt


def MD5(jawny):
    return hashlib.md5(jawny.encode('utf-8'))


def SH_1(jawny):
    return hashlib.sha1(jawny.encode('utf-8'))


def SH_2(jawny):
    return hashlib.sha256(jawny.encode('utf-8'))
    # return hashlib.sha384(jawny.encode('utf-8'))
    # return hashlib.sha224(jawny.encode('utf-8'))
    # return hashlib.sha512(jawny.encode('utf-8'))


def SH_3(jawny):
    # return hashlib.sha3_224(jawny.encode('utf-8'))
    return hashlib.sha3_256(jawny.encode('utf-8'))
    # return hashlib.sha3_384(jawny.encode('utf-8'))
    # return hashlib.sha3_512(jawny.encode('utf-8'))

"""
def check_kolizji(lista_hashy):
    pom = [[bin(ord(hhash[0])), bin(ord(hhash[1]))] for hhash in lista_hashy]
    print(pom)
    pom_str_lst = []

    for x in pom:
        pom_str_lst = []
        # print(x)
        # print(x[0][2:])
        pom_str = x[0][2:] + x[1][2:]
        # print(pom_str)
        pom_str = pom_str[:12]
        print(pom_str)
        pom_str_lst.append(pom_str)

    for a in pom_str_lst:
        print("AAAAA")
        print(a)


def check_SAC(hash1, hash2):
    bh1 = bin(hash1)
    bh2 = bin(hash2)
    c = 0
    n = len(bh1)
    if n != len(bh2):
        print("SAC - niezgodne długości hashy")
        return True
    for i in range(n):
        if bh1[n] == bh2[n]:
            c += 1
        # else:
        # continue
    return c / n
    # c/n to będzie proc zgodnych bitów, powinno być około 0,5
"""

def check_kolizji_na_bitach(Lista_skrotow, n):
    # print("Przed ordem", Lista_skrotow)
    Lista_skrotow = [''.join(format(ord(char), '08b') for char in string) for string in Lista_skrotow]
    # print("Po ord", Lista_skrotow)
    Lista_skrotow = [skrot[:n] for skrot in Lista_skrotow]
    # print("Po skroceniu", Lista_skrotow)
    d = {}
    for skrot in Lista_skrotow:
        if skrot in d:
            d[skrot] += 1
        else:
            d[skrot] = 1

    suma = 0
    for key in d.keys():
        if d[key] > 1:
            print("Kolizja na: ", key, "ilość kolizji = ", d[key])
            suma += d[key]
    print("SUMARYCZNIE KOLIZJI DLA n= ", n, "to ", suma, " na ", len(Lista_skrotow), " hashy")


def check_SAC():
    print("Kryterium SAC dla przykładów:")
    # slowo1 = "Kot"
    # slowo2 = "Kou"
    slowo1 = "figa"
    slowo2 = "giga"
    hash1 = MD5(slowo1)
    hash2 = MD5(slowo2)
    hash1 = hash1.hexdigest()
    hash2 = hash2.hexdigest()
    print(hash1)
    print(hash2)
    binhash1 = ''.join(format(ord(char), '08b') for char in hash1)
    binhash2 = ''.join(format(ord(char), '08b') for char in hash2)
    print(binhash1)
    print(binhash2)
    n = len(binhash1)
    wyn = ""
    for i in range(n):
        if (binhash1[i] == binhash2[i]):
            wyn += "0"
        else:
            wyn += "1"
    print(wyn)

    pomd = {}
    pomd["0"] = 0
    pomd["1"] = 1
    for i in range(len(wyn)):
        pomd[wyn[i]] += 1
    print("n = ", n)
    print(pomd)







def main():
    lista_hashyy = []
    # md5df = pd.DataFrame(columns=["Algorytm", "Słowo_Jawne", "Długość_słowa", "Czas wykonania", "Długość_Skrótu", "Skrót"])
    # sh1df = pd.DataFrame(columns=["Algorytm", "Słowo_Jawne", "Długość_słowa", "Czas wykonania", "Długość_Skrótu", "Skrót"])
    # sh2df = pd.DataFrame(columns=["Algorytm", "Słowo_Jawne", "Długość_słowa", "Czas wykonania", "Długość_Skrótu", "Skrót"])
    # sh3df = pd.DataFrame(columns=["Algorytm", "Słowo_Jawne", "Długość_słowa", "Czas wykonania", "Długość_Skrótu", "Skrót"])
    CZASY = []
    d = {}
    for slowo in DANE:
        T_start = time.perf_counter_ns()
        wynMD = MD5(slowo)
        T_MD = time.perf_counter_ns() - T_start
        lista_hashyy.append(wynMD.hexdigest())
        CZASY.append(T_MD)
    d = {"Slowo_Jawne": DANE, "Długość_słowa": [len(slowo) for slowo in DANE], "Czas wykonania": CZASY,
         "Długość_Skrótu": [len(h) for h in lista_hashyy], "Skrót": lista_hashyy}
    md5df = pd.DataFrame(d)
    print(md5df)
    # print(lista_hashyy)
    lista_do_kolizji = lista_hashyy
    # check_kolizji(lista_hashyy)

    lista_hashyy = []
    CZASY = []
    d = {}
    for slowo in DANE:
        T_start = time.perf_counter_ns()
        wynSH1 = SH_1(slowo)
        T_SH1 = time.perf_counter_ns() - T_start
        lista_hashyy.append(wynSH1.hexdigest())
        CZASY.append(T_SH1)
        # print(f"{slowo}\t{len(slowo)}\tSH1\t\t{T_SH1}\t{len(wynSH1.hexdigest())}\t{wynSH1.hexdigest()}")
    d = {"Slowo_Jawne": DANE, "Długość_słowa": [len(slowo) for slowo in DANE], "Czas wykonania": CZASY,
         "Długość_Skrótu": [len(h) for h in lista_hashyy], "Skrót": lista_hashyy}
    sh1df = pd.DataFrame(d)
    # print(sh1df)

    for slowo in DANE:
        T_start = time.perf_counter_ns()
        wynSH2 = SH_2(slowo)
        T_SH2 = time.perf_counter_ns() - T_start
        # print(f"{slowo}\t{len(slowo)}\tSH2\t\t{T_SH2}\t{len(wynSH2.hexdigest())}\t{wynSH2.hexdigest()}")

    for slowo in DANE:
        T_start = time.perf_counter_ns()
        wynSH3 = SH_3(slowo)
        T_SH3 = time.perf_counter_ns() - T_start
        # print(f"{slowo}\t{len(slowo)}\tSH3\t\t{T_SH3}\t{len(wynSH3.hexdigest())}\t{wynSH3.hexdigest()}")

    # print(lista_hashyy)
    # check_kolizji(lista_hashyy)
    # check_kolizji_na_bitach(lista_do_kolizji, 12)
    print(lista_do_kolizji)
    for i in range(12, 0, -1):
        print("Ilość bitów: ", i)
        check_kolizji_na_bitach(lista_do_kolizji, i)
    check_SAC()



DANE = ["Kot", "Kou", "Kto", "Ala", "Aba", "Wysokogórska_Wyprawa", "Gdzie?", "Everest", "Smoki", "Gobliny",
        "Inne Baśniowe stwory", "Kontrowersyjne opinie", "lol następny jest pusty", "", "A ten będzie mieć spację", " ",
        "Tak, koniec pomysłów."]
if __name__ == '__main__':
    main()

"""
3.
MD5 is reversible: https://ekursy.put.poznan.pl/pluginfile.php/2453830/mod_resource/content/1/CWICZENIE%208.pdf
773681c58e9b8e3883ef2ad880ffaa47 is reversed to "Kto"
byłoby znacznie bezpieczniejsze gdyby użyć "soli" (lub ciągu zaburzającego), który pomógłby w przypadku np powtórzonych
haseł w bazie danych ukrywając je poprzez używanie innego zaburzenia (innej soli) dla każdego hasła
sól rozbudowałaby znacznie "lookup" tabele do odwracania hashów.

4.
https://crypto.stackexchange.com/questions/1434/are-there-two-known-strings-which-have-the-same-md5-hash-value

zostały już znalezione kolizje dla MD5 -> pod zamieszczonym linkiem znajduje się przykład dla takiej kolizji.

MD5 nie spełnia trzech warunków potrzebnych by uznać je za bezpieczne i skuteczne, gdyż
1. istnieje możliwość kolizji
2. Preimage resistance -> istnieje możliwość odwrócenia skrótu do pierwotnej wartości
3. Second-Preimage resistance  -> przeprowadzono również skuteczny second-preimage attack znajdując różne dane 
pierwotnie wejściowe do funkcji MD5 z konkretnych danych wyjściowych
4.



"""
