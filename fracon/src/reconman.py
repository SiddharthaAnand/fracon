
class Reconman():
    def __init__(self, _initial_query, _suppression_query, _preferences_query, _ticketman, _postman, **kargs):
        self._initial_query = _initial_query
        self._suppression_query = _suppression_query
        self._preference_query = _preferences_query
        self._email = _postman
        self._ticket = _ticketman
        self._kargs = kargs

    def run(self):
        print('Running reconman...run()')

    def send_mail(self):
        print ('Sending mail...whoosh~')

    def create_ticket(self):
        print ('Creating ticket...shoosh~')

    @classmethod
    def deserialize(cls, data):
        from fracon.src import initial_query, suppressions_query, preferences_query, ticketman, postman
        _initial_query = initial_query.InitialQuery.deserialize(data["_initial_query"])
        _suppression_query = suppressions_query.SuppressionQuery.deserialize(data["_suppression_query"])
        _preferences_query = preferences_query.PreferenceQuery.deserialize(data["_preferences_query"])
        _ticketman = ticketman.Ticketman.deserialize(data["_ticketman"])
        _postman = postman.Postman.deserialize(data["_postman"])

        return cls(_initial_query=_initial_query,
                   _suppression_query=_suppression_query,
                   _preferences_query=_preferences_query,
                   _ticketman=_ticketman,
                   _postman=_postman,
                   kargs=data["kargs"])