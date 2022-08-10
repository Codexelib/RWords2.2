# RW1 ==> Yeni Kelime Listesi Olustur
# created by c0d3rm4n

import os
def creator(name):
	os.system('mkdir user/' + name)	
	os.system('touch user/' + name + '/' + name + '.wl')
	os.system('touch user/' + name + '/' + name + '.ml')