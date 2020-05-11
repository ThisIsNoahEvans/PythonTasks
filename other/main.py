import random

countryName1 = ['Doth', 'Nask', 'Thout', 'Dome', 'Deha']
countryName2 = ['hax', 'ingar', 'ham', 'shire', 'ton']
playerRaces = ['humans', 'elves', 'martians', 'cats', 'pandas']
monsters = ['goblins', 'ogres', 'sharks', 'werewolves', 'cheetahs']
resources = ['wood', 'gold', 'iron', 'compost', 'stone']
magic = ['necromancy', 'conjuration', 'sorcery', 'divination', 'astrology']
government = ['a monarchy', 'a dictatorship', 'democratic', 'communism', 'a republic']

print('The name of your new country is', (random.choice(countryName1) + random.choice(countryName2)) + '. \n')
print('In this country, there are', (random.choice(playerRaces)) + '. \n')
print('However, there are three monsters. They are', (random.choice(monsters)) + ', ' + (random.choice(monsters))  + ', and ' + (random.choice(monsters)) + '. \n')
print('You have access to two resources:', (random.choice(resources)),'and', (random.choice(resources))+ '. \n')
print('There is a type magic here. It is called', (random.choice(magic)) + '. \n')
print('The government style here is', (random.choice(government)) + '.')
