import csv,time,shutil,os
from collections import deque

print(f"Starting at {time.ctime()}")
interval = 600

#For each number, this divides it by all numbers from 2 to sqrt(number)+1. If it's divisible by any of them, the number is rejected
def prime_test(n):
    if n <= 1:
        return False
    if n == 2 or n == 3 or n == 5:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0: #Checks if divisible by 2,3, or 5 - should eliminate ~3/4 of all candidates for speed. Going past 5 gets into diminishing returns to the point it becoems more computationally intensive than it saves
        return False
    for i in range(7, int(n ** 0.5) + 1,2):
        if n % i == 0:
            return False
    return True

#Iterates from either 2 or the last value in primes.csv, passing each value to prime_test. If prime_test is true, adds the prime to the primes list
def generate_primes(m):
    number_primes_found = 0
    primes = []
    num = m + 1
    last_save = time.time()
    while True:
        if prime_test(num):
            number_primes_found += 1
            primes.append(num)
            #print(num) #Commented out because it is so voluminous, but it is fun to see so I've left it here. Just uncomment it if you want to see the numbers fly by
            # Writing list every 10 minutes in order to not lose progress, then empties list to prevent memory filling up
            if time.time() - last_save > interval:
                print("Saving")
                write_list(primes)
                print(f"Found {len(primes)/interval:,.2f} numbers per second")
                primes = []
                last_save = time.time()
                print(f"Found {number_primes_found:,d} so far this run")
                print("***************************")
        num += 1

#Writes prime list to primes.csv
def write_list(working_list):
    with open('primes.csv', 'a') as myfile:
        wr = csv.writer(myfile)
        for n in working_list:
            wr.writerow([int(n)])
    myfile.close()
    filename = 'primes.csv'
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        num_lines = sum(1 for _ in reader)
        csvfile.close()
    print(f"Total length of primes.csv: {num_lines:,d}")
    max_value_list = tail_seek("primes.csv", 1)
    max_value_found = int(max_value_list[0])
    print(f"Highest prime found: {max_value_found:,d}")

#Pulls out last value from primes.csv in a memory-efficient way. Stole this code, so I don't understand it very well
from collections import deque

def tail_seek(filename, num_lines):
    with open(filename, 'r') as f:
        return list(deque(f, num_lines))


# Checks if primes.csv exists, then either takes the last value as the starting value for generate_primes, or passes 1 (becomes 2) as the starting value
if os.path.exists("primes.csv"):
    shutil.copy("primes.csv", "primes.csv.bkp") #Creates backup of existing primes.csv to prevent losing progress from error
    max_value_list = tail_seek("primes.csv", 1)
    max_value_found = int(max_value_list[0]) #turns the last prime in primes.csv into an integer rather than a list item
    print(f"Starting from {max_value_found:,d}")
    generate_primes(max_value_found) #Starts the prime-generation process, passing the last value in primes.csv as the starting value
else:
    print("Starting new list")
    generate_primes(1) #If there is no such file found, call function as normal, passing 1 (becomes 2)

