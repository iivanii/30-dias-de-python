#Level 1

#1. Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

#2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

#3. Insert multiple IT companies at once to the set it_companies
it_companies.update,('Activision','Instagram')

#4. Remove one of the companies from the set it_companies
it_companies.remove('Apple')

#5. What is the difference between remove and discard
print('El método discard no crea una excepción cuando falta un elemento en el set')

#Level 2

#1. Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
AB=A.union(B)

#2. Find A intersection B. 
A.intersection(B)

#3. Is A subset of B
A.issubset(B)

#4. Are A and B disjoint sets
A.isdisjoint(B)

#5. Join A with B and B with A
joinAB=A.update(B)
joinBA=B.update(A)

#6. What is the symmetric difference between A and B
print('La diferencia simétrica de A y B es el conjunto que contiene todos los elementos de A y de B, salvo a a aquellos que pertenecen a ambos')

#7. Delete the sets completely
del A
del B

