class QueryMan:
    def __init__(self, _name, _select, _from, _where, **kargs):
        self._name, self._select, self._from, self._where, self._kargs = _name, _select, _from, _where, kargs

    def __repr__(self):
        return '{0}'.format(self._name)

    @classmethod
    def deserialize(cls, data):
        return cls(**data)
