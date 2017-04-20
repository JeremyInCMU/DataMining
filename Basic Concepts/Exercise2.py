# Excercise 2
import math

# 1. Implement pearson algorithm: get correlation coefficient
def pearson(user1, user2):
    n = 0
    x_y = 0
    sum_x = 0
    sum_y = 0
    sum_x_square = 0
    sum_y_square = 0

    for key in user1.keys():

        if key in user2.keys():

            x_y += user1[key] * user2[key]
            sum_x += user1[key]
            sum_y += user2[key]
            sum_x_square += math.pow(user1[key], 2)
            sum_y_square += math.pow(user2[key], 2)
            n += 1

    try:
        dividend = (x_y - sum_x * sum_y / n)
        denom1 = math.pow(sum_x_square - math.pow(sum_x, 2) / n, 0.5)
        denom2 = math.pow(sum_y_square - math.pow(sum_y, 2) / n, 0.5)
        return dividend / (denom1 * denom2)
    except:
        return 0

# Test Functions

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0,
 "Norah Jones": 4.5, "Phoenix": 5.0,
 "Slightly Stoopid": 1.5,
 "The Strokes": 2.5, "Vampire Weekend": 2.0},

 "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5,
 "Deadmau5": 4.0, "Phoenix": 2.0,
 "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
 "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0,
 "Deadmau5": 1.0, "Norah Jones": 3.0,
 "Phoenix": 5, "Slightly Stoopid": 1.0},
 "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0,
 "Deadmau5": 4.5, "Phoenix": 3.0,
 "Slightly Stoopid": 4.5, "The Strokes": 4.0,
 "Vampire Weekend": 2.0},
 "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0,
 "Norah Jones": 4.0, "The Strokes": 4.0,
 "Vampire Weekend": 1.0},
 "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0,
 "Phoenix": 5.0, "Slightly Stoopid": 4.5,
 "The Strokes": 4.0, "Vampire Weekend": 4.0},
 "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0,
 "Norah Jones": 3.0, "Phoenix": 5.0,
 "Slightly Stoopid": 4.0, "The Strokes": 5.0},
 "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0,
 "Phoenix": 4.0, "Slightly Stoopid": 2.5,
 "The Strokes": 3.0}}

def test():
    print(pearson(users['Angelica'], users['Bill']))
    print(pearson(users['Angelica'], users['Hailey']))
    print(pearson(users['Angelica'], users['Jordyn']))





