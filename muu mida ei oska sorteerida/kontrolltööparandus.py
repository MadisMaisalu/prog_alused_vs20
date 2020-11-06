import random
koneminuti_hind = float(input("Sisestage kõneminuti hind: "))
konede_arv = int(input("Sisestage kõnede arv: "))

def kone_hind(kone_pikkus, koneminuti_hind):
    if kone_pikkus < 60:
        kone_hind=koneminuti_hind
    if kone_pikkus > 600:
        kone_hind=10*koneminuti_hind

random.seed()
kone_kestvus = []
for x in range(konede_arv):
    kone_kestvus.append(random.randrange(1, 1000))

kogu_arve = 0
for y in range(len(kone_kestvus)):
    uhe_kone_hind = kone_hind(kone_kestuvs[y], hind)
    kogu_arve += uhe_kone_hind
    print("Arve on: " + str(kogu_arve))

