# by Kami Bigdely
# Docstrings and blank lines
class OnBoardTemperatureSensor:
    '''Calculates Temperature Sensor'''
    VOLTAGE_TO_TEMP_FACTOR = 5.6
    def __init__(self):
        ''' Initializes variables '''
        pass
    def read_voltage(self):
        ''' Initializes variables '''        
        return 2.7
    def get_temperature(self):
        ''' Initializes variables '''
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]
  
class CarbonMonoxideSensor:
    '''Calculates the Carbon Monoxide '''
    VOLTAGE_TO_CO_FACTOR = 0.048
    
    def __init__(self, temperature_sensor):
        ''' Initializes variables '''
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()
            
    def get_carbon_monoxide_level(self):
        ''' Initializes variables '''
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(
            sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide
    
    def read_sensor_voltage(self):
        ''' Initializes variables '''
        # In real life, it should read from hardware.        
        return 2.3
    
    def convert_voltage_to_carbon_monoxide_level(voltage, temperature):
        ''' Initializes variables '''
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature
    
class DisplayUnit:
    ''' Visualizes a unit'''
    
    def __init__(self):
        ''' Initializes variables '''
        self.string = ''
        
    def display(self, msg):
        ''' Initializes variables '''
        print(msg)
        
class CarbonMonoxideDevice():
    ''' A device capable of Carbon Monoxide'''
    
    def __init__(self, co_sensor, display_unit):
        ''' Initializes variables '''
        self.carbonMonoxideSensor = co_sensor 
        self.display_unit = display_unit 
              
    def display(self):
        ''' Initializes variables '''
        msg = 'Carbon Monoxide Level is : ' + str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)

if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.display()
    