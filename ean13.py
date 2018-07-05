# ean13 generator python script

import numpy as np


def ean_gen():
    ean_base = np.random.randint(low=0, high=10,  size=12, dtype=np.int32)
    # variables temp pour calculer les valeurs pondérées
    pond = []
    for i in range(len(ean_base)):
        if i % 2 == 0:
            pond.append(ean_base[i] * 1)
        else:
            pond.append(ean_base[i] * 3)

    remainder = np.sum(pond) % 10
    if remainder == 0:
        key = 0
    else:
        key = 10 - remainder

    return str(ean_base) + str(key)


print(ean_gen())
