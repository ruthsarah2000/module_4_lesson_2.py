'''
Develop a Bus class as part of a public transportation module. Use class variables to represent common attributes like city 
name and base fare. Implement instance variables for specific attributes like route number and passenger capacity.
'''


class Bus:
    city_name = "YourCity" 
    base_fare = 2.50  

    def __init__(self, route_number, passenger_capacity):
        self.route_number = route_number  
        self.passenger_capacity = passenger_capacity  

    def calculate_fare(self, distance):
        """
        Calculates the fare for a given distance.

        Parameters:
        distance (float): The distance traveled by the bus.

        Returns:
        float: The calculated fare.
        """
        return self.base_fare * distance

class TransportationModule:
    @staticmethod
    def show_bus_details(bus):
        """
        Displays details of a bus.

        Parameters:
        bus (Bus): The Bus object.
        """
        print("Bus Details:")
        print("City:", bus.city_name)
        print("Route Number:", bus.route_number)
        print("Passenger Capacity:", bus.passenger_capacity)
        print("Base Fare:", bus.base_fare)

if __name__ == "__main__":
   
    bus1 = Bus("101", 50)
    bus2 = Bus("102", 40)

    
    print("Common Bus Attributes:")
    print("City Name:", Bus.city_name)
    print("Base Fare:", Bus.base_fare)

   
    TransportationModule.show_bus_details(bus1)
    TransportationModule.show_bus_details(bus2)

    distance_traveled = 10  
    fare_bus1 = bus1.calculate_fare(distance_traveled)
    fare_bus2 = bus2.calculate_fare(distance_traveled)
    print("\nFare for Bus 1:", fare_bus1)
    print("Fare for Bus 2:", fare_bus2)
