class Car:
    def __init__(self): # Constructor Function
        # define class properties here
        self.wheel_count = 0
        self.color = "Red"
        self.engine_model = "V8"
        self.fuel_tank_cpacity = 37
        self.fuel_type = "Petrol"
        self.current_gear = 0
        self.max_gear = 6
    
    # define class methods
    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")
        self.current_gear = 0

    def shift_up(self):
        if(self.current_gear < 6):
            self.current_gear += 1

    def shift_down(self):
        if(self.current_gear > 1):
            self.current_gear -= 1

# Class Ended

demo_car = Car()
demo_car.start()
demo_car.shift_up()
print(demo_car.current_gear)
demo_car.shift_up()
print(demo_car.current_gear)
demo_car.shift_up()
print(demo_car.current_gear)
demo_car.shift_down()
print(demo_car.current_gear)
demo_car.stop()
