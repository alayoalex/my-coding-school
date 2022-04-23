items = [i for i in range(10)]
differences = [next_el - elt for elt, next_el in zip(items, items[1:])]
print(differences)