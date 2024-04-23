# Brute force tool
# v0.1

import argparse
import time
import threading


parser = argparse.ArgumentParser(description="Brute Force Tool v0.1",epilog = "1 request per thread per second, max 12 threads, max 10,000 tries total")
# https://docs.python.org/3/library/argparse.html#module-argparse

parser.add_argument("-u", "--username", help="specify username to bruteforce", required=True)
parser.add_argument("-w", "--wordlist", help="set wordlist e.g. /usr/share/worslists/rockyou.txt", required=True)
parser.add_argument("-t", "--threads", help="set thread count (default = 1, max = 12)", type=int, default=1)
parser.add_argument("-p", "--password", help="the password hash to match to", required=True)


args = parser.parse_args()

#ensure threads are within range
if args.threads < 1:
    raise ValueError("Threads lower than 1")
if args.threads > 12:
    raise ValueError("Threads higher than 12")

#import wordlist and turn it into list of words
num_threads = args.threads
wordlist = open(args.wordlist).readlines
pw = args.password

if len(wordlist) < 10000:
    try_total = len(wordlist)
else:
    try_total = 10000

# brute force function
def brute_force(s, e, pw, wordlist):
    while try_total > 0:
        for word in wordlist[s:e]:
            if word == pw
                print(f"--Match Found--")
                print(f"The password for {args.username} is 'FOUNDPASS'")
            try_total -= 1
            time.sleep(1)

# split brute force function over given number of threads
def split_brute(pw, wordlist, num_threads):
    chunk_size = len(wordlist) // num_threads
    threads = []
    for i in range(num_threads):
        s = i * chunk_size
        e = (i + 1) * chunk_size if i < num_threads - 1 else len(wordlist)
        thread = threading.Thread(target=brute_force, args=(s, e, pw, wordlist))
        threads.append(thread)
        thread.start
    
    for thread in threads:
        thread.join()


def main():
    split_brute(pw,wordlist,num_threads)

main()
