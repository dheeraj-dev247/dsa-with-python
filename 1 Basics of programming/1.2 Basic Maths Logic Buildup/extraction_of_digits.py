def extraction_digit(num):
    while num > 0:
        last_digit = num%10
        print(f"Last Digit is {last_digit}")
        num = num//10

extraction_digit(154)