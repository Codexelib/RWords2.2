# RW2 ==> Kelime Listesi Sec
# created by c0d3rm4n

import os

def chooser(sayac,listeler):
	print('0=0=0=0=0=0=0=0=0=0=0' + '\n')
	
	if bool(listeler) == False:
		print('  EMPTY')
		
	else:
		for liste in listeler:
			print(sayac, '- ' + liste)
			sayac += 1
	
	print('\n' + '0=0=0=0=0=0=0=0=0=0=0')
		