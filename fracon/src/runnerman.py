import sys

sys.path.insert(0, '/home/sid/github/reconciliation_framework')
from fracon.src import reconman
import json


def serialize():
    from fracon.src import initial_query, suppressions_query, preferences_query, ticketman, postman
    recon = reconman.Reconman(_initial_query=initial_query.InitialQuery(),
                              _suppression_query=suppressions_query.SuppressionQuery(),
                              _preferences_query=preferences_query.PreferenceQuery(),
                              _postman=postman.Postman(),
                              _ticketman=ticketman.Ticketman())
    data = json.dumps(recon, default=lambda o: o.__dict__, indent=4)
    print(data)


def deserialize(_config=None):
    recons = reconman.Reconman.deserialize(json.load(_config))
    # for recon in recons:
    print()
    print('-' * 20)
    print('type(recon) - ', type(recons))
    print('type(recon._initial_query) - ', type(recons._initial_query))
    print('recon._initial_query - ', recons._initial_query)
    print('recon._suppression_query - ', str(recons._suppression_query))
    print('recon._preference_query - ', recons._preference_query)
    print('recon._send_mail - ', recons._email)
    print('recon._ticket - ', recons._ticket)
    print('recon._run - ', recons.run())
    print('recon._run - ', recons._kargs)


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as _config:
            deserialize(_config=_config)
    else:
        print('\t\tUsage : python fracon/src/runnerman.py fracon/configuration/serialized_config')
        sys.exit(1)