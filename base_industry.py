import time


class Producer():
    def __init__(self, product,production_rate:int):
        self.state = False  # on or off (currently on off)
        self.production_rate = production_rate
        self.product = product
        self.request_pending = 0  # this is a U64 number that is modified by central to show the amount that is being
        # requested for production. may not be needed
        self.recipes = {}
    def prod_setup(self,pending):
        return []

    def prod(self, pending):
        self.state = True
        self.request_pending = pending
        for i in range(pending):
            time.sleep(0.1)
            yield [self.product, self.production_rate]
            self.request_pending -= 1
        self.state = False
        self.request_pending = 0


    def __str__(self):
        return self.product


iron = Producer("iron",3)
copper = Producer("copper",2)
energy = Producer("energy",5)
oil = Producer("oil",3)
rem = Producer("rem",1)  # rare earth metals
