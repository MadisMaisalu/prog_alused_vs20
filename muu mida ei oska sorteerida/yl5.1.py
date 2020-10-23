fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
     vastuvõetud.append(int(rida))
fail.close()
print(vastuvõetud)
aasta = int(input("Sisesta aasta vahehemikust 2011 kuni 2019: "))
aastad = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
#kontrollime aasta olemasolu
if aasta in aastad:
    i = print(aastad.index(aasta))
    #prindi sama indeksiga väärtus nimekirjast
    print("Aastas " + str(aasta) + " võeti vastu " + str(vastuvõetud[i]))