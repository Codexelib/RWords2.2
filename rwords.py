""" RWords Terminal Beta 2.0 - created by c0d3rm4n """
RWords_surum = 'terminal beta 2.0'

# IMPORT RWS

import sys
sys.path.insert(0, 'rws/')
import rw1
import rw2
import rw3
import rw4
import rw5
sys.path.insert(0, '')

# GENERAL MODULES

import rwork
import rwebdata
import os
import random
import webbrowser
import time

# SETTINGS

ayar_tekrar_sor = 'ON'
ayar_akilli_klavye = 'ON'
ayar_ana_klayve = 'EU'

# PREPARE THE TERMINAL 

os.system('clear')

print('''
██████╗ ██╗    ██╗ ██████╗ ██████╗ ██████╗ ███████╗
██╔══██╗██║    ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝██║ █╗ ██║██║   ██║██████╔╝██║  ██║███████╗
██╔══██╗██║███╗██║██║   ██║██╔══██╗██║  ██║╚════██║
██║  ██║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████║
╚═╝  ╚═╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝
				created by c0d3rm4n
''')

# MENUS

mainMenu = """
FOR LEARN
[1] Kelime Listesi Olustur
[2] Kelime Listesi Sec
[3] Kelime Listesini Duzenle
[4] Kelimeleri Goruntule
[5] Calismayi Baslat
[6] Skor Tablosunu Goruntule
[7] Siniflari Goruntule

APP SETTINGS
[8] Yardim
[9] Ayarlar
[10] Bilgi
[11] Format
[12] Cikis """

duzenleMenu = """0=0=0=0=0=0=0=0=0=0=0

[1] Kelime Ekle 
[2] Kelime Cikar

0=0=0=0=0=0=0=0=0=0=0 """

ekleMenu = """0=0=0=0=0=0=0=0=0=0=0

[1] Manuel Ekle
[2] Internetten Ekle

0=0=0=0=0=0=0=0=0=0=0"""

# FUNCTIONS

def TLine(bosluk_adet):
	for i in range(0,bosluk_adet):
		print('')
		"""
		Sonrasinda yazi basilan her seyin sonuna
		TLine koy .
		"""
	
# VARIABLES

secili_liste = 'Secilmemis' # menude secili listeyi gosterir
liste_sayim = 1 # creator icin sayac
iptal = '(iptal etmek icin i ye basiniz)' # Tum inputlar icin ust menuye donus
kelime_sayim = 1 # kelimeleri listelemek icin sayac

# APP LOOP

print(mainMenu)

while True:
	
	if ayar_ana_klayve == 'EU':
		os.system('setxkbmap eu')
	elif ayar_ana_klayve == 'TR':
		os.system('setxkbmap tr')

	TLine(1)
	print('Secili Liste : ' + secili_liste)
	menuSecim = input('Seciminiz : ')

	if menuSecim == '1':
		TLine(1)
		isim_secim = input('Isim ' + iptal + ' : ')
		if isim_secim == '':
			TLine(1)
			print('Olusturulacak listenin bir ismi olmali !')
			pass
		elif isim_secim == 'i' or isim_secim == 'I':
			pass
		else:
			rw1.creator(isim_secim)
	
	elif menuSecim == '2':
		kullanici_listeler = os.listdir('user')
		"""
		Her liste secim ekraninda tekrar user 
		klasorunun icine baksin diye buraya 
		tanimladim .
		"""
		TLine(1)
		rw2.chooser(liste_sayim,kullanici_listeler)
		TLine(1)		
		if bool(kullanici_listeler) == False:
			pass
		else:
			liste_secim = input('Liste Numara ' + iptal + ' : ') 
			uzunluk = len(liste_secim)
			if int(liste_secim) > uzunluk or int(liste_secim) <= 0:
				TLine(1)
				print('Gecersiz Liste Numarasi !')
			elif liste_secim == 'i' or liste_secim == 'I':
				pass
			else:
				secili_liste = kullanici_listeler[int(liste_secim) - 1]
				
	elif menuSecim == '3':
			
			if secili_liste == 'Secilmemis':
				TLine(1)
				print('Lutfen oncelikle bir liste seciniz !')
			else:
				word_file = open('user/' + secili_liste + '/' + secili_liste + '.wl','a')
				mean_file = open('user/' + secili_liste + '/' + secili_liste + '.ml','a')

				TLine(1)
				print(duzenleMenu)
				TLine(1)
				duzenle_secim = input('Seciminiz : ')
				if duzenle_secim == '1':
					TLine(1)
					print(ekleMenu)				
					TLine(1)
					ekle_secim = input('Ekleme Turu : ')
					TLine(1)

					if ekle_secim == '1':
						while True:	
							if ayar_akilli_klavye == 'ON':
								os.system('setxkbmap eu')
							yeni_kelime = input('Kelime: ')
							if ayar_akilli_klavye == 'ON':
								os.system('setxkbmap tr')
							yeni_anlam = input('Kelimenin Anlami : ')
							if ayar_ana_klayve == 'EU':
								os.system('setxkbmap eu')
							elif ayar_ana_klayve == 'TR':
								os.system('setxkbmap tr')
							TLine(1)
							rw3.manual(word_file,mean_file,yeni_kelime,yeni_anlam)
							ekle_iptal = input('Iptal etmek icin i ye basiniz : ')
							if ekle_iptal == 'i' or ekle_iptal == 'I':
								break
			
					elif ekle_secim == '2':
						word_file = open('user/' + secili_liste + '/' + secili_liste + '.wl','r+')
						mean_file = open('user/' + secili_liste + '/' + secili_liste + '.ml','r+')
						current_words = word_file.read().splitlines() # rw4 web word_check
						current_means = mean_file.read().splitlines() # rw4 web mean_check
						word_file = open('user/' + secili_liste + '/' + secili_liste + '.wl','a')
						mean_file = open('user/' + secili_liste + '/' + secili_liste + '.ml','a')

						kelime_adet = input('Kac Adet (52128 words in database) ' + iptal + ' : ')
						if kelime_adet == 'i' or kelime_adet == 'I':
							pass
						else:
							TLine(1)
							rw4.web(int(kelime_adet),rwebdata.database,word_file,mean_file,current_words,current_means)
							
					else:
						TLine(1)
						print('Gecersiz secim !')
				
				elif duzenle_secim == '2':
					word_file = open('user/' + secili_liste + '/' + secili_liste + '.wl','r+')
					mean_file = open('user/' + secili_liste + '/' + secili_liste + '.ml','r+')
					word_lines = word_file.read().splitlines()
					mean_lines = mean_file.read().splitlines()
					os.system('rm -f ' + 'user/' + secili_liste + '/' + secili_liste + '.wl')
					os.system('rm -f ' + 'user/' + secili_liste + '/' + secili_liste + '.ml')
					os.system('touch ' + 'user/' + secili_liste + '/' + secili_liste + '.wl')
					os.system('touch ' + 'user/' + secili_liste + '/' + secili_liste + '.wl')
					word_file = open('user/' + secili_liste + '/' + secili_liste + '.wl','a')
					mean_file = open('user/' + secili_liste + '/' + secili_liste + '.ml','a')

					kelime_cikar = input('Cikarmak istediginiz kelime ' + iptal + ' : ')

					if kelime_cikar in word_lines and kelime_cikar not in mean_lines:
						cikarilacak_kelime = kelime_cikar
						numara = rw5.bul(cikarilacak_kelime,word_lines)
						cikarilacak_anlam = mean_lines[numara - 1]

						for word in word_lines:
							if word == cikarilacak_kelime:
								pass
							else:
								word_file.write(word + '\n')

						for mean in mean_lines:
							if mean == cikarilacak_anlam:
								pass
							else:
								mean_file.write(mean  + '\n')

					elif kelime_cikar in mean_lines and kelime_cikar not in word_lines:
						cikarilacak_anlam = kelime_cikar
						numara = rw5.bul(cikarilacak_anlam,mean_lines)
						cikarilacak_kelime = word_lines[numara - 1]

						for word in word_lines:
							if word == cikarilacak_kelime:
								pass
							else:
								word_file.write(word + '\n')

						for mean in mean_lines:
							if mean == cikarilacak_anlam:
								pass
							else:
								mean_file.write(mean + '\n')
					
					elif kelime_cikar == 'i' or kelime_cikar == 'I':
						pass

	elif menuSecim == '4':
		word_file = open('user/' + secili_liste + '/' + secili_liste + '.wl','r+')
		mean_file = open('user/' + secili_liste + '/' + secili_liste + '.ml','r+')
		word_lines = word_file.read().splitlines()
		mean_lines = mean_file.read().splitlines()

		TLine(1)
		for word in word_lines:
			numara = rw5.bul(word,word_lines)
			print(str(kelime_sayim) + '-) ' + word + ' = ' + mean_lines[numara - 1])
			kelime_sayim += 1

	elif menuSecim == '5':
		word_file = open('user/' + secili_liste + '/' + secili_liste + '.wl','r+')
		mean_file = open('user/' + secili_liste + '/' + secili_liste + '.ml','r+')
		word_lines = word_file.read().splitlines()
		mean_lines = mean_file.read().splitlines()
		words2 = []
		means2 = []
		words3 = []
		means3 = []

		# Skor hesabi
		leaderboard = open('leaderboard','a')
		
		soru_sayi = len(word_lines)
		start = time.time()
		rwork.calisma(word_lines,mean_lines,words2,means2,ayar_akilli_klavye,ayar_ana_klayve)
		end = time.time()
		total_time = round(end - start, 2) # kullanilan zaman
		yanlis = len(words2) # yanlislar
		dogru = soru_sayi - yanlis # dogrular

		skor = dogru * 100 - yanlis * 25 - total_time * 1
		
		# Tags
		if skor < -50 :
			tag = '🤓 Unrecoverable'
		elif -50 < skor and skor < 0:
			tag = '💩 Noob'
		elif 0 < skor and skor < 50:
			tag = '😕 Bad'
		elif 50 < skor and skor < 100:
			tag = '😐 Normal'
		elif 100 < skor and skor < 150:
			tag = '😀 Good'
		elif 150 < skor and skor < 200:
			tag = '🤖 Robot'
		elif 200 < skor:
			tag = '👽 Alien'
		
		# Save Score and Admins
		print('Skorunuz :', skor)
		save_score = input('Isim : ')
		
		if save_score == 'coderman':
			leaderboard.write(save_score + ' ==> ' + str(skor) + ' 😎 Creator' + '\n')
		elif save_score == 'lusey':
			leaderboard.write(save_score + ' ==> ' + str(skor) + ' 😺  Developer' + '\n')
		else:
			leaderboard.write(save_score + ' ==> ' + str(skor) + ' ' + tag + '\n')

		# Settings 1
		if ayar_tekrar_sor == 'ON':
			rwork.calisma(words2,means2,words3,means3,ayar_akilli_klavye,ayar_ana_klayve)

	elif menuSecim == '6':
		leaderboard = open('leaderboard','r+')
		user_scores = leaderboard.read().splitlines()
		TLine(1)
		for user_score in user_scores:
			print(user_score)

	elif menuSecim == '7':
		print("""
0=0=0=0=0=0=0=0=0=0=0

[NORMALLY USERS]
🤓 Unrecoverable (S<-50)
💩 Noob (-50<S<0)
😕 Bad (0<S<50)
😐 Normal (50<S<100)
😀 Good (100<S<150)
🤖 Robot (150<S<200)
👽 Alien (200<S)

[ADMINS]
😎 Creator 
😺 Developer

0=0=0=0=0=0=0=0=0=0=0
""")

	# APP SETTINGS
	elif menuSecim == '8':
		webbrowser.open('documentation.html')

	elif menuSecim == '9':
			print("""
AYARLAR
[1] Bilemediklerini tekrar sor : """ + ayar_tekrar_sor + """
[2] Akilli klavye : """ + ayar_akilli_klavye + """
[3] Birincil klave : """ + ayar_ana_klayve)

			ayar_degisim = input('Degistirmek istediginiz ayar ' + iptal + ' : ')
			
			# tekrar sor
			if ayar_degisim == '1':
				ayar_degisim_1 = input('[ON] Ac, [OFF] Kapali : ')
				if ayar_degisim_1 == 'ON':
					ayar_tekrar_sor = 'ON'
				elif ayar_degisim_1 == 'OFF':
					ayar_tekrar_sor = 'OFF'
			
			# akilli klavye
			elif ayar_degisim == '2':
				ayar_degisim_2 = input('[ON] Ac, [OFF] Kapali : ')
				if ayar_degisim_2 == 'ON':
					ayar_akilli_klavye = 'ON'
				elif ayar_degisim_2 == 'OFF':
					ayar_akilli_klavye = 'OFF'
			
			# ana klavye
			elif ayar_degisim == '3':
				ayar_degisim_1 = input('[EU] Ingilizce, [TR] Turkce : ')
				if ayar_degisim_1 == 'EU':
					ayar_ana_klayve = 'EU'
				elif ayar_degisim_1 == 'TR':
					ayar_ana_klayve = 'TR'

			# iptal
			elif ayar_degisim == 'i':
				pass

	elif menuSecim == '10':
		print('Surum : ' + RWords_surum)
		if secili_liste != 'Secilmemis':
			word_file = open('user/' + secili_liste + '/' + secili_liste + '.wl','r+')
			word_lines = word_file.read().splitlines()
			print('Kelime Sayisi : ' + str(len(word_lines)))

	elif menuSecim == '11':
		# delete user lists
		os.system('rm -rf user')
		os.mkdir('user')
		secili_liste = 'Secilmemis'

		# clear leaderboard
		os.system('rm -f leaderboard')
		os.system('touch leaderboard')

	elif menuSecim == '12':
		sys.exit()


