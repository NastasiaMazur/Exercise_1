
#1
def name_age():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello {name}. Your age is: {age}")
    result = name + age
    print("The returned string will be:", result)
    return result

name_age()


#2
def swap_integers(num1, num2):g
    print(f"X={num1}")
    print(f"Y={num2}")

    # Swap with temporary variable (num 3)
    num3 = num1
    num1 = num2
    num2 = num3

    print("After swap:")
    print(f"X={num1}")
    print(f"Y={num2}")

    swapped_nums = str(num1) + str(num2)
    print("Return value:", swapped_nums)
    return swapped_nums

swap_integers(10, 20)


#3
def check_numbers(num1, num2):
    if num1 % 6 == 0 or num2 % 6 == 0:
        print("One number is divisible by 6")
    else:
        print("Neither number is divisible by 6 or both are divisible by 6")

    if num1 % 10 == 0 and num2 % 10 == 0:
        print("Both numbers are divisible by 10")
        result = True
    else:
        print("Both numbers are not divisible by 10")
        result = False

    print("Return value:", result)
    return result

check_numbers(6,10)

#4
def sum_up(num1, num2):
    if num2 <= num1 or num1 < 0 or num2 < 0:
        return 0

    else:
        return sum(range(num1, num2))


print(sum_up(3, 9))


#5
def circle_area(r1, r2, r3):
    pi = 3.141
    area1 = pi * r1 ** 2
    area2 = pi * r2 ** 2
    area3 = pi * r3 ** 2

    total_area = area1 + area2 + area3
    return float(total_area)


print(circle_area(1, 2, 3))


#6
def check_string(text):
    if text.lower().startswith('a') or text.lower().endswith('a'):
        print("Your text starts OR ends with an a")
        #return true
    else:
        print("Your text starts AND ends with an a, or Your text DOESN'T begin and end with a")
        #return false

print(check_string("apple"))


#7
def triangle(rows):
    for i in range(1, rows + 1):
        print("* " * i)

triangle(4)

#