# printing not repeting element

li = [1, 3, 1, 3, 4, 5, 6, 7, 8, 1, 5, 3]

elst = []
for i in li:
    if li.count(i) == 1:
        #        if i not in elst:
        elst.append(i)
print(elst)

#[4, 6, 7, 8]
