'''
Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner 
to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.
'''

class Vehicle:
    def __init__(self, registration_number, vehicle_type, owner):
        self.registration_number = registration_number
        self.vehicle_type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        """
        Updates the owner of the vehicle.

        Parameters:
        new_owner (str): The new owner's name.
        """
        self.owner = new_owner
        print(f"Owner updated: {self.owner}")


if __name__ == "__main__":
    
    vehicle1 = Vehicle("ABC123", "Car", "Johnny Dep")
    vehicle2 = Vehicle("XYZ789", "Motorcycle", "Angelina Joline")

    print("Initial Owners:")
    print("Vehicle 1 - Owner:", vehicle1.owner)
    print("Vehicle 2 - Owner:", vehicle2.owner)

    vehicle1.update_owner("Michael Jackson")
    vehicle2.update_owner("Sarah Parker")
