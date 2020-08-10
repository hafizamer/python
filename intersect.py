def intersect(number1, number2):
    Intersect=[n for n in number1 if n in number2]
    return Intersect

number1=[46,53,75,51,53,57]
number2=[51,65,94,765,75,15]

print(number1)
print(number2)
print(intersect(number1, number2))



def intersect_alt(number1, number2):
    set1=set(number1)
    set2=set(number2)
    return list(set1.intersection(set2))

lists=intersect_alt(number1, number2)

print(number1)
print(number2)
print(lists)

