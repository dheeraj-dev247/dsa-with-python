def extract_digit(n):
    while n > 0:
        last_digit = n % 10
        print(f"Last digit is : {last_digit}")
        n = int(n / 10)
    return "Completed"


print(extract_digit(345))
