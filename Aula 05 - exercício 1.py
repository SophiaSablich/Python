# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:52:05 2026

@author: Sophia
"""

def grau(prova,teste01,teste02):
    calc = prova * 0.7 + teste01 * 0.1 + teste02 * 0.2
    return calc

nome = input('\nNome do aluno: ')

B1_p = float(input('\nNota da prova do bloco 1: '))
B1_t1 = float(input('Nota do teste do bloco 1: '))
B1_t2 = float(input('Nota do teste do bloco 1: '))

B1 = grau(B1_p,B1_t1,B1_t2)

B2_p = float(input('\nNota da prova do bloco 2: '))
B2_t1 = float(input('Nota do teste do bloco 2: '))
B2_t2 = float(input('Nota do teste do bloco 2: '))

B2 = grau(B2_p,B2_t1,B2_t2)

print('\nO nome do(a) aluno(a) é {}, o grau do bloco 1 é {:.1f} e o grau do bloco 2 é {:.1f}'.format(nome,B1,B2))