class ExceptionMan:
    def __init__(self):
        print('ExceptionMan...init()')

    def __repr__(self):
        print('ExceptionMan...repr()')

    def run(self):
        print('ExceptionMan...run()')

    @classmethod
    def deserialize(cls, data):
        return cls(**data)

