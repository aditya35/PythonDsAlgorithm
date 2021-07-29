from heapq import heapify , heappush, heappop

class emp :
    def __init__(self,name,age:int):
        self.name = name
        self.age = age

    def __lt__(self, nxt):
        return self.name > nxt.name

    def print_me(self):
        print("name is ",self.name,end="   ")
        print("age is ",self.age)


if __name__ == "__main__":
    min_heap  = []
    heapify(min_heap)
    heappush(min_heap,1)
    heappush(min_heap,2)
    heappush(min_heap,1)
    heappush(min_heap,2)



    while len(min_heap) > 0 :
        print(heappop(min_heap))

    my_dict = {'z': 'aebra', 'b': 'call', 'w': 'ihale',
               'a': 'zpple', 'm': 'lonkey', 'c': 'gat'}

    my_list = [ (k,v) for k,v in my_dict.items()]

    print(my_list)

    heapify(my_list)

    while(len(my_list)>0):
        print(heappop(my_list))

    emps = []

    heappush(emps,emp("Aditya",23))
    heappush(emps,emp("za",67))
    heappush(emps,emp("sja",24))

    heapify(emps)
    while len(emps) > 0 :
        heappop(emps).print_me()