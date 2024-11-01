import csv

primes = []

maximum_number = int(input('What is the number you would like to find primes under?'))

try:
    with open('primes_under_'+ str(maximum_number) + '.csv', 'r') as csvfile: #Opens file indicated by maximum
        reader = csv.reader(csvfile)
        for n in reader:
            primes.append(int(n[0]))
        m = primes[-1]
        print("Starting from"+ str(primes[-1]))
        csvfile.close()
        generate_primes(m, maximum_number)
except:
    primes = generate_primes(m,maximum_number) #If there is no such file found, call function as normal, minimum defaulted as 2

print(primes)

