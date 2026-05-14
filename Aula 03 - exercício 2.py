# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:48:59 2026

@author: Sophia
"""

nome = input('\nQual o nome do aluno? ')
g1 = float(input('\nQual foi a nota da G1 do aluno? '))
g2 = float(input('\nQual foi a nota da G2 do aluno? '))

media = (2*g1 + 3*g2)/ 5

print('\nA média do aluno {} é {}'.format(nome,media))
