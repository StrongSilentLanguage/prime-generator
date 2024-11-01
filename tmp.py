# Reads primes.csv filee with dodgy data "2","3","4" etc. and writes it to neprimes.csv with correct formatting
import csv
with open('primes.csv', 'r') as f:
    data = f.read()
    cd = data.split(',')

    with open('newprimes.csv', 'w') as nf:
        csvfile = csv.writer(nf)
        for n in cd:
            n = n.replace('"', "")
            csvfile.writerow([int(n)])