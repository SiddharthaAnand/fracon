import sys
sys.path.insert(0, '/home/sid/github/reconciliation_framework')
from fracon.src import queryman


class PreferenceQuery(queryman.QueryMan):
    def __init__(self, _name, _select, _from, _where, _kargs):
        super().__init__(_name=_name,
                         _select=_select,
                         _from=_from,
                         _where=_where,
                         _kargs=_kargs)
        print('Preference Query...init()')
