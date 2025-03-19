#!/usr/bin/python3

class passenger:
    passenger_names = []
    total_weight = 350

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def weight_count(self):
        if self.weight > self.total_weight:
            print(f"{self.name} is carrying Too much weight!")
        else:
            print(f"{self.name} carrying {self.weight}kg")


Amazing = passenger("Amazing", 32)
Regina = passenger("Regina", 354)

Amazing.weight_count()
Regina.weight_count()
