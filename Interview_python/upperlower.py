# i have an string in this way PrintCapsFirst
# but we need to get o/p like  this PrintCapsFirst

st = 'PrintCapsFirst'

pot = ''
pots = ''
for item in st:
    if item.isupper():
        pot = pot + item
    elif item.islower():
        pots = pots + item
print(pot+pots)
# PCFrintapsirst
