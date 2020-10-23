isik = 0

#Kõik on väga katki ja ei oska,
# proovisin vähemalt 10 erinevat lahendust, lõpuks andsin alla

perekonnanimi = input("Sisestage perekonnanimi: ")
if (perekonnanimi[-2:] == "ne") and (isik == 0):
    print("Isik on abielus.")
    isik = 2
else:
    isik = 0

if (perekonnanimi[-2:] == "te") and (isik == 0):
    print("Isik on vallaline.")
    isik = 1
else:
    isik = 0

if (perekonnanimi[-1:] != "e") and (isik == 0):
    print("Isik ei ole leedulane.")
    isik = 3
else:
    isik = 0

if isik == 0:
    print("Isiku perekonnaseis on teadmata.")

