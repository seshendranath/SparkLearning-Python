#count the number of unique words
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    cust = int(fields[0])
    amount = float(fields[2])
    return (cust, amount)

lines = sc.textFile("C:/SparkCourse/customer-orders.csv")
rdd = lines.map(parseLine)
totalAmountsByCustomer = rdd.reduceByKey(lambda x, y: x + y)
totalAmountsByCustomerSorted = totalAmountsByCustomer.map(lambda x_y: (x_y[1],x_y[0])).sortByKey()

results = totalAmountsByCustomerSorted.collect()
for result in results:
    print(result)



#!spark-submit Word-Count.py
