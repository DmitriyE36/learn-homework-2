"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

workers = [{'name':'Bob', 'age':'38', 'job':'junior'},
           {'name':'Nil', 'age':'33', 'job':'middle'},
           {'name':'Fil', 'age':'27', 'job':'senior'},
           {'name':'Bill', 'age':'23', 'job':'team_lead'},
]

def main():
    with open('workers_dict.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for worker in workers:
            writer.writerow(worker)

if __name__ == "__main__":
    main()
