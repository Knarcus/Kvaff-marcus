
from linkedQFile import LinkedQ

""" 
1. Vårt mål här är att bryta ned alla fraser rekursivt och kontrollera att allting stämmer
 

"""

class Grammatik_fel(Exception):
    pass # Läs sedan vad det här är och vad det betyder?



def kontrollera_molekyl(molekyl):
    kontrollera_atom(molekyl)
    if molekyl.peek() == ".":
        molekyl.dequeue()
    else:
        kontrollera_nummer(molekyl)


def kontrollera_atom(molekyl):
    # atomer bör stå på form Xx12 där X är stor bokstav, x är liten bokstav och 12 är ett nummer
    kontrollera_stor_bokstav(molekyl)
    if molekyl.peek().isalpha():
        kontrollera_liten_bokstav(molekyl)
        

def kontrollera_stor_bokstav(molekyl):
    # Kontrollera att det är en stor bokstav
    stor_bokstav = molekyl.peek()
    if stor_bokstav.isupper():
        molekyl.dequeue()
        return
    atom_str = ""
    while molekyl.peek()!= ".":
        atom_str += molekyl.dequeue()
    raise Grammatik_fel("Saknad stor bokstav vid radslutet " + atom_str)


def kontrollera_liten_bokstav(molekyl):
    # Kontrollera att det är en liten bokstav
    liten_bokstav = molekyl.dequeue()
    if liten_bokstav.islower():
        return
    raise Grammatik_fel("Fel alla andra bokstäver måste vara gemener: " + liten_bokstav)


def kontrollera_nummer(molekyl):
    # Jag förstår inte riktigt men jag tror att det kan lösa sig senare.
    nr_str = ""
    while molekyl.peek() != "." and molekyl.peek().isdigit():
        char = molekyl.dequeue()
        nr_str += char
    num = int(nr_str)
    if num > 1 and nr_str[0] != "0":
        return    
    raise Grammatik_fel("För litet tal vid radslutet " + nr_str[1:])
        
    

def kolla_grammatiken(molekyl):
    molekyl = bryt_ned_molekyl(molekyl)
    
    try:
        kontrollera_molekyl(molekyl)
        return "Formeln är syntaktiskt korrekt"
    except Grammatik_fel as fel:
        return str(fel)

def bryt_ned_molekyl(molekyl):
    q = LinkedQ()
    for char in molekyl: # Iterera över varje tecken
        q.enqueue(char)
    q.enqueue(".") # Lägg till en punkt i slutet som markerar slutet på molekylen
    return q

def main():
    while True:
        molekyl = input()
        if molekyl != "#":
            resultat = kolla_grammatiken(molekyl)
            print(resultat)
        else:
            break


"""import unittest
class SyntaxTest(unittest.TestCase):
    
    # Testet fungerar på det sättet att du skriver given input och förklarar vad som ska komma ut från det
    def testSubjmolekyl(self):
        self.assertEqual(kolla_grammatiken("He25"), "Följer vår syntax")

    def testFelmolekyl(self):
        self.assertEqual(kolla_grammatiken("HE25"), "Fel alla andra bokstäver måste vara liten: E")

if __name__ == '__main__':
    unittest.main() """


main()
