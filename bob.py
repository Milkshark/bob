import random as r

def correct(liste):
    suite = 0
    chiffre_de_suite = liste[0]
    for e in liste:
        if e == chiffre_de_suite:
            suite += 1
            if suite > 2:
                return (False)
        else:
            suite = 0
        chiffre_de_suite = e
    return (True)


def liste_up_low(n):
    liste = []
    for i in range(n):
        liste.append(r.randint(0,1))
    if correct(liste):
        return (liste)
    else:
        return(liste_up_low(n))
        
 
def mot_casse(mot):
    mot_c = ''
    li = liste_up_low(len(mot))
    li[0] = 1
    for i in range(len(mot)):
        if li[i] == 0:
            mot_c += mot[i].upper()
        else:
            mot_c += mot[i].lower()
        
    return mot_c

def bob(phrase):
    phrase_c = ''
    for word in phrase.split(' '):
        phrase_c += mot_casse(word) + ' '
    return phrase_c


