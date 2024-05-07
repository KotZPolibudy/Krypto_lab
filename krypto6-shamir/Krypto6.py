import random


def polynom(x, parts):
    point = 0
    for partIdx, partVal in enumerate(parts[::-1]):
        point += x ** partIdx * partVal
    return point


def reconstructSecret(sample):
    sums = 0
    for i in range(len(sample)):
        product = 1
        for j in range(len(sample)):
            if i != j:
                product *= (sample[j][0] / (sample[j][0] - sample[i][0]))
        product *= sample[i][1]
        sums += product
    return round(sums)


max_val = 10000
minPartsToGetSecret = 3
numberOfSecretParts = 6
secret = 2708
print("Secret: ", secret)

# generowanie wielomianu
genParts = [random.randrange(0, max_val) for i in range(minPartsToGetSecret - 1)]
genParts.append(secret)

# rozdawanie części (tworzenie par (x, y)
secretShares = []
for i in range(1, numberOfSecretParts + 1):
    x = random.randrange(1, max_val)
    secretShares.append((x, polynom(x, genParts)))
parts = secretShares

print(f'Generated parts:\n{", ".join(str(part) for part in parts)}')
randomSampleToRecreateSecret = random.sample(parts, minPartsToGetSecret)
print(f'Random samples of parts:\n{", ".join(str(part) for part in randomSampleToRecreateSecret)}')
print("Reconstructed secret: ", reconstructSecret(randomSampleToRecreateSecret))
