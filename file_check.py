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


if os.path.exists("scan_start.json"):
    with open("scan_start.json","r") as f:
        data2 = json.load(f)
        #print(data2["key"])
        starting_point = data2["key"]
else:
    starting_point = 0

with open('primes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for _ in range(starting_point): #Skips first number of rows to make scanning large files easier. Do need to note stop point in previous runs though
        next(reader)
    print(f"Starting at row: {starting_point:,d}")
    for n in reader:
        iteration += 1
        if iteration % 1000000 == 0:
            num = int(n[0])
            print(f"Testing {num:,d}") #Basically a progress meter
            print(f"Up to row: {iteration + starting_point:,d}") #Gives periodic update on row number for later re-starts
            if os.path.exists("scan_start.json"):
                    starting_point = data2["key"] + iteration
                    data2.update({"key": starting_point})
                    out_file = open("scan_start.json", "w")
                    json.dump(data2, out_file)
                    out_file.close()
            else:
                out_file = open("scan_start.json", "w")
                data = {"key": iteration}
                json.dump(data, out_file)
        if prime_test(int(n[0])) is False: #In case there's a composite found, alert the user
            print(str(num)+ " is composite.")