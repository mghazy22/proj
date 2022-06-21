import json
import csv
from queueman import queuem

class newqueue(queuem):
    no_of_objects=0
    savedqu={}
    def __init__(self,name,size):
        super(newqueue, self).__init__()
        self.name=name
        self.size=size




    @classmethod
    def savedobject(cls,my_str):
       con=json.loads(my_str)
       cls.savedqu={"name":con["name"],"size":con["size"]}
       cls.no_of_objects += 1
       cls.q1.clear()
       return newqueue(con["name"],con["size"])

    @classmethod
    def save(cls):
        with open('f1.csv','a') as f:
            w=csv.writer(f)
            w.writerow(cls.savedqu.values())
            f.close()
    @classmethod
    def load(cls):
        file = open("f1.csv")
        csvreader = csv.reader(file)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)
        file.close()


    def insert (self, item2):
        self.q1.append(item2)
        if len(self.q1) >= self.size:
           raise TypeError("QueueOutOfRangeException")


str='{"name":"a1","size":3}'
str2='{"name":"a2","size":6}'
q1=newqueue.savedobject(str)
q1.insert(3)
q1.insert(2)
q1.printqueue()
q2=newqueue.savedobject(str2)
q2.insert(32)
q2.insert(22)
q2.printqueue()






