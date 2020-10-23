import random


täringute_arv = int(input("Täringute arv: "))

while täringute_arv > 0:
    print(random.randint(1, 6))
    täringute_arv -= 1