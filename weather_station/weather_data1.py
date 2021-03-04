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

class ForecastDisplay(Observer):
    """The ForecastDisplay class shows the weather forcast based on the current
    temperature, humidity and pressure."""

    def __init__(self, weather_data):
        self.weather_data = weather_data  # save the ref in an attribute.
        weather_data.register_observer(self)  # register the observer
        # init the forecast metrics
        self.forecast_temp = 0
        self.forecast_humidity = 0
        self.forecast_pressure = 0

    def update(self, temperature, humidity, pressure):
        self.forecast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        self.forecast_humidity = humidity - 0.9 * humidity
        self.forecast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
        self.display()

    def display(self):
        print(
            "Forecast conditions:",
            self.forecast_temp,
            "F degrees and",
            self.forecast_humidity,
            "[%] humidity",
            "and pressure",
            self.forecast_pressure,
        )


class WeatherStation:
    def run(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)

        # Create two objects from StatisticsDisplay class and
        # ForecastDisplay class. Also register them to the concerete instance
        # of the Subject class so the they get the measurements' updates.
        stats_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)

        weather_data.set_measurements(80, 65, 30.4)
        weather_data.set_measurements(82, 70, 29.2)
        weather_data.set_measurements(78, 90, 29.2)

        # un-register the observer
        weather_data.remove_observer(current_display)
        weather_data.set_measurements(120, 100, 1000)


if __name__ == "__main__":
    ws = WeatherStation()
    ws.run()