class Vehicle:
    def __init__(self, vin, make , mileage , model ):
        self.vin=vin
        self.make=make
        self.mileage=mileage
        self.model=model

    def get_maintenance_cost(self):
        return 50

class Car(Vehicle):
    def __init__(self, vin, make, mileage, model , passenger_capacity):
        super().__init__(vin, make, mileage , model)
        self.passenger_capacity=passenger_capacity

    def get_maintenance_cost(self):
        return 50 + (self.passenger_capacity*5)  



class Truck(Vehicle):
    def __init__(self, vin, make, mileage , model , payload_capacity):
        super().__init__(vin, make, mileage , model )
        self.payload_capacity=payload_capacity

    def get_maintenance_cost(self):
       return 100 + (self.mileage*0.01)
    


class Motorcycle(Vehicle):
    def __init__(self, vin, make, mileage , model , has_sidecer ):
        super().__init__(vin, make, mileage , model )
        self.has_sidecer=has_sidecer

    def display_info(self):
        if self.has_sidecer:
            print("Sidecar Edition")
        else:
            print("No Sidecar Edition")    


class Fleet:
    def __init__(self):
        self.vehicles=[]
    def add_vehicle(self, vehicle):
            
        self.vehicles.append(vehicle)
    def total_maintenance_cost(self):
        total=0

        for i in range(len(self.vehicles)):
            self.vehicles[i].get_maintenance_cost()
            cost= self.vehicles[i].get_maintenance_cost()
            print(f"the cost of the vehicles : {cost} ")
            total=cost+total

        print(f"the grand total : {total}")

c1=Car(2407, "mercedes", 2000 ,"GLA" , 4)        
t1=Truck(2055 , "BMW", 5000  , "series",100)
m1=Motorcycle(1556 , "BMW" ,  3000,"cruisers"  , True)
fleet1=Fleet()
fleet1.add_vehicle(c1)
fleet1.add_vehicle(t1)
fleet1.add_vehicle(m1)
fleet1.total_maintenance_cost()




        

       