import csv

previous = None
start_length = 0
duplicates = 0
ordering_errors = 0

with open('primes.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        n = int(row[0])
        start_length += 1

        if previous is not None:
            if n == previous:
                duplicates += 1
                print(f"Duplicate found: {n}")

            elif n < previous:
                ordering_errors += 1
                print(
                    f"Ordering error: {n} follows {previous}"
                )

        previous = n

print("\nVerification complete.")
print(f"Numbers checked: {start_length:,}")
print(f"Duplicates found: {duplicates:,}")
print(f"Ordering errors: {ordering_errors:,}")

if duplicates == 0 and ordering_errors == 0:
    print("SUCCESS: No duplicates or ordering errors found.")
else:
    print("WARNING: Potential problems detected.")
