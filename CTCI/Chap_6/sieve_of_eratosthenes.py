import math


def sieve(max_num):
    sieve_list = []
    for i in range(2, max_num + 1):
        sieve_list.append(i)

    prime = 2
    while prime <= int(math.sqrt(max_num)):
        if prime in sieve_list:
            for i in range(prime*prime, max_num + 1, prime):
                if i in sieve_list:
                    sieve_list.remove(i)
        prime += 1
    return sieve_list


if __name__ == "__main__":
    print(sieve(100))
