def sum_three_num(a, b, c):
    return a + b + c


oo = lambda a, b, c: a + b + c
print(oo(3, 4, 3))


def find_odd_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

# find_odd_even(5)

check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(11))