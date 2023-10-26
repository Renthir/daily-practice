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

#exercise

def numbers_even ():
    for n  in range(2, 10, 2):
        print(n)

    print("We have 4 even numbers")


#or

def numbers_even2 (min, max):
    count = 0 
    for num in range(min, max):
        if num % 2 == 0:
            count += 1
            print(num)
    print(f"We have {count} even numbers")


# numbers_even2(1, 10)


pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius = diameter / 2

# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area = pi * (radius ** 2)

# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
to_smash = (alice_candies + bob_candies + carol_candies) % 3

def practice(done_today):
    if not done_today:
        must_complete = True
    else:
        must_complete = False
    return must_complete

def whats_the_point(point):
    if point:
        print('Finally, I have it!')
    else:
        print("There isn't one, is there? We're just all fleshbags trying to find meaning where there is none. Writing silly lines so our complex rocks can read them back to us in interesting ways.")
        return "There's no point"


def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    return round(num, 2)

print(round(5.3980, -1))
print(round(40.3980, -2))
print(round(302.3980, -3))

def to_smash(total_candies, num_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % num_friends

x = -10
y = 5
# # Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x), abs(y))

#I'm back, ready to code again

def to_smash2(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    grammar = ""
    if total_candies == 1:
        grammar = "candy"
    else:
        grammar = "candies"

    print("Splitting", total_candies, grammar)
    return total_candies % 3

# to_smash2(91)
# to_smash2(1)

def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0
    
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return True if number < 0 else False

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion

def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (mustard and not ketchup) 

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    sum_of = int(ketchup) + int(mustard) + int(onion)
    return True if sum_of == 1 else False

def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) < 2:
        return None
    return L[1] 


def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]

def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    first = racers.pop(0)
    last = racers.pop(-1)
    racers.append(first)
    racers.insert(0, last)
    
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3, 2, 0, 2]

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    index_n = arrivals.index(name)
    if index_n >= (len(arrivals) / 2):
        if index_n != len(arrivals) - 1:
            return True
        else:
            return False
    else:
        return False
    
# list1 = []
# list1.upper()

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    return False

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [num > thresh for num in L]

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range( len(meals)-1 )
        if meals[i] == meals[i+1]
            return True
    return False

def estimate_average_slot_payout(n_runs):
    # Play slot machine n_runs times, calculate payout of each
    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    # Calculate the average value
    avg_payout = sum(payouts) / n_runs
    return avg_payout

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    if len(zip_code) == 5:
        if zip_code.isdigit():
            return True
    return False

