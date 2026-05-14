# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:29:23 2026

@author: PC18
"""

# Sophia Sablich - 2521027
# Turma 33J - Profª Joísa
# Exercício: IMC

nome = input('\nNome: ')
alt = float(input('\nAltura: '))
kg = float(input('\nPeso: '))

imc = kg / (alt * alt)

print('\n{} tem IMC igual a {:.1f}'.format(nome,imc))