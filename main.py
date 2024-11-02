
class Worker:
    def __init__(self,name,age):
        self.Name=name
        self.Age=age

wor1=Worker("Andrew", 23)
wor2=Worker("adolf", 43)
wor3=Worker("bimba", 47)
wor4=Worker("amogus", 33)
wor5=Worker("sigma", 1945)

worker_list=[wor1, wor2, wor3, wor4,wor5]

print (worker_list)


worker_iter=iter(worker_list)

for elem in worker_iter:
    print(elem.Name, elem.Age)
