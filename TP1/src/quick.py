import sys
import time

ex_path = sys.argv[1]  # Path de l'exemplaire

data = []

fread = open(ex_path, "r")


def quickSort(data_to_sort):
    if not data_to_sort:
        return []
    else:
        pivot = data_to_sort[0]
        leftside = []
        rightside = []
        for i in data_to_sort[1:]:
            if i < pivot:
                leftside.append(i)
            else:
                rightside.append(i)
    return quickSort(leftside) + [pivot] + quickSort(rightside)


with fread:
    for line in fread:
        data.append(int(line.strip()))

# On commence a compter le temps uniquement pour le tri
start_time = time.time()

final_result = quickSort(data)

execution_time = time.time()-start_time

options = sys.argv[2:]
if '-p' in options:  # On imprime les nombres triés
    for i in range(len(final_result)):
        if i != len(final_result) - 1:
            print(final_result[i], end=' ')
        else:
            print(final_result[i])
if '-t' in options:  # On imprime le temps d'exécution
    print(execution_time)

