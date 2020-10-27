from random import *
istekoht = input("Kas soovite istekoha ise valida või loosida? (Ise/Loos) ")
if (istekoht == "ise" or istekoht == "Ise"):
    istekoha_tapsustus = input("Kas soovite istuda akna juures? (aken/muu) ")
    if istekoha_tapsustus == "aken" or istekoha_tapsustus == "Aken":
        print("Olete registreeritud akna kõrvalisele istmele!")
    else:
        print("Olete saanud koha mujale.")

if istekoht == "loos" or istekoht == "Loos":
    koht = (randint(1, 3))
    if koht == 1:
        print("Saite isekoha akna äärde.")
    if koht == 2 or koht == 3:
        print("Saite isekoha mujale.")
