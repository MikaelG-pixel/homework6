my_dict = {'Satir': 1111, 'Dan': 2222, 'Mor': 3333}
print(my_dict)
print(my_dict['Satir'])
print(my_dict.get('Gal'))
my_dict.update({'Fal': 8516, 'Maxim': 1234})
print(my_dict.pop('Dan'))
print(my_dict)

my_set = {1, 1, 1, 2, 'Maz', 47, 95}
print(my_set)
my_set.update([4,'frg'])
my_set.remove(1)
print(my_set)