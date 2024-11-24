

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes_ = []
not_primes = []




for num in range(2,len(numbers )+1):
    is_prime_ = True
    if num > 1:
            for i in range(2, num):
                is_prime_ = False
                if (num % i) == 0:
                    not_primes.append(num)
                    break
            else:primes_.append (num)
print (list(primes_))
print(list(not_primes))

