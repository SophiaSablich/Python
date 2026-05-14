# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:26:42 2026

@author: Sophia
"""

def convert_GBP(GBP):
    convert = 1.23 * GBP
    return convert

def convert_DL(DL):
    convert = 5.24 * DL
    return convert

valor_GBP = float(input('\nLibras esterlinas: '))

convert_D = convert_GBP(valor_GBP) 

print('\nA conversão de libras esterlinas para dólares é {}'.format(convert_D))

valor_DL = float(input('\nDólares: '))

convert_BRL = convert_DL(valor_DL) 

print('\nA conversão de dólares para reais é {}'.format(convert_BRL))

valor_LDB = float(input('\nLibras esterlinas: '))

convert_LDB = convert_GBP(valor_LDB)
convert_LDBB = convert_DL(convert_LDB)

print('\nDólares:  {}\nReais: {:.2f}'.format(convert_LDB,convert_LDBB))