import csv,time,shutil,os

if os.path.exists():
    shutil.copy("primes.csv","primes.csv.bkp")



# m = 2 #Default starting point for search
# primes = []
#For each number, this divides it by all numbers from 2 to sqrt(number)+1. If it's divisible by any of them, the number is rejected
def prime_test(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Iterates through every number between 2 and the maximum entry, passes it to prime_test, and if that returns true it adds it to the primes list
def generate_primes(m):
    number_primes_found = 0
    primes = []
    num = m + 1
    last_save = time.time()
    while True:
        if prime_test(num):
            number_primes_found += 1
            primes.append(num)
            #print(num)
            # Writing list every 10,000 primes in order to not lose progress. Need to figure out a way for it to pick up again, maybe through reading the file and setting the maximum value as the minimum?
            if time.time() - last_save > 600:
                print("Saving")
                write_list(primes)
                primes = []
                last_save = time.time()
                print("Found "+ str(number_primes_found)+" so far this run")
                '''
                with open('primes_under_'+ str(maximum_number) + '.csv', 'w') as myfile:
                    
                    wr = csv.writer(myfile)
                    for n in primes:
                        wr.writerow([int(n)])
                    '''
        num += 1

def write_list(working_list):
    with open('primes.csv', 'a') as myfile:
        wr = csv.writer(myfile)
        for n in working_list:
            wr.writerow([int(n)])


# Enter the number to search under, from 2 to that
# maximum_number = int(input('What is the number you would like to find primes under?'))
try:
    with open('primes.csv', 'r') as csvfile: #Opens file indicated by maximum
        max_value_found = 0
        reader = csv.reader(csvfile)
        for n in reader:
            n = int(n[0])
            if n > max_value_found:
                max_value_found = n
            #primes.append(int(n[0]))
        #m = primes[-1]
        # print("Starting from"+ str(primes[-1]))
        print("Starting from"+ str(max_value_found))
        generate_primes(max_value_found)
except:
    generate_primes(1) #If there is no such file found, call function as normal, minimum defaulted as 2

#primes = generate_primes(m,maximum_number)
#print(primes)
# print((str(len(primes))+" primes found."))
#
# write_list(primes)
'''
with open('primes_under_'+ str(maximum_number) + '.csv', 'w') as myfile:
    wr = csv.writer(myfile)
    for n in primes:
        wr.writerow([int(n)]) #Otherwise it writes it either all to the one row, and/or as a series of lists rather than integers
'''