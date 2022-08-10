import random
import os
import sys
sys.path.insert(0, 'rws/')
import rw5
sys.path.insert(0, '')

# Renkler                                                                                   
class bcolors:                                                                              
    WARNING = '\033[93m'                                                                    
    ENDC = '\033[0m'                                                                        
    RED = '\u001b[31m'                                                                      
    ACIKMAVI = '\u001b[32;1m'

def calisma(word_list,mean_list,backup_words,backup_means,setting2,setting3):
  os.system('clear')
  soru_sayac = 1
  forms = ['en-tr','tr-en']
  soru_sayi = len(word_list)
  while True:
    
    if bool(word_list) == False and bool(mean_list) == False:
      print('Calisma Bitti')
      if setting3 == 'EU':
        os.system('setxkbmap eu')
      elif setting3 == 'TR':
        os.system('setxkbmap tr')
      break

    else:
      form = random.choice(forms)
      if form == 'en-tr':
        random_word = random.choice(word_list)
        r_line = rw5.bul(random_word,word_list)
        answer = mean_list[r_line - 1]
        
        if setting2 == 'ON':
          os.system('setxkbmap tr')
        print('')
        quest = input(bcolors.RED + str(soru_sayi) + '-) ' + bcolors.ENDC + bcolors.ACIKMAVI + random_word + ' = ' + bcolors.ENDC)
        soru_sayac += 1
        soru_sayi -= 1
        if soru_sayac == 20:
            soru_sayac = 0
            os.system('clear')
        
        if quest == answer:
          word_list.remove(random_word)
          mean_list.remove(answer)
        else:
          print('yanlis cevap ! ' + answer + ' olacakti .')
          word_list.remove(random_word)
          mean_list.remove(answer)
          backup_words.append(random_word)
          backup_means.append(answer)

      elif form == 'tr-en':
        random_mean = random.choice(mean_list)
        m_line = rw5.bul(random_mean,mean_list)
        answer = word_list[m_line - 1]

        if setting2 == 'ON':
          os.system('setxkbmap eu')
        print('')
        quest = input(bcolors.RED + str(soru_sayi) + '-) ' + bcolors.ENDC + bcolors.ACIKMAVI + random_mean + ' = ' + bcolors.ENDC)
        soru_sayac += 1
        soru_sayi -= 1
        if soru_sayac == 20:
            soru_sayac = 0
            os.system('clear')
        
        if quest == answer:
          word_list.remove(answer)
          mean_list.remove(random_mean)
        else:
          print('yanlis cevap ! ' + answer + ' olacakti .')
          mean_list.remove(random_mean)
          word_list.remove(answer)
          backup_means.append(random_mean)
          backup_words.append(answer)
