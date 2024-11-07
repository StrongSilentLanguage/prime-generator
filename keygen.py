import csv,random

primes = []

with open('primes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for n in reader:
        primes.append(int(n[0]))
        #print(int(n[0]))

print(primes[-1])

# Generates random factors from list of primes (the "private key), then multiplies them together to generate a product (the "public key")
factor1 = primes[random.randint(0,len(primes))]
factor2 = primes[random.randint(0,len(primes))]
product = int(factor1 * factor2)

print("Product: "+ str(product))

for i in range(2, int(product ** 0.5) + 1):
    if product % i == 0:
        print("Factor 1: "+str(i))
        print("Factor 2: "+str(int(product / i)))
        #print(product)

