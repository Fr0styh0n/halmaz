
'''
    Halmaz (set):
    - rendezetlen (elemeknek nincs indexe)
    - egy elem csak egyszer szerepelhet
    - többféle típust tárolhat egyszerre is
    - a halmaz eleme maga nem változtatható meg
'''
    
    # halmaz létrehozása
reggeli = {'tea', 'vaj', 'piritós'}
    
    # üres halmaz létrehozása
    # ebed = {}  <- SZÓTÁRT hoz létre!!!
ebed = set()

    # bejárható gyűjteményből, pl. listából
ebed = set(['halászlé', 'kenyér', True])  
  
  
    # egy elem hozzáadása
reggeli.add('lekvár')

    # egy nem meghatározott elem eltávolítása
reggeli.pop()
    
    # egy bizonyos elem eltávolítása
    # ha nincs ilyen elem, akkor hibát eredményez
reggeli.remove('sajt')

    # egy bizonyos elem eltávolítása
    # ha nincs ilyen elem, nem eredményez hibát
reggeli.discard('sajt')



reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
ebed = {'víz', 'halászlé', 'kenyér'}

    # metszet
print(reggeli & ebed)
    # unio
print(reggeli | ebed)
    # különbség
print(reggeli - ebed)
    # csak az egyikben, vagy csak a másikban
print(reggeli ^ ebed)

# video kiirása
diak =['Kiss','Péter','10.A', 17, True, False]
print(diak[3])

diak = {
	      'vezeteknev': 'Kiss',
	      'keresztnev': 'Péter',
          'osztaly' :'10.A',
	      'eletkor': 17,
	      'menza': True,
          'info_fakt' : False,
          'matek_jegyek': [5,4,4,3,5,5]
    }
print(diak['eletkor'])

raktar = {
    114589: 'Dominó polc',
    264875: 'Student íróasztal',
    364879: 'Kényelem01 fotel',
    568974: 'Family étkezőasztal 6 fös',
}
print(raktar)


# szótár

    # üres szótár létrehozása
raktar = {}
print(raktar)

    # szótár létrehozása adatokkal 
diak = {
          'vezeteknev': 'Kiss',
	      'keresztnev': 'Péter',
          'osztaly' :'10.A',
	      'eletkor': 17,
	      'menza': True,
}
print(diak['eletkor'])
print(diak.get('eletkor', 'nincs adat'))
print('szakkor' in diak)
diak['szakkor'] = True
print(diak)
diak['eletkor'] = 20
print(diak)
del diak['vezeteknev']
print(diak)
for kulcs in diak:
	print(kulcs, diak[kulcs])

for ertek in diak.values():
    print(ertek)

print(diak.items())
for kulcs, ertek in diak.items():
    print(kulcs, ertek)
    
    # szótár elemeinek elérése kulcs alapján
print(diak['eletkor'])
print(diak.get('eletkor'))

    # nem létező kulcsra való hivatkozás -> KeyError
    # print(diak['osztaly'])

    # nem létező kulcsra hivatkozunk a .get metódussal, 
    # ilyenkor a megadott alapértékkel tér vissza
print(diak.get('kollegista', 'nem'))

    # ellenőrzés, hogy létezik-e a kulcs
print('keresztnev' in diak)
  

    # érték módosítása
diak['eletkor'] = 21
print(diak['eletkor'])

    # még nem létező kulcs megadása értékkel
diak['osztaly'] = '10.A'

    # kulcs-érték törlése
del diak['vezeteknev']



for kulcs in diak:
	print(kulcs, diak[kulcs])

for ertek in diak.values():
    print(ertek)

for kulcs, ertek in diak.items():
    print(kulcs, ertek)
    