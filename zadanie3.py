import random
import math
import hashlib
import time


def MD5(jawny):
    return hashlib.md5(jawny.encode('utf-8'))


def SH_1(jawny):
    return hashlib.sha1(jawny.encode('utf-8'))


def SH_2(jawny):
    # return hashlib.sha256(jawny.encode('utf-8'))
    # return hashlib.sha384(jawny.encode('utf-8'))
    # return hashlib.sha224(jawny.encode('utf-8'))
    return hashlib.sha512(jawny.encode('utf-8'))


def SH_3(jawny):
    # return hashlib.sha3_224(jawny.encode('utf-8'))
    # return hashlib.sha3_256(jawny.encode('utf-8'))
    # return hashlib.sha3_384(jawny.encode('utf-8'))
    return hashlib.sha3_512(jawny.encode('utf-8'))


def main_pierwszy():
    print("Słowo\tDługość Słowa\tAlgorytm\tCzas\tDługość Wyniku\tWynik(hash bajtami)")
    for slowo in DANE:
        T_start = time.perf_counter_ns()
        wynMD = MD5(slowo)
        T_MD = time.perf_counter_ns() - T_start

        T_start = time.perf_counter_ns()
        wynSH1 = SH_1(slowo)
        T_SH1 = time.perf_counter_ns() - T_start

        T_start = time.perf_counter_ns()
        wynSH2 = SH_2(slowo)
        T_SH2 = time.perf_counter_ns() - T_start

        T_start = time.perf_counter_ns()
        wynSH3 = SH_3(slowo)
        T_SH3 = time.perf_counter_ns() - T_start

        print(f"{slowo}\t{len(slowo)}\tMD5\t\t{T_MD}\t{len(wynMD.hexdigest())}\t{wynMD.hexdigest()}")
        print(f"{slowo}\t{len(slowo)}\tSH1\t\t{T_SH1}\t{len(wynSH1.hexdigest())}\t{wynSH1.hexdigest()}")
        print(f"{slowo}\t{len(slowo)}\tSH2\t\t{T_SH2}\t{len(wynSH2.hexdigest())}\t{wynSH2.hexdigest()}")
        print(f"{slowo}\t{len(slowo)}\tSH3\t\t{T_SH3}\t{len(wynSH3.hexdigest())}\t{wynSH3.hexdigest()}")


def check_kolizji(lista_hashy):
    pom = [[bin(ord(hhash[0])), bin(ord(hhash[1]))] for hhash in lista_hashy]
    print(pom)

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
    pass


def main():
    lista_hashyy = []
    for slowo in DANE:
        T_start = time.perf_counter_ns()
        wynMD = MD5(slowo)
        T_MD = time.perf_counter_ns() - T_start
        lista_hashyy.append(wynMD.hexdigest())
        print(f"{slowo}\t{len(slowo)}\tMD5\t\t{T_MD}\t{len(wynMD.hexdigest())}\t{wynMD.hexdigest()}")

    for slowo in DANE:
        T_start = time.perf_counter_ns()
        wynSH1 = SH_1(slowo)
        T_SH1 = time.perf_counter_ns() - T_start
        print(f"{slowo}\t{len(slowo)}\tSH1\t\t{T_SH1}\t{len(wynSH1.hexdigest())}\t{wynSH1.hexdigest()}")

    for slowo in DANE:
        T_start = time.perf_counter_ns()
        wynSH2 = SH_2(slowo)
        T_SH2 = time.perf_counter_ns() - T_start
        print(f"{slowo}\t{len(slowo)}\tSH2\t\t{T_SH2}\t{len(wynSH2.hexdigest())}\t{wynSH2.hexdigest()}")


    for slowo in DANE:
        T_start = time.perf_counter_ns()
        wynSH3 = SH_3(slowo)
        T_SH3 = time.perf_counter_ns() - T_start
        print(f"{slowo}\t{len(slowo)}\tSH3\t\t{T_SH3}\t{len(wynSH3.hexdigest())}\t{wynSH3.hexdigest()}")


    print(lista_hashyy)
    check_kolizji(lista_hashyy)




DANE = ["Kot", "Kou", "Kto", "Ala", "Aba", "Wysokogórska_Wyprawa", "Gdzie?", "Everest", "Smoki", "Gobliny", "Inne Baśniowe stwory", "Kontrowersyjne opinie", ""]
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





