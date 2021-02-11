
print("Numara Matik Oyununa Hoşgeldiniz")
#Rastgele sayı atar
from random import randint
tahminEdilecekSayi = randint(1,100)

sayac=0


while True:
	sayac+=1
	#Kullanıcıdan girdi alır
	tahmin =input("Tahmininizi giriniz(1 ile 100 arasında bir sayı):")
	try:
		tahmin=int(tahmin)
		pass
	except ValueError:
		print("Lütfen 1 ile 100 arasında BİR SAYI giriniz")
		continue

	if 0<=tahmin<=100:
	   if 70<=abs(tahminEdilecekSayi-tahmin)<=99:
	   	print("Sayıya Çok Uzaksınız")
	   	continue
	   elif 50<=abs(tahminEdilecekSayi-tahmin)<=69:
	   	print("Sayıya Uzaksınız")
	   	continue
	   elif 30<=abs(tahminEdilecekSayi-tahmin)<=49:
	   	print("Sayıya Yakınsınız")
	   	continue
	   elif 10<=abs(tahminEdilecekSayi-tahmin)<=29:
	   	print("Sayıya Çok Yakınsınız")
	   	continue
	   elif 1<=abs(tahminEdilecekSayi-tahmin)<=9:
	   	print("Neredeyse Oluyordu")
	   	continue
	   else:
	    print("Tebrikler Bildiniz :)")
	    print("Rastele seçilen sayı {0}".format(tahminEdilecekSayi))
	    print("Tahmin sayınız {0}".format(sayac))
	    devam=input("Devam Etmek İster Misiniz? (E/H)")
	    if devam.upper()=="H":
	    	break
	    else:
	    	tahminEdilecekSayi = randint(1,100)
	    	
	else:
		print("1 ile 100 arasında sayı giriniz")
		continue






		
			
            

