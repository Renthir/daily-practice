import math
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
        
def daily():
    print("daily practice would be nice if I knew what I was doing. I knew so much and now I feel like I know almost nothing. At least I can still commit and push to the repo...")


def mystery():
    results = {'sanity': 'Hello'}
    return results

def check_alive(health):
    if(health <= 0):
        return False
    else:
        return True
    
#it was the test problem, i imagine they live somehwere where that's legal
def people_with_age_drink(age):
    drink = ''
    if age < 14:
        drink = 'drink toddy'
    elif age < 18:
        drink = 'drink coke'
    elif age < 21: 
        drink = 'drink beer'
    else: 
        drink = 'drink whisky'
    return drink    

print("Hello, world!")
print("I'm just quickly doing this again to get the certif")


def get_expected_cost1(beds, baths):
    value = 80000 + (beds * 30000) + (baths * 10000)
    return value

def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    cost = (total_sqft / sqft_per_gallon) * cost_per_gallon
    return cost

def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    paint_needed = math.ceil(total_sqft / sqft_per_gallon)
    cost = paint_needed * cost_per_gallon
    return cost

def get_expected_cost(beds, baths, has_basement):
    price_beds = beds * 30000
    price_baths = baths * 10000
    value = 80000 + price_beds + price_baths + (40000 * has_basement)
    return value

def cost_of_project1(engraving, solid_gold):
    cost = (50 + 7 * len(engraving)) * (not solid_gold) + (100 + 10 * len(engraving)) * solid_gold
    return cost

def get_grade(score):
    if score < 60:
        grade = "F"
    elif score < 70:
        grade = "D"
    elif score < 80:
        grade = "C"
    elif score < 90:
        grade = "B"
    else:
        grade = "A"

def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + (10 * len(engraving))
    else:
        cost = 50 + (7 * len(engraving))
    return cost

def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        price = 5
    elif num_gallons <= 22000:
        price = 6
    elif num_gallons <= 30000:
        price = 7
    else: 
        price = 10
    bill = price * (num_gallons / 1000)
    return bill

def get_phone_bill(gb):
    if gb <= 15:
        bill = 100
    else:
        extra = gb - 15
        bill = 100 + (100 * extra)
    return bill

def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    # TODO: Complete the function
    percentage_liked = sum(list_liked) / len(ratings)
    return percentage_liked

def percentage_growth(num_users, yrs_ago):
    growth = (num_users[-1] - num_users[-yrs_ago - 1])/num_users[-yrs_ago - 1]
    return growth

