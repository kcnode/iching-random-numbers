


import random

def generate_random_numbers():
    # Generate two sets of random numbers between 1 and 64
    set1 = random.sample(range(1, 65), 6)  # 6 unique numbers for the first set
    set2 = random.sample(range(1, 65), 6)  # 6 unique numbers for the second set
    return set1, set2

if __name__ == "__main__":
    numbers = generate_random_numbers()
    print("Set 1:", numbers[0])
    print("Set 2:", numbers[1])
