def reverse_an_interger(n):
    rev_int = 0
    while n > 0:
        ld = n % 10
        print(ld)
        rev_int = (rev_int * 10) + ld
        n = int(n / 10)
    return rev_int


print(reverse_an_interger(1234))
