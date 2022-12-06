reggeli = {'vaj', 'tea' ,'piritos'}



ebed =set()
ebed =set(['halászlé', 'kenyér', True, True])


print(type(ebed))
print(ebed)

reggeli.add('víz')
# reggeli.remove('körte')
reggeli.discard('körte')


print(reggeli)


Reggeli = {'víz','vaj', 'tea' ,'piritos'}
ebéd = {'halászlé', 'kenyér', 'víz'}

print(Reggeli & ebéd)
print(Reggeli | ebéd)
print(Reggeli - ebéd)
print(Reggeli ^ ebéd)


gyumolcskosar = ['eper','alma','szilva','eper']
fajta = set()
for gyumolcs in gyumolcskosar:
    fajta.add(gyumolcs)
print(fajta)