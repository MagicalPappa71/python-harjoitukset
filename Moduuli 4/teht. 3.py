# Ohjelma, joka kysyy biologisen sukupuolen ja hemoglobiiniarvoa.
sukupuoli = input("Anna sukupuoli:")
hemoglobiini = int(input("Anna hemoglobiinin arvo"))
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
if sukupuoli == "nainen" and hemoglobiini > 175:
    print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "nainen" and hemoglobiini < 117:
    print ("Hemoglbiiniarvo on alhainen.")
elif sukupuoli == "nainen" and 175 >= hemoglobiini >= 117:
    print("Hemoglobiiniarvo on normaali.")


elif sukupuoli == "mies" and hemoglobiini > 195:
    print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "mies" and hemoglobiini < 134:
    print("Hemoglobiiniarvo on alhainen.")
elif sukupuoli == "mies" and 195 >= hemoglobiini or "mies" and hemoglobiini <= 134:  
    print("Hemoglobiiniarvo on normaali.")

else:
    print("ei ole ihminen")

