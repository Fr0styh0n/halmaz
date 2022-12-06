# 1. feladat
halmaz1 = {1,2,3,4,5,6,7}
halmaz1.remove(2)

# 2.feladat
halmaz2 = {}
halmaz2 = halmaz1.copy()
print(halmaz1)
print(halmaz2)

# 3.feladat & 4.feladat
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
x.difference_update(y) 

print(z)
print(x)

# 5.feladat & 6.feladat

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
x.intersection_update(y)

print(x)
print(z)

# 7.feladat
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)

# 8.feladat 

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)


# 9.feladat
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)
# 10.feladat
