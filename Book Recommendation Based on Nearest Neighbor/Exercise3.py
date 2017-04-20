# Excersise 3
import Exercise1
import Exercise2
import codecs
# Book Recommendation System

# 1. BX-Book-Ratings:
        
        # User ID: Book ID: Ratings;

# 2. BX-Books:
        
        # BookID: Book Name: Auhtor: Publish: Url;

# 3. BX-Users:
    
        # User ID: Location: Age;


# Data Structures Need:

    # {User ID: {bookID: rating}}
    # {bookID: (title, author)}
    # {User ID: (location, age)}


class recommender:

    def __init__(self, data = None, k = 1, metric = "pearson", n = 5):
        """
            data: the data sets used to calculate recommendation item (csv file)
            k: the k nearest neigbor
            metric: the way to calculate distance
            n: number of recommendation items.
        """

        self.k = k
        self.distType = metric
        self.n = n

        # Check which way to calculate distance.
        if (metric == "pearson"):
            self.fn = self.pearson
        elif (metric == "manhattan"):
            self.fn = self.manhattan
        elif (metric == "euclide"):
            self.fn = self.euclide

        # If input data is a dictionary, set it as deployed data
        if type(data).__name__ == 'dict':
            self.ratingData = data
        else:
            self.ratingData = {}

        self.bookData = {}
        self.userData = {}

    # Load data from csv file to generate data structure: {User ID: {bookID: rating}}

    def loadBookRatingData(self, path = ""):

        f = codecs.open(path, 'r', 'utf8')

        for line in f:

            fields = line.split(";")

            userID = fields[0].strip('"')
            bookID = fields[1].strip('"')
            rating = fields[2].strip().strip('"')

            if userID not in self.ratingData.keys():
                
                self.ratingData[userID] = dict()

            self.ratingData[userID][bookID] = rating

        f.close()

    # Load data from csv file to generate data structure: {bookID: (title, Author)}
    def loadBookData(self, path = ""):

        f = codecs.open(path, 'r', 'utf8')

        for line in f:

            fields = line.split(";")

            bookID = fields[0].strip()
            title = fields[1].strip('"')
            author = fields[2].strip('"')

            self.bookData[bookID] = (title, author)

        f.close()

    # Load data from csv file to generate data structure:     # {User ID: (location, age)}
    def loadUserData(self, path = ""):

        f = codecs.open(path, 'r', 'utf8')

        for line in f:

            fields = line.split(";")

            userID = fields[0].strip()
            location = (fields[1]).strip('"')
            age = ""

            if (len(fields) == 3):
                age = fields[2].strip().strip('"')


            self.userData[userID] = (location, age)

        f.close()

    # Calculate distance with pearson method
    def pearson(self, rating1, rating2):

        return Exercise2.pearson(rating1, rating2)


    # Calculate distance with manhanttan method
    def manhattan(self, rating1, rating2):

        return Exercise1.minkowskiDistance(rating1, rating2, 1)

    # Calculate distance with euclidian method
    def euclidian(self, rating1, rating2):

        return Exercise1.minkowskiDistance(rating1, rating2)

    # ComputeNearestNeighbor
    def computeNearestNeighbor(self, userName):

        return Exercise1.computeNearstNeighbor(userName, self.ratingData, self.fn)

    # Implement recommendation
    def recommend(self, userName):

        # Define a dictionary to contain recommendation results
        recommendations = {}

        # Distances for n nearest neighbors
        neighbors = self.computeNearestNeighbor(userName)
        user = self.ratingData[userName]

        # Calculate total distance
        totalDist = 0.0

        for i in range(self.k):

            totalDist += neighbors[i][1]

        # Calcualte fraction of different distance

        for i in range(self.k):

            books = self.ratingData[neighbors[i][0]]

            for book in books.keys():

                if book not in user.keys():

                    if book not in recommendations.keys():

                        recommendations[book] = neighbors[i][1] / totalDist * books[book]

                    else:

                        recommendations[book] += neighbors[i][1] / totalDist * books[book]

        recommendations = list(recommendations.items())
        recommendations = [(k ,v) for (k ,v) in recommendations]
        recommendations.sort(key = lambda artistTuple: artistTuple[1],
                             reverse = True)

        return recommendations[:self.n]

def testMethod():

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

     a = recommender(users)
     a.loadBookRatingData("/Users/Jeremy/Downloads/BX-Dump/BX-Book-Ratings.csv")
     a.loadBookData("/Users/Jeremy/Downloads/BX-Dump/BX-Books.csv")
     a.loadUserData("/Users/Jeremy/Downloads/BX-Dump/BX-Users.csv")

     print(a.recommend('Jordyn'))
     print(a.recommend('Hailey'))

     b = recommender(users, 3, "manhattan", 5)
     print(b.recommend('Jordyn'))

testMethod()


