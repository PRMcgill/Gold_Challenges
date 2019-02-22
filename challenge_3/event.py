
class Event:

    def __init__(self, event_type: str, people_attending: int, date: str, cost_per_person: float):
        self.event_type = event_type
        self.people_attending = people_attending
        self.date = date
        self.cost_per_person = cost_per_person
        

    def __repr__(self):
        return self.event_type
