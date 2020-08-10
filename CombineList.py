movies=["Data","Vaccine","Virus","Neutral"]

power=[2,4,3,5]

rating=[]

for combine in zip(movies, power):
    rating.append(combine)

print(rating)
