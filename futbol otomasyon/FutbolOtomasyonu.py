adet = int(input("Kac futbolcu eklenecek: "))

altsatir = "\n"

isimler = []
yaslar = []
goller = []
asistler = []

def ekleme():
    for i in range(0, adet, 1):
        isim = input(f"{i+1}.Futbolcu isim:")
        isim = isim.upper()
        yas = int(input(f"{i+1}.Futbolcu Yas:"))
        gol = int(input(f"{i+1}.Futbolcu gol sayisi:"))
        asist = int(input(f"{i+1}.Futbolcu asist sayisi:"))
        isimler.append(isim)
        goller.append(gol)
        yaslar.append(yas)
        asistler.append(asist)

def guncelleme():
    print("1.isim 2.yas 3.gol 4.asist")
    hangisi = int(input("Guncellencek Kategori:"))
    if hangisi == 1:
        kacinci = int(input("Guncelenecek indis no:"))
        isim = input("Yeni futbolcu isim:")
        isim = isim.upper()
        isimler[kacinci] = isim
    elif hangisi == 2:     
        kacinci = int(input("Guncelenecek indis no:"))
        yas = int(input("Yeni futbolcu yas:"))
        yaslar[kacinci] = yas
    elif hangisi == 3:
        kacinci = int(input("Guncelenecek indis no:"))
        gol = int(input("Yeni futbolcu gol sayisi:"))
        goller[kacinci] = gol
    else:
        kacinci = int(input("Guncelenecek indis no:"))
        asist = int(input("Yeni futbolcu asist sayisi:"))
        asistler[kacinci] = asist
        

def silme():
    print("1.isim 2.yas 3.gol 4.asist")
    hangisi = int(input("Silinecek Kategori:"))
    if hangisi == 1:
        kacinci = int(input("Silinecek indis no:"))
        isimler[kacinci] = "NONE"
    elif hangisi == 2:     
        kacinci = int(input("Silinecek indis no:"))
        yaslar[kacinci] = 0
    elif hangisi == 3:
        kacinci = int(input("Silinecek indis no:"))
        goller[kacinci] = 0
    else:
        kacinci = int(input("Silinecek indis no:"))
        asistler[kacinci] = 0

def listeleme():
    for i in range(adet):
        print(f"{isimler[i]} {yaslar[i]} Yas {goller[i]} Gol {asistler[i]} Asist")

def istatistik():
    toplamgol = 0
    toplamasist = 0
    toplamyas = 0
    for i in range(adet):
        toplamgol += goller[i]
        toplamasist += asistler[i]
        toplamyas += yaslar[i]
    ortgol = toplamgol / adet
    ortasist = toplamasist / adet
    ortyas = toplamyas /adet
    print(f"Gol Ortalamasi:{ortgol} Asist Ortalamasi:{ortasist} Yas Ortalamasi:{ortyas}")

while True:
    print(altsatir, end="")
    print("0.cikis 1.ekleme 2.guncelleme 3.silme 4.listeleme 5.istatistik")
    print(altsatir, end="")
    tus = input("tus:")
    if tus == "1":
        ekleme()
    elif tus == "2":
        guncelleme()
    elif tus == "3":
        silme()
    elif tus == "4":
        listeleme()
    elif tus == "5":
        istatistik()
    else:
        print("cikis yaptiniz...")
        break
