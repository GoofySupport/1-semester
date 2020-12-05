# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:18:33 2020

@author: stoff
"""

import random 
from itertools import product

spillekort =[]

 
kuløre = ['hjerter' , 'spar', 'klør', 'ruder']
    
ranks = ['to' , 'tre', 'fire', 'fem' , 'seks', 'syv', 'otte' ,
            'ni', 'ti', 'knægt' , 'dame', 'konge', 'es' ]

"""
Laver et deck hvor alle kort er i og får dem blandet 
Bliver printet som en liste 
"""

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        
    def show(self):
        print('{} {}'. format(self.suit , self.value))

class Deck(object):

# Nested for loop der udskriver alle kort og giver dem værdier, blander dem

    værdier = 2
    for rank in ranks:
        for kulør in kuløre:
            spillekort.append([kulør + ' ' + rank, værdier])
        værdier +=1
    
    random.shuffle(spillekort)
    
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        for s in kuløre:
            for v in ranks:
                self.cards.append(Card(s, v))
            
    
    def show(self):
        for c in self.cards:
           c.show()
    
    def drawCard(self):
        return self.cards.pop()

    def bland(self):
        for i in range(len(self.cards) -1,0 , -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            

"""
Laver spillere hvor man selv kan indsætte navn
Øverst vil der være alle variabler
Det ender ud i en liste af spillere 


"""

class Spil:
    
    def __init__(self):
         antal_spiller = 0
         self.players = []
         playerTurn = 0
         self.hand = []
         
    def tilføj_spiller(self,players):
        self.players.append(players)
        
    def draw(self, deck):
        self.hand.append(Deck.drawCard())
        return self
        
    def showHands(self):
        for card in self.hand:
            card.show()
    
    
    


class Spillere:
     
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name        
        
        
    def fullname(self):
        return '{} {}'. format(self.first , self.last)
    
    

spiller_1 = Spillere('first', 'ast')
spiller_2 = Spillere('kris', 'kris')
spiller_3 = Spillere('Hey' , '2')

deck = Deck()

deck.show()  # meget vigtig fordi den kan bruges i class spil til at give kort eller lave spillere osv.

spiller_1.Spil(draw(deck))

spiller_1.draw(deck)
spiller_1.showHands()

