# RW3 ==> Web Uzerinden Ekle
# created by c0d3rm4n

from deep_translator import GoogleTranslator
import random

def web(adet,database,word_target,mean_target,word_check,mean_check):

  """ adet ==> kac kelime istedigi
  database ==> kelimeleri cekecegimiz liste objesi
  word_target ==> kelime listesi
  mean_target ==> anlam listesi 
  word_check ==> listeye daha onceden yazilmis olan kelimeler 
  mean_check ==> listeye daha onceden yazilmis olan anlamlar """

  print('[E] Ekle, [C] Cikar, [D] Duzenle' + '\n')

  for i in range(0,adet):
    random_word = random.choice(database)
    random_mean = GoogleTranslator(source='auto', target='tr').translate(random_word)
    
    web_secim = input(random_word + ' = ' + random_mean + '\n' + 'secim : ')
    print('')

    if web_secim == 'e' or web_secim == 'E':
      if random_word in word_check:
        print('Zaten mevcut' + '\n')
      else:
        word_target.write(random_word + '\n')
        mean_target.write(random_mean + '\n')

    elif web_secim == 'c' or web_secim == 'C':
      pass
    
    elif web_secim == 'd' or web_secim == 'D':
      new_word = input(random_word + ' >> ')
      new_mean = input(random_mean + ' >> ')
      print('')
      word_target.write(new_word + '\n')
      mean_target.write(new_mean + '\n')

    database.remove(random_word)