class TemperatureDashboard:
    def __init__(self, threshold=25):
        self.threshold = threshold
        self.temperatures = {'temperature1': 0, 'temperature2': 0, 'temperature3': 0}

    def set_threshold(self, threshold):
        self.threshold = threshold

    def update_temperatures(self, temperature1, temperature2, temperature3):
        self.temperatures['temperature1'] = temperature1
        self.temperatures['temperature2'] = temperature2
        self.temperatures['temperature3'] = temperature3

    def get_temperature_status(self):
        for temp in self.temperatures.values():
            if temp > self.threshold + 5:
                return 'Red'
        for temp in self.temperatures.values():
            if temp > self.threshold:
                return 'Yellow'
        return 'Green'


# Example usage:
dashboard = TemperatureDashboard()

# Set initial temperatures
dashboard.update_temperatures(22, 24, 25)

# User sets threshold
dashboard.set_threshold(30)

# Update temperatures
dashboard.update_temperatures(28, 32, 29)

# Get current temperature status
status = dashboard.get_temperature_status()
print("Current Status:", status)
