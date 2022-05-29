#P1
nameDictionary = {
    'firstName':'Raveendra',
    'lastName' : 'Bhat'
}
print(nameDictionary)
print(type(nameDictionary))
print(nameDictionary['firstName'])

#P2
carDict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
print(carDict.keys())
print(list(carDict.keys()))

#P3
phonebook = {
    'Andrew Parson': 8806336,
    'Emily Everett': 6784346,
    'Peter Power': 7658344,
    'Lewis Lame': 1122345
}
print(phonebook)
phonebook.pop('Peter Power')
print(phonebook)

#P4
ageDictionary = {'Tim':18,'Charlie':12, 'Tiffany':22, 'Robert':25}
print(ageDictionary)
ageDictionary.clear()
print(ageDictionary)

#P5
baseballTeams = {
    'Colarado':'Rockies',
    'Boston':'Red Sox',
    'Minnesota':'Twins',
    'Milwaukee':'Brewers',
    'Seattle':'Mariners'
}
print(baseballTeams)
print(list(baseballTeams.values()))
