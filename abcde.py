a=9
b=5
c=3
d=8
e=6
print(a if a<b and a<c and a<d and a<e else b if b<c and b<d and b<e else c if c<d and c<e else d if d<e else e)
