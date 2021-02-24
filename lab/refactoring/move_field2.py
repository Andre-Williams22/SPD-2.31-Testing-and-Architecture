# Kami Bigdely
# Move Field

class Car:
    def __init__(self, engine, wheels, cabin, tpms_di, fuel_tank):
        self.engine = engine
        # TODO: tpms is better to be in the Wheel class. 
        # Each wheel has a single tpms attached to it. 
        # Thus, instead of having a list of tpms in 'Car' class
        # have each of the tpms in each 'Wheel'.
        self.tpms_list = tpms_di  # Tire Pressure Monitoring System.
        self.wheels = wheels
        # Set wheels' car reference into each wheel.
        for w in wheels:
            w.set_car(self)
            
        self.cabin = cabin
        self.fuel_tank = fuel_tank

    
class Wheel:
    # TODO: You may add tpms as a method parameter here to 
    #       initilaize the 'Wheel' object or you can create
    #       a setter method to set the tpms of the wheel. (you can do 
    #       both of course.)
    def __init__(self, car = None, wheel_location = None, serial_number=None):
        self.car = car
        self.wheel_location = wheel_location
        self.serial_number = serial_number
        self.sensor_transmit_range = 300 # [feet]
        self.sensor_pressure_range = (8,300) # [PSI]
        self.battery_life = 6 # [year]

    def install_tire(self):
        print('remove old tube.')
         # TODO: Rewrite the following after moving tpms to the 'Wheel' class
        print('cleaned tpms: ', 
              self.car.tpms_di[self.wheel_location].get_serial_number, 
              '.')
        print('installed new tube.')        
        
    def read_tire_pressure(self):
        # TODO: After making tpms an attribute of 'Wheel' class,
        #       rewrite the following.
        return self.car.tpms_di[self.wheel_location].get_pressure()
    
    def set_car(self, car):
        self.car = car
        
    def get_pressure(self):
        return 3
    
    def get_serial_number(self):
        return self.serial_number
        

class Engine:
    def __init__(self):
        pass
    
class FuelTank:
    def __init__(self):
        pass
    
class Cabin:
    def __init__(self):
        pass    
    

engine = Engine()
# TODO: Rewrite the following after moving tpms to the 'Wheel' class.
wheels = [Wheel(None, 'front-right', 983408543), Wheel(None, 'front-left', 4343083), 
          Wheel(None, 'back-right', 23654835), Wheel(None, 'back-left', 3498857)]

cabin  = Cabin()

fuel_tank = FuelTank()

my_car = Car(engine, wheels, cabin, fuel_tank)


