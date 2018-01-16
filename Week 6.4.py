richter = float(input("Enter the mangnitue on the Richter scale: "))
if richter >= 8.0:
    print("Most structures fall")
elif richter >= 7.0:
    print("Most buildings destroyed")
elif richter >= 6.0:
    print("Many building considerably damaged, some collapse")
elif richter >= 4.5:
    print("Damage to poorly constructed buildings")
else:
    print("No destruction of buildings")
