class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def register_observer(observer):
        pass

    def remove_observer(observer):
        pass

    # This method is called to notify all observers
    # when the Subject's state (measuremetns) has changed.
    def notify_observers():
        pass


# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        pass



class WeatherData:
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        
    def register_observer(self, observer):
        # When an observer registers, we just
        # add it to the end of the list.
        self.observers.append(observer)

    def remove_observer(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)

    def notify_observers(self):
        # We notify the observers when we get updated measurements
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurements_changed()
    def measurementsChanged(self):
        """Notifies other part of the program that the measurements 
        has been updated.
        """
        # Grab the most recent measurements by calling the WeatherData's getter
        # methods (already implemented).
        temp = getTemperature()
        humidity = getHumidity()
        pressure = getPressure()
        
        # Now update the display
        currentConditionsDisplay.update(temp, humidity, pressure)
        statisticsDisplay.update(temp, humidity, pressure)
        forcastDisplay.update(temp, humidity, pressure)
        


class CurrentConditionsDisplay(Observer):
    def __init__(self, weather_data):
        self.temerature = 0
        self.humidity = 0
        self.pressure = 0

        self.weather_data = weather_data  # save the ref in an attribute.
        weather_data.register_observer(self)  # register the observer
        # so it gets data updates.

    def update(self, temperature, humidity, pressure):
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print(
            "Current conditions:",
            self.temerature,
            "F degrees and",
            self.humidity,
            "[%] humidity",
            "and pressure",
            self.pressure,
        )

