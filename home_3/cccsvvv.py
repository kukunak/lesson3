
#Создайте список словарей:
        #[
        #{'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        #{'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        #{'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    #]
#Запишите содержимое списка словарей в файл в формате csv
import csv

users = [
    {'name': 'Маша', 'age': '25', 'job': 'Scientist'},
    {'name': 'Васек', 'age': '1', 'job': 'Pioner'},
    {'name': 'Виталя', 'age': '167', 'job': 'Vampire'}
]
with open('persons.csv', 'w', encoding = 'utf-8', newline = '') as vrotmnenogi:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(vrotmnenogi, fields, delimiter = ';')
    writer.writeheader()
    for user in users:
        writer.writerow(user)