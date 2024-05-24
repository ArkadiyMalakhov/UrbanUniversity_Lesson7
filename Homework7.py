print('------СЛОВАРИ------')

my_dict = {'Max':1956, 'Vova':1992, "Sahsa":1985, 'Petya':2005, 'Ostap':1911}
print('Исхсодный список:', my_dict)
print('Вечный ученик - Ostap:',my_dict['Ostap'])
print(my_dict.get('Kiril', "Kiril не числится в списке"))
a = my_dict.pop('Petya')
my_dict.update({'Kesha': 1979, 'Zhora': 1981})
print('Не выучил урок - Petya:', a)
print('Итоговый список: ',my_dict)

print('-----МНОЖЕСТВА-----')

my_set = {1, 2, 3, 4, 1, 1, 2, 4, 4, 5, 7, 2}
print(my_set)
my_set.add(11)
my_set.add(12)
my_set.add((8, 9, 'String'))
print(my_set)
my_set.discard((8, 9, 'String'))
print(my_set)