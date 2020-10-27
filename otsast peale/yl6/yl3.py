def kuu_nimi(kuu_number):
    kuud = [
        "jaanuar",
        "veebruar",
        "märts",
        "aprill",
        "mai",
        "juuni",
        "juuli",
        "august",
        "september",
        "oktoober",
        "november",
        "detsember",
    ]
    return kuud[kuu_number-1]

#kuupaeva formaat on PP.KK.AAAA

def kuupaev_sonena(kuupaev):
    kuupaev_eraldi_elementidega = kuupaev.split(".")
    paev = kuupaev_eraldi_elementidega[0]
    kuu = kuu_nimi(int(kuupaev_eraldi_elementidega[1]))
    aasta = kuupaev_eraldi_elementidega[2]
    kuupaev_sone_kujul = kuupaev_eraldi_elementidega[0] + ". " + kuu_nimi(int(
    kuupaev_eraldi_elementidega[2])) + " " + kuupaev_eraldi_elementidega[2] + ". a"
    return kuupaev_sone_kujul

kuupaev = input("Sisesta kuupäev kujul PP.KK.AAAA: ")
kuupaev_sonena(kuupaev)