import math

## Pyydä käyttäjältä ympyrän säde ja tallenna muuttujaan
radius = input("Anna säteen pituus senttimetreinä")

## laske ympyrän pinta-ala
## pi * säde potenssiin kaksi
area = math.pi * radius ** 2

## tulosta ympyrän pinta-ala
print("Ympyrän pinta-ala on: " + str (area))
