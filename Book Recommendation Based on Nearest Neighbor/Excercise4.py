# This exercise for one-slop collaborative filter algorithm.
# dev = {} Deviation between different items (item1, item2) : dev
# u = {} User rating for different items user : (item, rating)

class Recommeder():

    def __init__(self):

        self.Users = dict()
        self.items = list()


    def loadDataSet(self, path):

        if (type(path).__name__ == 'dict'):

                self.Users = path

    #     f = codecs.open(path, 'r', 'utf8')

    #     for line in f:

    #     r = 


    #########  Implement Algorithm ##############
    # Do recommendations
    def doRecommendation(self, tarUser, numOfRecommend):

        recommendations = list(self.oneSlop(tarUser).items())
        recommendations = [(k, v) for (k, v) in recommendations]
        recommendations.sort(key = lambda artistTuple: artistTuple[1],
                             reverse = True)

        if (numOfRecommend > len(recommendations)):

            return recommendations

        return recommendations[numOfRecommend]

    # Main method: estimate rating based on one slop weight
    def oneSlop(self, tarUser):

        recommendations = {}

        dev = self.calDev()

        for item in self.items:

            if (item not in self.Users[tarUser]):

                count = 0
                tempRating = 0.0

                # Potential recommended items
                for (tarItem, assisItem) in dev.keys():

                    if tarItem == item and assisItem in self.Users[tarUser]:

                        tempAdd = dev[(tarItem, assisItem)][0] + self.Users[tarUser][assisItem]
                        tempRating += tempAdd * dev[(tarItem, assisItem)][1]

                        count += dev[(tarItem, assisItem)][1]

                if (item not in recommendations):

                    recommendations[item] = tempRating / float(count);

        return recommendations

    # Get the form of deviation among different items.
    def calDev(self):

        result = {}

        # Extract all available items from the input data structuer.
        for user in self.Users.keys():

            for item in self.Users[user].keys():

                if (item not in self.items):

                    self.items.append(item)

        # Calcualte deviation between any two items.
        dev = 0.0

        for item1 in self.items:

            for item2 in self.items:

                if (item1, item2) not in result.keys():

                    result[(item1, item2)] = self.calSingleDev(item1, item2)

        return result

    # Calcualte deviation between two items.
    def calSingleDev(self, item1, item2):

        tempResult = list();

        # Get item1 ratings and item2 ratings rated by all users.
        for value in self.Users.values():

            if (item1 in value.keys() and item2 in value.keys()):

                tempResult.append(value[item1] - value[item2])

        return (sum(tempResult) / float(len(tempResult)), len(tempResult))


# Test the one slope recommender class
def testOneSlopeRecommendation():

    users2 = {"Amy": {"Taylor Swift": 4, "PSY": 3, "Whitney Houston": 4},
    "Ben": {"Taylor Swift": 5, "PSY": 2},
    "Clara": {"PSY": 3.5, "Whitney Houston": 4},
    "Daisy": {"Taylor Swift": 5, "Whitney Houston": 3}}

    recommender =  Recommeder()
    recommender.loadDataSet(users2)
    print(recommender.doRecommendation("Ben", 2))

testOneSlopeRecommendation()
