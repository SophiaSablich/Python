# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:16:08 2026

@author: Sophia
"""

# Função Calculo da área de um retângulo
# Recebe parâmetro - base e altura
# Retorna a área do retângulo


def calcAreaRet(base,altura):
    area = base * altura
    return area

def moldura():
    print(20 * '-')

def moldura_escolhida(tam,caractere):
    print(tam * caractere)
    
# Bloco Principal

moldura()

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
d = float(input('d: '))

areaMaior = calcAreaRet(a,b)
areaMenor = calcAreaRet(c,d)
areaPint = areaMaior - areaMenor

moldura()

moldura_escolhida(30,'#')

print('A área pintada é {:.1f}'.format(areaPint))

moldura_escolhida(30,'#')

moldura()