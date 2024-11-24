import csv

primes = []
start_length = 0

with open('primes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for n in reader:
        primes.append(int(n[0]))
        start_length += 1

primes.sort()

print(f"Starting length: {start_length:,d}")

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
print(f"Ending length: {len(primes):,d}")
print(f"Removed: {(start_length - len(primes)):,.0f}")