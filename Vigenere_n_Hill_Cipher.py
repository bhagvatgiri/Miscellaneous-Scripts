# -*- coding: utf-8 -*-
import numpy as np

def string_vi(key,input_string):
    input_string= input_string.replace(' ','').upper()
    key_len = len(key)
    input_string_len = len(input_string)
    z = input_string_len-key_len
    l = []
    for i in range(key_len):
        l.append(key[i])
    for i in range(z):
        l.append(key[i%key_len])
    return l,input_string

 

def vigenere_enc(key,input_string):
        key,input_string = string_vi(key,input_string)
        input_string_list = []
        for i in range(len(input_string)):
            input_string_list.append(input_string[i])
        input_string_new = []
        for i in range(len(input_string)):
            shift = ord(key[i])-65
            input_string_new.append(chr((ord(input_string_list[i]) -65 + shift)%26 +65))
        a=''
        for i in range(len(input_string_new)):
            a = a + input_string_new[i]
        return a

def vigenere_dec(key,input_string):
    key,input_string = string_vi(key,input_string)
    input_string_list = []
    for i in range(len(input_string)):
            input_string_list.append(input_string[i])
    input_string_new = []
    for i in range(len(input_string)):
        shift = ord(key[i])-65
        input_string_new.append(chr((ord(input_string_list[i])-65 -shift)%26 +65))
    a=''
    for i in range(len(input_string_new)):
        a = a + input_string_new[i]
    return a

def string_vi(key,input_string):
  input_string= input_string.replace(' ','').upper()
  key_len = len(key)
  input_string_len = len(input_string)
  z = input_string_len-key_len
  l = []
  for i in range(key_len):
    l.append(key[i])
  for i in range(z):
    l.append(key[i%key_len])
  return l,input_string

 

def vigenere_enc(key,input_string):
        key,input_string = string_vi(key,input_string)
        input_string_list = []
        for i in range(len(input_string)):
            input_string_list.append(input_string[i])
        input_string_new = []
        for i in range(len(input_string)):
            shift = ord(key[i])-65
            input_string_new.append(chr((ord(input_string_list[i]) -65 + shift)%26 +65))
        a=''
        for i in range(len(input_string_new)):
            a = a + input_string_new[i]
        return a

def vigenere_dec(key,input_string):
    key,input_string = string_vi(key,input_string)
    input_string_list = []
    for i in range(len(input_string)):
            input_string_list.append(input_string[i])
    input_string_new = []
    for i in range(len(input_string)):
        shift = ord(key[i])-65
        input_string_new.append(chr((ord(input_string_list[i])-65 -shift)%26 +65))
    a=''
    for i in range(len(input_string_new)):
        a = a + input_string_new[i]
    return a

def hill_cipher_string_padding(input_string):
    input_string = input_string.replace(" ","").upper()
    if len(input_string)%3 == 0:
      return x
    elif len(input_string)%3 == 1:
      input_string = input_string + 'XX'
      return input_string
    else:
        input_string = input_string + 'X'
        return input_String
        
        
def hill_enc(M,input_string):
        y = hill_cipher_string_padding(input_string)
        length = len(y)/3
        list = []
        for i in y:
            list.append(ord(i)-65)
        array1= np.array(list)
        plain_text = np.array_split(array1,length)
        j = []
        for i in range(int(length)):
            j.append(np.matmul(plain_text[i],M))
        j = np.array(j)
        j =j%26 + 65
        k = np.resize(j,(1,len(y)))
        k_list = k[0].tolist()
        a=''
        for i in k_list:
            a = a + chr(i)
        return a 


def hill_dec(M,input_string):
    input_string= hill_cipher_string_padding(input_string)
    Mod26invTable = {}
    for m in range(26):
      for minv in range(26):
        if (m*minv)%26==1:
          Mod26invTable[m] = minv
    Minv = np.linalg.inv(M)
    Mdet = np.linalg.det(M)
    Madj = Mdet*Minv
    Madj26 = Madj % 26
    Mdet26 = Mdet%26
    if Mdet26 in Mod26invTable:
      Mdet26inv = Mod26invTable[Mdet26]
    else:
      Mdet26inv = -1
    Minv26 = (Mdet26inv*Madj26)%26
    length = len(input_string)/3
    list = []
    for i in input_string:
        list.append(ord(i)-65)
    array2 = np.array(list)
    plain_text = np.array_split(array2,length)
    plain_text = np.array(plain_text)
    a=[]
    for i in range(int(length)):
        a.append(np.matrix.round(np.matmul(plain_text[i],Minv26))%26)
    a = np.array(a)
    a=a+ 65
    re = np.resize(a,(1,len(input_string)))
    re_list = re[0].tolist()
    relist = []
    for i in re_list:
        relist.append(int(i))
    p=''
    for i in relist:
        p = p + chr(i)
    return p 



  
if __name__=="__main__":
  x=hill_enc(np.array([[17,17,5],[21,18,21],[2,2,19]]),'Test string')
  v=hill_dec(np.array([[17,17,5],[21,18,21],[2,2,19]]),'BPBLJCPRGHQO')
  print(x,v)
  o=vigenere_enc('KEY', 'Test String')
  q=vigenere_dec('KEY','DIQDWRBMLQ')
  print(o,q)

