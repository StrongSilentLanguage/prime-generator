import csv

primes = []

with open('primes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for n in reader:
        primes.append(int(n[0]))

primes.sort()
print(len(primes))

for n in range (0,len(primes) - 1):
    while primes[n] == primes[n+1]:
        print(primes[n])
        primes.remove(primes[n+1])
    #print("Checking "+ str(primes[n]))

with open('primes.csv', 'w') as myfile:
    wr = csv.writer(myfile)
    for n in primes:
        wr.writerow([int(n)])

print("Finished.")
