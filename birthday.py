import random
import hashlib


def hash_function(key):
    return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16) & 0xffffffff


def how_many_before_collision(buckets, loops=1):
    for i in range(loops):
        tries = 0
        tried = {}

        # while True:
        #     random_key = random.random()
        #     index = hash_function(random_key) % buckets
        #     if index not in tried:
        #         tried.add(index)
        #         tries += 1
        #     else:
        #         break

        while True:
            random_key = random.random()
            index = hash_function(random_key) % buckets

            if index not in tried:
                tried[index] = 0

            tried[index] += 1
            tries += 1

            if tried[index] == 2:
                break

        print(
            f"{buckets} buckets, {tries} hashes before 2 collisions. ({tries / buckets * 100:.1f}% full)")


how_many_before_collision(65536, 10)
