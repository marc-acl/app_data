import csv

with open('ausflistung.csv', 'r', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    
    for row in spamreader:
        print('\n'.join(row))
        print("")