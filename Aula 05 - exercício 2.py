# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:15:15 2026

@author: Sophia
"""

def cria_nome_completo(nom,sob):
    nc = nome + ' ' + sob
    return nc

#BP

nm = 'Lala'
sb = 'Patinhas'

nmComp = cria_nome_completo(nm,sb)
print(nmComp)

nomComp = cria_nome_completo('Tigre','Fofão')
print(nomComp)

print(cria_nome_completo('Miki','Feliz'))