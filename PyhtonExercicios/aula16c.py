#O + une as tuplas númericas em uma só, a ordem terá total influência.
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c)
print(c.index(8))
print(c.count(2))
print(d)
print(d.index(5, 1))
print(len(d))