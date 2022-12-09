import random

game = True;

denemeHakkı = None

print("Sayı Tahmin Etme Oyunu'na Hoşgeldiniz.")

while denemeHakkı == None:
  zorluk = input("""
  Zorluk Seçiniz
  Kolay Mod: 1
  Normal Mod: 2
  Zor Mod: 3
  """)
    
#Kolay Mod Durumları
  if zorluk == "1":
    sayı = random.randint(1,50)
    denemeHakkı = 5
    
    print("Kolay Mod");
    print("1 ile 50 arasında bir sayı seçili.")
    print("5 deneme hakkın var.")
    print("Tahmininin seçili sayıdan büyük veya küçük olduğunu söyleyeceğiz.")
  while zorluk == "1":
    tahmin = input("""Tahminde bulunun.
     """)
    
    if int(sayı) == int(tahmin):
      print("Tebrikler. Cevabın doğru.")
      denemeHakkı = None
      zorluk = None
    elif int(sayı) != int(tahmin):
      denemeHakkı = denemeHakkı - 1
      print("Tahminin yanlış.")
      print("Kalan deneme hakkın:", denemeHakkı)
      if int(tahmin) > int(sayı):
        print("Tahminin seçili sayıdan büyük.")
      elif int(tahmin) < int(sayı):
        print("Tahminin seçili sayıdan küçük.")
      if denemeHakkı == 0:
        print("Kaybettin.")
        print("Cevap şuydu:", sayı)
        denemeHakkı = None
        zorluk = None

#Normal Mod Durumları
  if zorluk == "2":
    sayı = random.randint(1,100)
    denemeHakkı = 5
    
    print("Normal Mod");
    print("1 ile 100 arasında bir sayı seçili.")
    print("5 deneme hakkın var.")
    print("Tahmininin seçili sayıdan büyük veya küçük olduğunu söyleyeceğiz.")
  while zorluk == "2":
    tahmin = input("""Tahminde bulunun.
    """)

    if int(sayı) == int(tahmin):
      print("Tebrikler. Cevabın doğru.")
      denemeHakkı = None
      zorluk = None
    elif int(sayı) != int(tahmin):
      denemeHakkı = denemeHakkı - 1
      print("Tahminin yanlış.")
      print("Kalan deneme hakkın:", denemeHakkı)
      if int(tahmin) > int(sayı):
        print("Tahminin seçili sayıdan büyük.")
      elif int(tahmin) < int(sayı):
        print("Tahminin seçili sayıdan küçük.")
      if denemeHakkı == 0:
        print("Kaybettin.")
        print("Cevap şuydu:", sayı)
        denemeHakkı = None
        zorluk = None
    
#Zor Mod Durumları
  if zorluk == "3":
    sayı = random.randint(1,200)
    denemeHakkı = 5
    
    print("Zor Mod");
    print("1 ile 200 arasında bir sayı seçili.")
    print("5 deneme hakkın var.")
    print("Tahmininin seçili sayıdan büyük veya küçük olduğunu söyleyeceğiz.")
  while zorluk == "3":
    tahmin = input("""Tahminde bulunun.
    """)

    if int(sayı) == int(tahmin):
      print("Tebrikler. Cevabın doğru.")
      denemeHakkı = None
      zorluk = None
    elif int(sayı) != int(tahmin):
      denemeHakkı = denemeHakkı - 1
      print("Tahminin yanlış.")
      print("Kalan deneme hakkın:", denemeHakkı)
      if int(tahmin) > int(sayı):
        print("Tahminin seçili sayıdan büyük.")
      elif int(tahmin) < int(sayı):
        print("Tahminin seçili sayıdan küçük.")
      if denemeHakkı == 0:
        print("Kaybettin.")
        print("Cevap şuydu:", sayı)
        denemeHakkı = None
        zorluk = None