import csv

primes = []
def load_csv_into_list(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            primes.append(row)
    return primes

# Example usage:
file_path = 'primes.csv'  # Replace with your actual CSV file path
csv_data = load_csv_into_list(file_path)

print(primes)
