import csv,random

primes = []

with open('primes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for n in reader:
        primes.append(int(n[0]))

# Generates random factors from list of primes (the "private key"), then multiplies them together to generate a product (the "public key")
factor1 = primes[random.randint(0,len(primes))]
factor2 = primes[random.randint(0,len(primes))]
product = int(factor1 * factor2)

primes = [] #Empties list to save memory

print(f"Public key: {product:,d}")

for i in range(3, int(product ** 0.5) + 1,2):
    if product % i == 0:
        print(f"Factor 1: {i:,d}")
        print(f"Factor 2: {product / i:,.0f}")
        break

