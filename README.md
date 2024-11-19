The core of this suite is primes.py, that's the script that churns through, finds the primes, and adds them to primes.csv if it exists (and creates it if it doesn't). It also makes a backup of primes.csv in case primes.py somehow messes it up or it somehow got corrupted. It's in the same folder so it's not a _good_ backup, but I can't do your job for you

file_check.py is what it sounds like, it applies a slower but more thorough check to primes.csv to find any composites that have somehow snuck in. There _shouldn't_ be any in there, but who knows, and also you could use it for any list of numbers as long as you name it primes.csv

keygen.py is a bit pointless, it kind of mimics how hard/easy it is to factor numbers, presumably it should get slower as primes.csv gets longer. Work in progress

duplicate_removal.py is another error-correction script, just sorts the list and removes duplicate values
