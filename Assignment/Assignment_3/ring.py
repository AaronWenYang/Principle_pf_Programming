class Ring(list):
    
    def __init__(self, _values=[]):
        if type(_values) is set:
            raise TypeError("'set' object is not subscriptable")
        if type(_values) is int:
            raise TypeError("'int' object is not subscriptable")
        if type(_values) is list or tuple :
            self._values = _values

    def __repr__(self):
        return "Ring({})".format(self._values)

    def __str__(self):
        return str(self._values)

    def __len__(self):
        return len(self._values)
