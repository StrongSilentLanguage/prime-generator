import csv,random,time

primes = []
random1 = 0
random2 = 0
duration_list = []


with open('1_million_random_primes.csv', 'r') as csvfile: # Reads list of random prime list into a working list
    reader = csv.reader(csvfile)
    for n in reader:
        primes.append(int(n[0]))
    csvfile.close()

def gen_primes(primes): # Assigns primes and generates semi-prime for testing
    random1 = random.randint(0,len(primes))
    random2 = random.randint(0,len(primes))
    prime1 = int(primes[random1])
    prime2 = int(primes[random2])
    semi_prime = prime1 * prime2
    #print(prime1)
    #print(prime2)
    print(semi_prime)
    return semi_prime

def prime_break(semi_prime): # Factors the semi-prime
    for i in range(2, int(semi_prime ** 0.5) + 1):
         if semi_prime % i == 0:
            print("Found it!")
            #print(i)
            break

iterations = 50 # Sets number of times being iterated to get more accurate idea of factoring time

for b in range(1,iterations + 1): # Iterates semi-prime factoring
    start_time = time.time()
    prime_break(gen_primes(primes))
    duration = round(time.time() - start_time,2)
    print(duration)
    duration_list.append(duration)
    print(f"Rolling average: {(sum(duration_list)/len(duration_list)):,.2f}")
    #if b % 10 == 0:
        #print(duration_list)
    print("*******************")

print(duration_list)
average_duration = sum(duration_list)/len(duration_list)
print(average_duration)