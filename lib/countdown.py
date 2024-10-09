# your code goes here!
import time

def countdown(n):
    for i in range(n):
        print(f"{n - i} SECOND(S)!")
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(n):
    for i in range(n):
        print(f"{n - i} SECOND(S)!")
        time.sleep(1)
    print("HAPPY NEW YEAR!")