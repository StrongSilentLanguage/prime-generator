import csv
import os.path
import json

iteration = 0
starting_point = 0

def prime_test(n):
    #print(n)
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n > 2 and n % 2 == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1): #This is a more thorough and computationally intenseive test than the original finder
        if n % i == 0:
            return False
    return True


if os.path.exists("scan_start.json"): #Checks if scan_start file exists, created by past runnings
    with open("scan_start.json","r") as f:
        data2 = json.load(f)
        starting_point = data2["key"] #Sets starting point as key value in that file
else:
    starting_point = 0 #If the file doesn't exist, starts at first value in primes.csv

with open('primes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for _ in range(starting_point): #Skips first number of rows to make scanning large files easier. Do need to note stop point in previous runs though
        next(reader)
    print(f"Starting at row: {starting_point:,d}")
    for n in reader:
        iteration += 1
        if iteration % 1000000 == 0: #Every million rows, updates starting scan value and updates user on progress
            num = int(n[0])
            print(f"Testing {num:,d}") #Basically a progress meter
            print(f"Up to row: {1000000 + starting_point:,d}") #Progress update for user
            if os.path.exists("scan_start.json"): #Updates json for future scans so it doesn't scan the same part over and over
                    starting_point = data2["key"] + 1000000
                    data2.update({"key": starting_point})
                    out_file = open("scan_start.json", "w")
                    json.dump(data2, out_file)
                    out_file.close()
            else:
                out_file = open("scan_start.json", "w") #If no scan_start file found/this is the first run, creates it
                data = {"key": iteration}
                json.dump(data, out_file)
        if prime_test(int(n[0])) is False: #In case there's a composite found, alert the user
            print(str(num)+ " is composite.")

print("Finished.")