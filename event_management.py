'''
Extend an existing Event class by adding a feature to keep track of the number of participants. 
Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
'''


class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
       
        return self.participant_count


if __name__ == "__main__":
    #event birthday party#
    event = Event("Birthday Party", "2024-04-21")

    event.add_participant()
    event.add_participant()
    event.add_participant()
    event.add_participant()
    event.add_participant()
    event.add_participant()
    event.add_participant()

    participant_count = event.get_participant_count()
    print("Participant Count:", participant_count)
