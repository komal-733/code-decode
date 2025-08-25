import random
import string
def coding(s):
  w=s.split()
  for a,i in enumerate(w):
    if len(i)>2:
      w[a]=''.join(random.choices(string.ascii_letters,k=3))+i[1:]+i[0]+''.join(random.choices(string.ascii_letters,k=3))
    else :
      w[a]=i[::-1]
  print(' '.join(w))

def decoding(s):
  w=s.split()
  for a,i in enumerate(w):
    if len(i)>2:
      w[a]=i[-4]+i[3:-4]
    else :
      w[a]=i[::-1]
  print(' '.join(w))
  
c=int(input("0:decode\t\t1:encode\n"))
s=input("enter code: ")
if c :
  coding(s)
else:
  decoding(s)