class Plant:
    def __init__(self, plant_name , plant_type, season):
        self.plant_name=plant_name
        self.plant_type=plant_type
        self.season=season

    def print_object(self):
        print(f"the name of plant is : {self.plant_name} ,the type of plant is : {self.plant_type} and the best time to plant the plant is in the season : {self.season.season}" )

class Season:
    def __init__(self, season):
        self.season=season

s1=Season("autumn")
s2=Season("summer")
s3=Season("summer")
s4=Season("winter")
s5=Season("spring")

p1=Plant("apple","fruit",s1)
p2=Plant("tomato","vegetable",s2)
p3=Plant("banana","fruit",s3)
p4=Plant("orange","fruit",s4)
p5=Plant("potato","vegetable",s5)

p1.print_object()
p2.print_object()
p3.print_object()
p4.print_object()
p5.print_object()

                