import time
import random


def marriage(name):
    r = random.randint(0, 10)
    time.sleep(r)
    print(f"{name} after {r} years")



def main():
    for child in ["ch1" , "ch2", "ch3" , "ch4"]:
        marriage(child)

if __name__  == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in {total_time} seconds")