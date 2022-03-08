def prime(x):
    if x<1:
        return []
    prime_numbers = [2,3]
    if x<3:
        return prime_number[:x]
    for i in range(2,x):
        next_pn = prime_numbers[-1]+2
        while any(not(next_pn%pn) for pn in prime_numbers):
            next_pn += 2
        prime_numbers.append(next_pn)
    return prime_numbers

N = 1000
print (prime(int(N)))


def areAnagrams(a,b):
    a = str(prime_numbers[0])
    b = str(prime_numbers+[1])
    if (sorted(a) == sorted(b)):
        return True
    else:
        return False
    if (areAnagrams(a, b)):
        print("Yes")
    else:
        print("No")
