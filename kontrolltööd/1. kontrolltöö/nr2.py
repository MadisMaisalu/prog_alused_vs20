from random import randint # impordin suvalise numbri generaatori
koneminuti_hind = float(input("Sisestage kõneminuti hind: ")) # siit saab kõneminuti hinna
konede_arv = int(input("Sisestage kõnede koguarv: ")) # siit saab kui mitu kõne tehti

i= konede_arv # kõnede arv sekundites siit
while i > 0:
    kone_kestvus = randint(1, 1000)
    arve = koneminuti_hind * (1 / 60) * kone_kestvus
    i= i-1
    if kone_kestvus < 60:
        kone_maksumus = koneminuti_hind
    if kone_kestvus > 600:
        kone_maksumus = 10*koneminuti_hind
    print(arve)
