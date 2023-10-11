dico = {}
for i in range(29):
    if i**2%29 not in dico.keys():
        dico[i**2%29]=[i]
    else:
        dico[i**2%29].append(i)
for k in sorted(dico.keys()):
    print(k,dico[k])