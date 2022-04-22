# -*- coding: utf-8 -*-
# you will need to install pycryptodome and bitsring, use the below command in colab or your terminal:
# !pip install pycryptodome
# !pip install bitstring

#Part 1: Testing the avalanche properties of AES using an automated code
#Part 2: Encrypting and decrypting a file using AES and DES
#import numpy as np

from Crypto.Util.Padding import pad,unpad
from Crypto.Cipher import DES, AES
from bitstring import BitArray


def aes_encryption(inputblock,key):
    aes_enc=AES.new(key,AES.MODE_ECB)
    aes_cipher=aes_enc.encrypt(inputblock)
    
    return aes_cipher

def padding(inputblock,size):
    if len(inputblock)<size:
        input_pad=pad(inputblock,size)
    else:
        input_pad=inputblock
    
    return input_pad




def bd(old,new):
    l=[]
#    num=0
    for i,j in zip(old,new):
#        print(i,j)
            if i!=j:
                l.append(j)
    return len(l)
                
        

def i(inputblock_padded,b):
    inputinhex=inputblock_padded.hex()
#    print("inputinhex",inputinhex )
    byte=BitArray(hex=inputinhex)
#    print("byte",byte)
    d=byte.bin
#    print("d", d[b])
    if d[b]=='0':
        new_char='1'
    elif d[b]=='1':
        new_char='0'
#    print(new_char)
    input_binary=d[:b]+new_char+d[b+1:]
#    print(input_binary)
##    print("After changinng",inputinhex1)
    decimal_representation = int(input_binary, 2)
    hexadecimal_string = hex(decimal_representation)
##    print(hexadecimal_string)
    hex1=hexadecimal_string[2:]
#    print('hex1',hex1)
    bytefromhex=bytes.fromhex(hex1)
    
    return bytefromhex   


def aes_input_av_test(inputblock,key,bitlist):
    diff_list=[]
    aes_enc=AES.new(key,AES.MODE_ECB)
    inputblock_padded=pad(inputblock,16)
#    print("After padding",inputblock_padded)
#    print("len after padding",len(inputblock_padded))
    aes_cipher=aes_enc.encrypt(inputblock_padded)
    org_in_hex=aes_cipher.hex()
    org_byte=BitArray(hex=org_in_hex)
    org_in_bin=org_byte.bin

#    print(aes_cipher.hex())
    
    for b in bitlist:
        newinput=i(inputblock_padded,b)
#        print("new input",newinput)
       
       
        new_cipher=aes_enc.encrypt(newinput)
#        print("new_cipher",new_cipher.hex())
        
        new_in_hex=new_cipher.hex()
        new_byte=BitArray(hex=new_in_hex)
        new_in_bin=new_byte.bin
        
        numbitdifferences = bd(org_in_bin, new_in_bin)
#        print("diff",numbitdifferences)
        diff_list.append(numbitdifferences)
    return diff_list


def aes_key_av_test(inputblock, key, bitlist):
    diff_list=[]
    inputblock_padded=padding(inputblock,16)
    org_cipher=aes_encryption(inputblock_padded,key)
    
    org_in_hex=org_cipher.hex()
    org_byte=BitArray(hex=org_in_hex)
    org_in_bin=org_byte.bin
    
    
    for b in bitlist:
        new_key=i(key,b)
        new_cipher=aes_encryption(inputblock_padded,new_key)
        
        org_in_hex=new_cipher.hex()
        org_byte=BitArray(hex=org_in_hex)
        new_in_bin=org_byte.bin
    
                
        
        bit_diff=bd(org_in_bin,new_in_bin)
        diff_list.append(bit_diff)
    return diff_list

        

###### PART2 ####
    

def encrypt_file(inputfile,des_key,aes_key,des_output_file,aes_output_file):
  finp=open(inputfile,'rb')
  filebytes=finp.read()
#  print(len(filebytes))
  #file_enc=aes_encryption()
  finp.close()
  
  fout_des=open(des_output_file,'wb')
  for i in range(0,len(filebytes),8):
    splits=filebytes[i:i+8]
    splits_pad_des=padding(splits,8)
    splits_des=des_encryption(splits_pad_des,des_key)
#    split_hex=splits_des.hex()
#    print("DES",split_hex)

    fout_des.write(splits_des)
  fout_des.close()


  fout_aes = open(aes_output_file,'wb')
  for i in range(0,len(filebytes),16):
    splits=filebytes[i:i+16]
    splits_pad=padding(splits,16)
    splits_enc=aes_encryption(splits_pad,aes_key)
#    split_enc_hex=splits_enc.hex()
#    print("AES",split_enc_hex)

    fout_aes.write(splits_enc)
  fout_aes.close()
  return 0

def decrypt_file(des_input_file,aes_input_file,des_key,aes_key,des_output_file,aes_output_file):
  #This function should create 2 output files. One for DES decryption, and the other for AES decryption.
    
    #Open a read file handler for the DES ciphertext input file.
    finp_des = open(des_input_file,'rb')
    #rb stands for read bytes.
    #Then read the bytes from the file and store them in a variable.
    filebytes_des = finp_des.read()
    #Then close the file.
    finp_des.close()


    '''
    For DES:
    in a loop, break filebytes into 8 bytes chunks
    run decryption for each block of 8 bytes
    Then write the final plaintext in the output file
    '''

    fout_des = open(des_output_file,'wb')
    # dec_string_des=b''
    for i in range(0,len(filebytes_des),8):
      splits=filebytes_des[i:i+8]
      splits_pad_des=padding(splits,8)
      
      try:
        splits_dec=unpad(des_decryption(splits_pad_des,des_key),8)
      except:
        splits_dec=des_decryption(splits_pad_des,des_key)

      # if len(filebytes_des)%8!=0:
      #   splits_dec=unpad(des_decryption(splits_pad_des,des_key),8)
      # else:
      #   splits_dec=des_decryption(splits_pad_des,des_key)

      # dec_string_des += splits_dec

    #  dec_string_des=unpad(dec_string_des , 8)
    #  print("dec string",dec_string_des)
#      print("DES", splits_dec)
      fout_des.write(splits_dec)
    fout_des.close()


    #Open a read file handler for the AES ciphertext input file.
    finp_aes = open(aes_input_file,'rb')
    #rb stands for read bytes.
    #Then read the bytes from the file and store them in a variable.
    filebytes_aes = finp_aes.read()
    #Then close the file.
    finp_aes.close()

    '''
    For AES:
    in a loop, break filebytes into 16 bytes chunks
    run decryption for each block of 16 bytes
    Then write the final plaintext in the output file
    '''
    fout_aes = open(aes_output_file,'wb')
    # dec_string=b''
    for i in range(0,len(filebytes_aes),16):
      splits=filebytes_aes[i:i+16]
      splits_pad=padding(splits,16)
      try:
        splits_aes_dec=unpad(aes_decryption(splits_pad,aes_key),16)
      except:
        splits_aes_dec=aes_decryption(splits_pad,aes_key)

#      print(splits_aes_dec)
      fout_aes.write(splits_aes_dec)
      #print(len(splits_aes_dec))
    fout_aes.close()

    return 0

        
  
def des_encryption(inputblock,key):
  des_enc=DES.new(key, DES.MODE_ECB)
  des_cipher=des_enc.encrypt(inputblock)

  return des_cipher

def des_decryption(cipher,key):
  my_dec_cipher = DES.new(key, DES.MODE_ECB)
  des_decryption=my_dec_cipher.decrypt(cipher)

  return des_decryption

def aes_decryption(cipher,key):
  my_aes_cipher = AES.new(key, AES.MODE_ECB)
  aes_decryption=my_aes_cipher.decrypt(cipher)
  
  return aes_decryption

print(aes_input_av_test(b'solongpadawan', b'verynicelongbyte',[0,29,68,100,127]),
aes_key_av_test(b'solongpadawan', b'verynicelongbyte',[0,29,68,100,127]),
encrypt_file('input.txt',b'8bytekey',b'veryverylongkey!','des_input.txt','aes_input.txt'),
decrypt_file('des_input.txt','aes_input.txt',b'8bytekey',b'veryverylongkey!','des_output.txt','aes_output.txt'))

aes_input_av_test(b'solongpadawan', b'verynicelongbyte',[0,29,68,100,127])

