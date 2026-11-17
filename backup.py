import hashlib, shutil, os, csv
from pathlib import Path

main_file = Path("primes.csv")
backup_file = Path("primes.csv.bkp")


def calculate_hash(filepath, chunk_size=16 * 1024 * 1024):
    """Calculate SHA-256 hash using 16 MB chunks."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(chunk_size):
            sha256.update(chunk)
    return sha256.hexdigest()


if main_file.exists():
    print("Main file found")
    print(f"{os.path.getsize(main_file)/1048576:,.1f} MB")
    if os.path.getsize(main_file) == 0:
        print("primes.csv exists but has zero size. Stopping")
        exit()
    else:
        main_file_hash = calculate_hash(main_file)
        print(main_file_hash)
else:
    print("primes.csv not found. Stopping program")
    exit()

if backup_file.exists():
    print("Backup found")
    print(f"{os.path.getsize(backup_file) / 1048576:,.1f} MB")
    if os.path.getsize(backup_file) == os.path.getsize(main_file):
        print("Files same size")
        # Now check hashes to see if they're identical or not
        backup_file_hash = calculate_hash(backup_file)
        print(backup_file_hash)
        if main_file_hash == backup_file_hash:
            print("Files match")
            exit()
        else:
            print("Files not identical")
            print("Backing up. Please wait.")
            shutil.copy("primes.csv", "primes.csv.bkp")  # Creates backup of existing primes.csv to prevent losing progress from error
    else:
        print("Files not same size")
        if os.path.getsize(backup_file) > os.path.getsize(main_file):
            print("Backup file bigger than primes.csv. Stopping - investigate primes.csv")
            exit()
        # call copy function since they can't be identical
        print("Backing up. Please wait.")
        shutil.copy("primes.csv", "primes.csv.bkp")  # Creates backup of existing primes.csv to prevent losing progress from error
        print("Files copied")
else:
    print("Backup not found. Making backup")
    shutil.copy("primes.csv", "primes.csv.bkp")  # Creates backup of existing primes.csv to prevent losing progress from error

if main_file_hash == calculate_hash(backup_file):
    print("File successfully backed up")
else:
    print("Something went wrong, check")

if main_file.exists():
    with open('primes.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        num_lines = sum(1 for _ in reader)
        csvfile.close()
    print(f"Total length of primes.csv: {num_lines:,d}")


# print("Checking")
# if os.path.exists("primes.csv"):
#     shutil.copy("primes.csv", "primes.csv.bkp")
#     print("Copied")
# else:
#     print("No primes.csv found.")
