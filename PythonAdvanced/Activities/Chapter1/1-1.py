import math


class Observation:
    def __init__(self, time: int, magnitude: float, error: float):
        self.time = time
        self.magnitude = magnitude
        self.error = error


class Star:

    def __init__(self, identifier, ra: float, dec: float, observation: Observation):
        self.identifier = identifier
        self.ra = ra
        self.dec = dec
        self.observation = observation

    def add_observation(self, time, magnitude, error):
        self.observations.append((time, magnitude, error))

    def calculate_average_magnitude(self):
        pass

    def calculate_magnitude_variance(self):
        pass


class Field:

    def __init__(self):
        self.stars = []

    def add_star(self, star):
        self.stars.append(star)


class Sky:

    def __init__(self):
        self.fields = []

    def add_field(self, field):
        self.fields.append(field)


# Example usage:
sky = Sky()

# Create a field and add it to the sky
field1 = Field()
sky.add_field(field1)

# Create stars and add them to the field
star1 = Star("Star1", 123.45, -67.89, "RR Lyrae")
star1.add_observation(0, 10, 0.1)
star1.add_observation(100, 12, 0.2)
field1.add_star(star1)

# Calculate average and variance for the star
average_magnitude = star1.calculate_average_magnitude()
variance = star1.calculate_magnitude_variance()
print("Average magnitude:", average_magnitude)
print("Variance:", variance)
