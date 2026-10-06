# Ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia.
# Käytetään import random, kun kyseessä tulostetaan satunnaisia numeroita.
import random 
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
print(random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))
print(random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))


