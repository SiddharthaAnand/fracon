
class Ticketman:
    def __init__(self, _name):
        print('Ticketman...init')
        self._name = _name

    def create(self):
        print ('Ticketman...create')

    @classmethod
    def deserialize(cls, data):
        return cls(**data)