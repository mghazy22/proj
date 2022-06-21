class queuem:
    q1=[]
    def __init__(self  ):
       pass

    def insert (self, item2):
        queuem.q1.append(item2)


    @property
    def pop(self):
        queuem.q1.pop(0)

    @classmethod
    def printqueue(cls):
        print(cls.q1)
    @classmethod
    def is_empty(cls):
        if not cls.q1:
            print("Empty Queue")
        else:
            print(cls.q1)


