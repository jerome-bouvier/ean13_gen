# ean13 generator

import numpy as np


def random_ean():
    # génération aléatoires des 12 premiers int
    ean_base = np.random.randint(low=0, high=10,  size=12, dtype=np.int32)
    for n in ean_base:
        print(n, end='')
    return ean_base


def define_key(ean):
    # variables temp pour calculer les valeurs pondérées
    pond = []
    for i in range(len(ean)):
        if i % 2 == 0:
            pond.append(base[i] * 1)
        else:
            pond.append(base[i] * 3)

    remainder = np.sum(pond) % 10
    if remainder == 0:
        key = 0
        print(key)
    else:
        key = 10 - remainder
        print(key)
    return key


choice = input("Generate ? or q to quit")
while choice != 'q':
    base = random_ean()
    cle = define_key(base)
    choice = input("Generate ? ")
