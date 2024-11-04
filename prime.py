import csv,time,shutil,os

#Creates backup of existing primes.csv to prevent losing progress from error
if os.path.exists("primes.csv"):
    shutil.copy("primes.csv","primes.csv.bkp")

#For each number, this divides it by all numbers from 2 to sqrt(number)+1. If it's divisible by any of them, the number is rejected
def prime_test(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if i > 2 and i % 2 == 0: #For even factors larger than 2, skip checking because if not eliminated by checking 2 it won't be divisble by 2k
            continue
        if i > 3 and i % 3 == 0: #Similar to 2 above, seiving for 3-divisible factors > 3
            continue
        if i > 5 and i % 5 == 0: #Similar to 2 and 3 above, seiving for 5-divisible factors > 5
            continue
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
            print(num) #Commented out because it is so voluminous, but it is fun to see so I've left it here. Just uncomment it if you want to see the numbers fly by
            # Writing list every 10 minutes in order to not lose progress, then empties list to prevent memory filling up
            if time.time() - last_save > 600:
                print("Saving")
                write_list(primes)
                primes = []
                last_save = time.time()
                print("Found "+ str(number_primes_found)+" so far this run")
        num += 1

#Writes prime list to primes.csv
def write_list(working_list):
    with open('primes.csv', 'a') as myfile:
        wr = csv.writer(myfile)
        for n in working_list:
            wr.writerow([int(n)])

#Checks if primes.csv exists, then either takes the last value as the starting value for generate_primes, or passes 1 (becomes 2) as the starting value
try:
    with open('primes.csv', 'r') as csvfile:
        max_value_found = 0
        reader = csv.reader(csvfile)
        for n in reader:
            n = int(n[0])
            if n > max_value_found:
                max_value_found = n
            #primes.append(int(n[0]))
        #m = primes[-1]
        # print("Starting from"+ str(primes[-1]))
        print("Starting from "+ str(max_value_found))
        generate_primes(max_value_found)
except:
    generate_primes(1) #If there is no such file found, call function as normal, passing 1 (becomes 2)
