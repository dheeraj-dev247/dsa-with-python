def extraction_digit(num):
    while num > 0:
        last_digit = num%10
        print(last_digit,end="")
        num = num//10

extraction_digit(54321)