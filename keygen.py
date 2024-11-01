import csv,random

primes = []

with open('primes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for n in reader:
        primes.append(int(n[0]))
        #print(int(n[0]))

print(primes[-1])

#print(primes)  # [[header1, header2, ...], [row1], [row2], ...]

random1 = random.randint(0,len(primes))
random2 = random.randint(0,len(primes))

factor1 = primes[random1]
factor2 = primes[random2]
product = int(factor1 * factor2)

print(product)
#print(str(factor1)+", "+ str(factor2))

for i in range(2, int(product ** 0.5) + 1):
    if product % i == 0:
        print("Factor 1: "+str(i))
        print("Factor 2: "+str(int(product / i)))
        #print(product)

