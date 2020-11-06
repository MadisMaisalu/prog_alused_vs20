import random

koneminuti_hind = float(input("Sisestage kõneminuti hind: "))
konede_koguarv = int(input("Sisestage kõnede arv: "))


def kone_maksumus(konede_pikkused, koneminuti_hind):
    if konede_pikkused < 60:
        return koneminuti_hind
    elif konede_pikkused > 600:
        return 10*(1/60)*koneminuti_hind
    #else:
        #return konede_pikkused * (1 / 60) * koneminuti_hind

random.seed()

konede_pikkused = []
arve = 0

for x in range(konede_koguarv):
    konede_pikkused.append(random.randrange(1, 1000))
    print(konede_pikkused)

for y in range(len(konede_pikkused)):
    uhe_hind = kone_maksumus(konede_pikkused[x], koneminuti_hind)
    arve += uhe_hind
    print(str(uhe_hind))

print("Kogu arve: " + str(arve) + "EUR")
