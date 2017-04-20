# 1. Minkowski function
import math

def minkowskiDistance(rating1, rating2, p = 2.0):

    dist = 0

    for key in rating1.keys():

        if (key in rating2.keys()):

            dist += abs(rating1[key] - rating2[key]) ** p

    return math.pow(dist, 1 / p)

# 2. Compute nearest neighbour

def computeNearstNeighbor(username, users, fn):

    distances = []

    for user in users:
        if user != username:
            distance = fn(users[user], users[username])
            distances.append((user, distance))

    if fn.__name__ == "pearson":

        distances.sort(key = lambda artistTuple: artistTuple[1],
                       reverse = True)
    
    else:

        distances.sort(key = lambda artistTuple: artistTuple[1],
                       reverse = False)
    return distances


