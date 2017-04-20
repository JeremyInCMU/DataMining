################# K - means clustering #####################
# 1. Algorithm Description and Complexity analysis
# 2. Metric to measure the distances:
#    Euclidean Distance: dist = ((x1 - x2)^2 + (y1 - y2)^2)^0.5
# 3. How to choose initial centroid locations:
#    Randomly choose cnetroids
# 4. How do you assign a data point to a centroid in your program iteration?
#    - Calculate the distance between a data point and all centroids.
#    - Find the minimum distance and then assign the data point to corresponding 
#      centroid.
#
# 5. what criteria you use to choose the best K value to classify your data set.
#      Fewer than 1% of the points are shifting from one cluster to another.
#
# Before hand:
#    - Calculate median for each attribute values
#    - Calculate absolute standard deviation of each attribute values
#    - Normalization of value for each attributes.
############################################################
from random import randint
import math
import copy

class Cluster:

    # Constructor
    def __init__(self, k, fileName, attributes, tolerance):
        self.k = k # Number of expect clusetrs
        self.tolerance = tolerance # The tolerance for iteration
        # Contain whole data of the input file. 
        self.data = dict()
        self.attributes = attributes
        self.file = open(fileName, "r");
        # Contain median value of each column
        self.median = dict()
        # Contain absolute standard deviation of each column
        self.asd = dict()
        # Contain centroid information
        self.centroids = dict()
        # Keep track of cluster status of each item
        self.cluster = list()
        # Keep track of the number of points whose cluster status is changing
        self.numOfClusterChange = 0
        # Calculate sse
        self.sse = 0
        # Keep track of iterations
        self.iterationNum = 0

    # Functinal Methods
    # Migrate data from file to data structure of this app.
    # BigO: O(n^2)
    def readData(self):
        attrLen = len(self.attributes)
        # Initialize data structure to store data import from the file.
        # Time complexity O(n)
        for key in self.attributes:
            self.data[key] = list()

        # Read data from file to the data structure
        # Time complexity O(n^2)
        lines = self.file.read().split("\n")
        for line in lines:
            values = line.split("\t")
            for i in range(len(self.attributes)):
                self.data[self.attributes[i]].append(float(values[i]))
        self.file.close()

    # Impelment normalization
    # BigO: O(n)
    def normalization(self):
        self.getMedian()
        self.getAsd()
        for key in self.data.keys():
            if (key == self.attributes[-1]): continue # Last column exception
            for i in range(len(self.data[key])):
                self.data[key][i] = (self.data[key][i] - self.median[key]) / self.asd[key]

    # Get median of each column
    # BigO: O(n)
    def getMedian(self):
        for key in self.data.keys():
            if (key == self.attributes[-1]): continue # Last two columns exception
            sortList = copy.deepcopy(self.data[key])
            sortList.sort()
            mid = sortList[len(sortList) // 2]
            if (len(sortList) % 2 == 0):
                mid += sortList[len(sortList) // 2 - 1]
                mid /= 2.0
            self.median[key] = mid

    # Get absolute standard deviation of each column
    # BigO: O(n^2)
    def getAsd(self):
        for key in self.data.keys():
            if (key == self.attributes[-1]): continue # Last two columns exception
            diff = 0
            n = len(self.data[key])
            mid = self.median[key]
            for val in self.data[key]:
                diff += abs(val - mid)
            self.asd[key] = diff / n

    # Initialize centroids
    # BigO: O(n^2)
    def initCentroids(self):
        length = len(self.data[self.attributes[0]])
        existRand = list() # Random numbers have been choosen
        for i in range(self.k):
            num = randint(0, length - 1)
            while (num in existRand):
                num = randint(0, length - 1)
            tempList = list()
            for key in self.attributes:
                tempList.append(self.data[key][num])
            self.centroids[i] = tempList
        # Initialize cluster status
        for i in range(len(self.data[self.attributes[0]])):
            self.cluster.append(-1);
    
    # Assign points to cluster
    # BigO: O(n^2)
    def assignPoints2Cluster(self):
        self.sse = 0
        self.numOfClusterChange = 0
        for i in range(len(self.data[self.attributes[0]])):
            min = 999999
            clusterType = -1
            for j in range(self.k):
                dist = self.calDist(i, j)
                if (dist < min): 
                    min = dist
                    clusterType = j;
            if (self.cluster[i] != clusterType):
                self.numOfClusterChange += 1
                self.cluster[i] = clusterType
            self.sse += min**2

    # Calculte distance
    # BigO: O(n)
    def calDist(self, k, j):
        # k is the index of item in self.data
        # j is the index of centroid which refers to cluster
        diff = 0;
        for i in range(len(self.attributes) - 1):
            diff += (self.data[self.attributes[i]][k] - self.centroids[j][i]) ** 2
        return diff ** 0.5

    # Update centroids
    # BigO: O(n^3)
    def updateCentroids(self):
        for i in range(self.k):
            temp = list()
            for j in range(len(self.cluster)):
                if  j == i: temp.append(j)
            self.updateCentroid(i, temp)

    # Update centroid
    # BigO: O(n^2)
    def updateCentroid(self, i, member):
        newCentroid = list()
        for key in self.data.keys():
            sumResult = 0
            for index in member:
                sumResult += self.data[key][index]
            newCentroid.append(sumResult / len(member))
            self.centroids[i] = newCentroid

    # Execute the iteration to get k clusters
    # BigO: O(n)
    def iteration(self):
        self.readData()
        self.normalization()
        self.initCentroids()
        self.assignPoints2Cluster()

        while True:
            if float(self.numOfClusterChange) / len(self.cluster) < self.tolerance:
                break
            self.iterationNum += 1
            self.updateCentroids()
            self.assignPoints2Cluster()

        print("The iteration number is %d" % self.iterationNum)
        print("The SSE is: %f" % self.sse)
        
        for i in range(self.k):
            temp = list()
            print("Cluster %d: " % i)
            print(" ========= ")
            for j in range(len(self.cluster)):
                if (self.cluster[j] == i):
                    temp.append(j)
            print(temp)
            print(" ========= ")
            print("\n")

def test():
    attributes = list()
    attributes.append("A")
    attributes.append("P")
    attributes.append("C")
    attributes.append("L")
    attributes.append("W")
    attributes.append("AC")
    attributes.append("LKG")
    attributes.append("Class")

########### Update ############
    result = dict()

    for k in range(1, 10):
        testCluster = Cluster(k, "seeds_dataset.txt", attributes, 0.01)
        testCluster.iteration()
        result[k] = testCluster.sse
    print(result)
###############################
test()


