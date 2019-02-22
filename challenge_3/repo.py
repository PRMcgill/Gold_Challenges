
import event

outings = []


class Menu_functions:

    def show_outings(self):
        return outings

    def add_outing(self, event_type, people_attending, date, cost_per_person):
        ao = event.Event(event_type, people_attending, date, cost_per_person)
        outings.append(ao)

        


