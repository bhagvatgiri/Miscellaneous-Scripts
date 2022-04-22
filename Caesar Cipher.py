#!/usr/bin/env python
# coding: utf-8

def caesar_str_enc(inpstring, k):
    outstring = ''
    for c in inpstring:
        if c == ' ':
            outstring = outstring + c
        else:
            outstring = outstring + chr((ord(c)+k-65)%26+65)
    return outstring

def caesar_str_dec(inpstring, k):
    outstring = ''
    for c in inpstring:
        if c == ' ':
            outstring = outstring + c
        else:
            outstring = outstring + chr((ord(c)-k-65)%26+65)    
    return outstring


