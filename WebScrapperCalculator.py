######################################################
#
#   Web Content Similarity Calculator
#
#   Author: Jeremy
######################################################

# Import Library
import urllib.request
import enchant
from bs4 import BeautifulSoup

class WebSimilarityCalculator:

    # Constructor
    def __init__(self, urlList):

        self.urlList = urlList # Store the input urls. 
        self.URLList = dict()  # Store URLs which are objects of each url and
                               # contains similarity information between current
                               # url and other urls.

    def process(self):  # Calculate similarities among different urls.

        for i in range(len(self.urlList)):

            url = URL(self.urlList[i])

            for j in range(len(self.urlList)):

                if self.urlList[j] in self.URLList: 
                    # If the similarity has been calculated
                    url.similarities[self.urlList[j]] = self.URLList[self.urlList[j]].similarities.get(self.urlList[i])
                else: 
                    #If not
                    url.similarities[self.urlList[j]] = calWebContentSimilarity(self.urlList[i], self.urlList[j])

            self.URLList[self.urlList[i]] = url

    def extractSimilarityResults(self):  # Print out all similarity results.

        # Print out the map from url to numbers.
        for i in range (len(self.urlList)):

            print(i, end = "")
            print(" : ", end = "")
            print(self.urlList[i])


        print(" " * 8, end = "")

        # Print the first line (each url)
        for j in range (len(self.urlList)):

            print(j, end = "")
            print(" " * 8 ,end = "")

        print("")

        # Print similarity data
        for m in range(len(self.urlList)):

            print(m , end = "")
            print(" " * 5, end = "")

            for n in range (m):

                print ("%.2f" % self.URLList[self.urlList[m]].similarities.get(self.urlList[n]), end = "")
                print (" " * 5, end = "")

            print("")

    def extractMostSimilarResults(self):   # Print out most similar url in the url set for each url.

        for url in self.urlList:

            print(url + " most similar web page is: " + "    " + self.URLList[url].getMostSimilarWeb())


#####################################
#   Helper Methods
#####################################

# Web similarity calculator
def calWebContentSimilarity(url1, url2):

    return calSimilarity(scrapWebContent(url1),
                         scrapWebContent(url2))

# Web Scrapper wrapper method
def scrapWebContent(destURL):

    html = urllib.request.urlopen(destURL).read()

    #soup = BeautifulSoup(html)
    soup = BeautifulSoup(html, "lxml" )

    # remove all script and style elements
    for script in soup(["script", "style"]):
        script.extract()

    # now retrieve text
    text = soup.get_text()

    # Extract words out of the string
    lines = text.split("\n")

    # Create a dictionary to contain all the words
    # and corresponding couts
    content = dict()

    # Create a dictionary to check if a string represents a valid word
    d = enchant.Dict("en_US")

    # Go through each line and get words
    for line in lines:
        if len(line) != 0:
            words = line.split(" ");
            for word in words:
                if (len(word) > 0 and d.check(word)):
                    content[word] = content.get(word, 0) + 1;

    return content


# Caclculate similarity between two contents
def calSimilarity(content1 , content2):

    innerProduct = product(content1, content2)
    norm1 = norm(content1)
    norm2 = norm(content2)

    if (innerProduct == 0 or
         norm1 == 0 or
         norm2 == 0):
        return 0

    return innerProduct / (norm1 * norm2)

# Calculate inner products of two vectors
def product(content1, content2):

    result = 0

    for key in content1.keys():
        
        result += content1[key] * content2.get(key, 0)

    return result

# Calculate norm of a vector
def norm(content):

    result = 0

    for value in content.values():
        result += value * value

    return result**0.5

###############################################
#
#   Class to contain similarity information
#
###############################################
class URL():

    def __init__(self, url):
        self.url = url
        self.similarities = dict()

    def getMostSimilarWeb(self):
        maxSimilarity = 0
        result = ""
        for key in self.similarities.keys():
            if (self.url != key and 
                self.similarities[key] > maxSimilarity):
                maxSimilarity = self.similarities[key]
                result = key;
        return result

    def getSimilarities(self):
        return self.similarities


#########################################
#             Test Cases
#########################################


def testCase():

    url1 = "https://www.jpmorgan.com/country/US/en/jpmorgan"
    url2 = "http://bankofamerica.com/"
    url3 = "http://rutgers.edu/"
    url4 = "http://www.rutgers.edu/"
    url5 = "http://www.cmu.edu/"
    url6 = "https://en.wikipedia.org/wiki/Rutgers_University"
    url7 = "https://en.wikipedia.org/wiki/Carnegie_Mellon_University"
    # url5 = "https://en.wikipedia.org/wiki/Lion"
    # url6 = "https://en.wikipedia.org/wiki/Car"
    # url7 = "https://en.wikipedia.org/wiki/Ford_Motor_Company"

    urlList = list([url1, url2, url3, url4, url5, url6, url7])

    calculator = WebSimilarityCalculator(urlList)
    calculator.process()
    calculator.extractSimilarityResults()
    calculator.extractMostSimilarResults()

testCase()

