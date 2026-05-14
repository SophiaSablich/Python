# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:50:26 2026

@author: PC18
"""

# Sophia Sablich - 2521027
# Turma 33J - Profª Joísa
# Exercício: idade futura
    
import random

nome = input('\nNome: ')
idade = int(input('\nIdade atual: '))
ano = int(input('\nAno corrente: '))

ano_x = random.randint(ano,2050)
idade_x = (ano_x - ano) + idade

print('\nObserve que nessa rodada foi gerado o ano {}'.format(ano_x))

print('\nAtualmente, em {}, {} tem {} anos'.format(ano,nome,idade))
print('\nEm {}: {} terá {} anos'.format(ano_x,nome,idade_x))