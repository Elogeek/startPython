import statistics
from random import shuffle

notes = [
    5, 12, 8,
    10, 2, 20,
    2, 6, 9,
]
shuffle(notes)
print(notes)
# module statistics
result = statistics.mean(notes)
print("La moyenne de l'élève est de {}".format(result))

#