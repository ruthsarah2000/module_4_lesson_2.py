'''
Implement a system to handle building records using file operations. Create a Building class and write a script 
to save and load building details to and from a file.
'''

class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def save_to_file(self, filename):
        """
        Saves the building details to a file.

        Parameters:
        filename (str): The name of the file to save to.
        """
        with open(filename, "w") as file:
            file.write(f"{self.name},{self.floors}")

    @classmethod
    def load_from_file(cls, filename):
        """
        Loads building details from a file and creates a Building object.

        Parameters:
        filename (str): The name of the file to load from.

        Returns:
        Building: The Building object loaded from the file.
        """
        with open(filename, "r") as file:
            data = file.readline().strip().split(",")
            name, floors = data
            return cls(name, int(floors))

if __name__ == "__main__":
   
    building1 = Building("Tower A", 30)
    building1.save_to_file("building_details.txt")
  
    loaded_building = Building.load_from_file("building_details.txt")

    print("Loaded Building Details:")
    print("Name:", loaded_building.name)
    print("Floors:", loaded_building.floors)
