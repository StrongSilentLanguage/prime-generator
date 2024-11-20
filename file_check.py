import csv, os.path, json, time, alive_progress

iteration = 0
starting_point = 0
last_report_time = time.time()
reporting_interval = 100000 #How often do you want the script to update you, in rows processed

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

#Gets length of file to be checked and assigns it to num_lines variable
with open('primes.csv', 'r') as file:
    reader = csv.reader(file)
    num_lines = sum(1 for _ in reader)
    file.close()

if os.path.exists("scan_start.json"): #Checks if scan_start file exists, created by past runnings
    with open("scan_start.json","r") as f:
        data2 = json.load(f)
        starting_point = data2["key"] #Sets starting point as key value in that file
        f.close()
else:
    starting_point = 0 #If the file doesn't exist, starts at first value in primes.csv

remaining_to_check = int(num_lines - starting_point)

with open('primes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for _ in range(starting_point): #Skips first number of rows to make scanning large files easier. Do need to note stop point in previous runs though
        next(reader)
    print(f"Starting at row: {starting_point:,d} of {num_lines:,d}")
    with alive_progress.alive_bar(remaining_to_check) as bar: #Progrss bar thingy
        for n in reader:
            iteration += 1
            if iteration % reporting_interval == 0: #Every reporting_interval rows, updates starting scan value and updates user on progress
                num = int(n[0])
                print(f"Testing {num:,d}") #Basically a progress meter
                print(f"Up to row: {reporting_interval + starting_point:,d} of {num_lines:,d}") #Progress update for user
                print(f"Time since last update {time.time()-last_report_time:,.2f} seconds")
                print(f"Checking {reporting_interval/int((time.time()-last_report_time)):,.2f} rows per second")
                print("******************************") #Makes it easier to separate out different output instances
                last_report_time = time.time()
                if os.path.exists("scan_start.json"): #Updates json for future scans so it doesn't scan the same part over and over
                        starting_point = data2["key"] + reporting_interval
                        data2.update({"key": starting_point})
                        out_file = open("scan_start.json", "w")
                        json.dump(data2, out_file)
                        out_file.close()
                else:
                    out_file = open("scan_start.json", "w") #If no scan_start file found/this is the first run, creates it
                    data = {"key": iteration}
                    json.dump(data, out_file)
                    out_file.close()
            if prime_test(int(n[0])) is False: #In case there's a composite found, alert the user
                print(str(num)+ " is composite.")

            bar() #Adds progress bar down the bottom

print("Finished.")