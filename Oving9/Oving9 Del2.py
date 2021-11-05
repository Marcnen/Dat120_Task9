# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 11:49:58 2021

@author: Marcus Vik
"""

#self for å rope på variabler 

class Quiz: #grunnmur
    
    def __init__(self, spørsmål, alternativ, svar = 0): #init = hovedbrikker (spørsmål, alternativ, svar)
        self.spørsmål = spørsmål
        self.alternativ = alternativ
        self.svar = svar - 1 #ikke starte på 0
        
    def __str__(self): #skrive ut class
        utskrift = self.spørsmål + "\n" 
        for index, verdi in enumerate(self.alternativ): #index, verdi i en liste
            utskrift += f"{index + 1}) {verdi}\n" #alternativene (index + verdi)
        return utskrift # gi utskrift
    
    def sjekk_svar(self, riktig_svar):
        if riktig_svar - 1 == self.svar:
            return True
        else: 
            return False
        
        
def start(SP, AL, SV):
    quiz_spørsmål = Quiz(SP, AL, SV)
    print(quiz_spørsmål)
    brukerens_svar = int(input(f"Skriv inn tallet på svaret du velger: "))
    
    if quiz_spørsmål.sjekk_svar(brukerens_svar):
        print(f"Riktig svar!!\n")
        
    else:
        print(f"Feil svar, det riktige svaret var: {quiz_spørsmål.svar + 1}) {quiz_spørsmål.alternativ[quiz_spørsmål.svar]}\n")     
        


start("Hva er den største ørkenen i verden", ["Sahara ørkenen", "Antarktis" ], 2)
start("Hva er 1+1", [1, 2, 3, 4], 2) 
start("Hva er 5*5", [10, 15, 20, 25], 4)