#first commit

#just remembering if I can do this right

c = 5

print(1 + c)

def even_or_odd(number):
    if number % 2 ==  0:
        return "Even"
    else:
        return "Odd"
    

def find_smallest_int(arr):
    small = arr[0]
    for num in arr:
        if num < small:
            small = num
    return small


def is_even(n): 
    return True if n % 2 == 0 else False 


def remove_char(s):
    new_s = s[1:-1]
    return new_s


def stringy(size):
    num = 1
    string = ""
    while num <= size:
        if num % 2 != 0:
            string += "1"
        else:
            string += "0"
        num += 1
            
    return string
        