class Color(object):

    def __init__(self, r=0, g=0, b=0):

        self._r = r
        self._g = g
        self._b = b

    def _clamp(self, value):
        return max(0, min(255, value))

    @property
    def r(self):
        return self._r
    
    @r.setter
    def r(self, value):
        self._r = self._clamp(value)
    
    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        self._g = self._clamp(value)

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = self._clamp(value)

    def get(self):
        return [self.r, self.g, self.b]