import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:    
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')    
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):        
        self._cards = [Card(rank, suit) for suit in self.suits                                        
                                        for rank in self.ranks]
    def __len__(self):        
        return len(self._cards)
    def __getitem__(self, position):        
        return self._cards[position] 
    
deck = FrenchDeck()
    
from random import choice

N = 7*[None]
for i in range ( 7 ) : 
    N[i] = choice(deck)
M = [choice(deck) for i in range(7)]
print (N[i].rank)
print (M)