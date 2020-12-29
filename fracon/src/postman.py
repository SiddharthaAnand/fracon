class Postman:
    def __init__(self, _from, _to, _subject, _body):
        print ('Postman...init()')
        self._from = _from
        self._to = _to
        self._subject = _subject
        self._body = _body

    def create(self):
        print ('Postman...create()')

    @classmethod
    def deserialize(cls, data):
        return cls(**data)