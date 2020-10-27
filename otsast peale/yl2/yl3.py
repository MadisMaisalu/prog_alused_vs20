vanus = int(input("Sisestage enda vanus: "))
while vanus >= 150:    # vanuse limiidiks on 150
    vanus = int(input("Viga! Proovige uuesti: "))   # veateade kui on üle 150
sugu = input("Sisestage enda sugu (Mees/Naine): ")
while (sugu !="Mees") or (sugu !="Naine"):  # veateade kui pole Mees või Naine !!!!SIIN ON MINGI VIGA!!!!! EI LASE VALIDA NAINE
    sugu = input("Viga! Proovige uuesti! Kasutage suurt esitähte (Mees/Naine): ")

treening = input("Valge treeningtüüp: Tervisetreening, Põhivastupidavus, Intensiivne ")
while treening != "Tervisetreening" or treening != "Põhivastupidavus" or treening != "Intensiivne":
    treening = input("Viga! Valige treeningtüüp(Tõstutundlik): Tervisetreening, Põhivastupidavus, Intensiivne ") # ainult tervisetreening töötab

# mehed

meeste_max_pulss = (220 - vanus)
naiste_max_pulss = (206 - vanus*0.88)

if treening == "Tervisetreening" and sugu == "Mees":
    print("Teie normaalne pulsisagedus on " +
          str(round(meeste_max_pulss*0.5)) +
          " kuni " + str(round(meeste_max_pulss*0.75)))

if treening == "Põhivastupidavus" and sugu == "Mees":
    print("Teie normaalne pulsisagedus on " +
          str(round(meeste_max_pulss*0.7)) +
          " kuni " + str(round(meeste_max_pulss*0.80)))

if treening == "Intensiivne" and sugu == "Mees":
    print("Teie normaalne pulsisagedus on " +
          str(round(meeste_max_pulss*0.8)) +
          " kuni " + str(round(meeste_max_pulss*0.87)))


# naised

if treening == "Tervisetreening" and sugu == "Naine":
    print("Teie normaalne pulsisagedus on " +
          str(round(naiste_max_pulss*0.5)) +
          " kuni " + str(round(naiste_max_pulss*0.75)))

if treening == "Põhivastupidavus" and sugu == "Naine":
    print("Teie normaalne pulsisagedus on " +
          str(round(naiste_max_pulss*0.7)) +
          " kuni " + str(round(naiste_max_pulss*0.80)))

if treening == "Intensiivne" and sugu == "Naine":
    print("Teie normaalne pulsisagedus on " +
          str(round(naiste_max_pulss*0.8)) +
          " kuni " + str(round(naiste_max_pulss*0.87)))
