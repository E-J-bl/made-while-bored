# made-while-bored
the title tells you everything you need to know
there is some more documentation if you want to change the code 
i will explain it at some point:
  the code works...

how to add more recipies and other:



Adding base industry:

first add the product into the base industry file in the format:
    product=Producer("product",how many are produced every 0.1 (as an int))

then add the object into the central storage in three places:
    first in self.storage which is the central storage unit. this takes the form:
        "product": self.minimum
            (self.minimum is a variable so use it)
    then under self.equiv in the form:
        "product": product
    finally in self.outtake which is a record of all requests made to the system. in the form:
        "product": 0

Adding secondary industry:
first add it to secondary industry in the format:
    product=Secondary("product",[ingredient1,ingredient2,etc],{ingredient1:1,ingredient2:3,etc})

    the final part represents the ratios of each reasorce needed to produce one of the product

then add the object into the central storage in three places:
    first in self.storage which is the central storage unit. this takes the form:
        "product": self.minimum
    then under self.equiv in the form:
        "product": product
    finally in self.outtake which is a record of all requests made to the system. in the form:
        "product": 0
