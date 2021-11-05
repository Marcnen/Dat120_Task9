# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 10:34:57 2021

@author: Marcus Vik
"""

samling = {} #dictonary 
with open("oving_1_rein_tekst.txt", "r", encoding="UTF8") as fil: #open + norsk alfabete 
    linjeteller = 0 
    for linje in fil:
        linje = linje.split() #splitter linjene (fjerner mellomrom linjene)
        linjeteller += 1 #teller hver linje med 1
        for ordet in linje:
            ordet = ordet.lower() #gjør alle ord til små bokstaver 
            if ordet in samling: #if orderet står i dictonary
                pass #gå videre 
            else:
                samling[ordet] = linjeteller #if ordet ikke er der, putt i dictonary
            
        
for ordene in samling:
    print(ordene, "- Linje", samling[ordene]) #print ut dictonary