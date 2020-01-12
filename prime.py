def nth_prime_number(n):
    prime_list = [2]
    num = 3
    while len(prime_list)<n:
        for p in prime_list:
            if num % p ==0:
                break
        else:
            prime_list.append(num)
        num += 2
    return prime_list[-1]


def find_prime_number_number(n):
    prime_list = [2]
    num = 3
    while n not in prime_list:
        for p in prime_list:
            if num % p == 0:
                break
        else:
            prime_list.append(num)
        num += 2
    return len(prime_list)


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
