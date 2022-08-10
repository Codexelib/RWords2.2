# RW3 ==> Kelime Silme
# created by c0d3rm4n


def sil(key,lines,file):
  """ key ==> silinecek kelime
      lines ==> hedef dosyanin icerigi
      file ==> dosya """
  
  if key in lines:
    for line in lines:
      if line == key:
        pass
      else:
        file.write(line + '\n')

def bul(key,lines):
  for i in range(0,len(lines)):
    if lines[i] == key:
      return i + 1
