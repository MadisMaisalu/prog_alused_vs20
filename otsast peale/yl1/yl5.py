ainepunktid = int(input("Sisestage ainepunktide arv: "))
nadalad = int(input("Sisestage nädalate arv: "))
tunde_nadalas = round(int(ainepunktid) / int(nadalad))
print("Teil on nädalas ümmarguselt " + str(tunde_nadalas) + " tundi.")