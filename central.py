from base_industry import *
from secondary_industry import *
import math

class Storage():
    def __init__(self, mininum):
        self.mininum = mininum
        self.storage = {"iron": self.mininum, "copper": self.mininum, "energy": self.mininum, "oil": self.mininum,
                        "rem": self.mininum, "copper_wires": self.mininum, "fuel": self.mininum,
                        "plastic": self.mininum, "circuitry": self.mininum, "steel": self.mininum}
        self.equiv = {"iron": iron, "copper": copper, "energy": energy, "oil": oil, "rem": rem,
                      "copper_wires": copper_wires, "fuel": fuel,
                      "plastic": plastic, "circuitry": circuitry, "steel": steel}
        self.outtake={"iron": 0, "copper": 0, "energy": 0, "oil": 0,
                        "rem": 0, "copper_wires": 0,"fuel": 0,
                        "plastic": 0, "circuitry": 0, "steel": 0}

    def podfunc_to_storage(self, func):
        for i in func:
            self.storage[i[0]] += i[1]
        print(self.storage)

    def greater_demand_check(self, required_ingredients):
        print(f"checking dependencies, list of dependencies: \n {required_ingredients}\n then acting on the dependencies")

        for ingredient in required_ingredients:
            print(ingredient, ingredient[0], self.storage[ingredient[0]], ingredient[1])
            if self.storage[ingredient[0]] < abs(ingredient[1]):
                print("found that greater demand than supply")

                if self.equiv[ingredient[0]].prod_setup(1) == []:
                    x = self.equiv[ingredient[0]].prod(abs(ingredient[1]) - self.storage[ingredient[0]])
                    print("producing primary")
                    self.podfunc_to_storage(x)
                else:
                    print("producing secondary, need to check if sufficient materials are present")
                    self.greater_demand_check(
                        self.equiv[ingredient[0]].prod_setup(abs(ingredient[1]) - self.storage[ingredient[0]]))
        print(self.storage)
        return True

    def run(self):
        running = True
        while running == True:
            print(self.storage)
            take_out = input("what item do you want out:")
            take_val = int(input("how much (int):"))
            self.outtake[take_out]+=take_val
            self.storage[take_out] -= take_val
            print(self.storage, "\n", take_out, take_val, "\n")
            for key, val in self.storage.items():
                if val < self.mininum:
                    print("solving deficit caused by",key,"\n")
                    current_producer = self.equiv[key]
                    setup = current_producer.prod_setup(self.mininum - val)
                    setting_up = self.greater_demand_check(setup)

                    for i in current_producer.prod(self.mininum - val):
                        self.storage[i[0]] += i[1]
                        if current_producer.recipes != {}:
                            for key, val in current_producer.recipes.items():
                                self.storage[key] -= val




            print("balancing")
            print(self.storage)
            while not all(val >= self.mininum for key, val in self.storage.items()):
                for key, val in self.storage.items():
                    if val < self.mininum:
                        print("\n",key)
                        current_producer = self.equiv[key]
                        setup = current_producer.prod_setup(self.mininum - val)
                        setting_up = self.greater_demand_check(setup)

                        for i in current_producer.prod(math.ceil((self.mininum - val)/current_producer.production_rate)):
                            self.storage[i[0]] += i[1]
                            if current_producer.recipes != {}:
                                for [key, val] in current_producer.recipes.items():
                                    self.storage[key] -= val

                time.sleep(0.05)
                print(self.storage)
            print("balanced")
            running = bool(input("do you want to continue? True/False"))

        pass

