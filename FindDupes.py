def ReturnDupe(lists):
    dupe=[]
    sets=set()
    for item in lists:
        first=len(sets)
        sets.add(item)
        second=len(sets)
        if first==second:
            dupe.append(item)
    return dupe
lists=['Agito', 'Ryuki', 'Faiz', 'Ryuki']
dupe=ReturnDupe(lists)
print(dupe)
