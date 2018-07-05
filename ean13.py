# ean13 generator python script

import numpy as np


def ean_gen():
    ean_base = np.random.randint(low=0, high=10,  size=12, dtype=np.int32)
    ean = []
    key = 0
    # variables temp pour calculer les valeurs pondérées
    pond = []
    for i in range(len(ean_base)):
        if i % 2 == 0:
            pond.append(ean_base[i] * 1)
        else:
            pond.append(ean_base[i] * 3)

    remainder = np.sum(pond) % 10
    if remainder == 0:
        pass
    else:
        key = 10 - remainder

    for n in ean_base:
        ean.append(ean_base[n])

    ean.append(key)
    return ean


# fancy print
for n in ean_gen():
    print(n, end='')
