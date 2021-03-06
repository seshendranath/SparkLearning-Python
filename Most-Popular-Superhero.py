#most popular superhero-max co-occurences
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("PopularHero")
sc = SparkContext(conf = conf)

def countCoOccurences(line): #no.of times hero co-occured with other superheroes
    elements = line.split()
    return (int(elements[0]), len(elements) - 1)

def parseNames(line):
    fields = line.split('\"')
    return (int(fields[0]), str(fields[1].encode('ascii', 'ignore'),("utf-8")))

names = sc.textFile("C:/SparkCourse/marvel-names.txt")
namesRdd = names.map(parseNames) 

lines = sc.textFile("C:/SparkCourse/marvel-graph.txt")

pairings = lines.map(countCoOccurences)
totalFriendsByCharacter = pairings.reduceByKey(lambda x, y : x + y)
flipped = totalFriendsByCharacter.map(lambda x_y : (x_y[1],x_y[0]))

mostPopular = flipped.max() #max key value

mostPopularName = namesRdd.lookup(mostPopular[1])[0] #lookup the name
#print (mostPopularName)
print(mostPopularName + " is the most popular superhero, with " + str(mostPopular[0]) + " co-appearances.")
