class Color(object):

    def __init__(self, r=0, g=0, b=0):

        self._r = self._clamp(r)
        self._g = self._clamp(g)
        self._b = self._clamp(b)

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

    def set(self, other_color):
        if isinstance(other_color, list):
            self.r = other_color[0]
            self.g = other_color[1]
            self.b = other_color[2]
        elif isinstance(other_color, tuple):
            self.r = other_color[0]
            self.g = other_color[1]
            self.b = other_color[2]
        elif isinstance(other_color, Color):
            self.r = other_color.r
            self.g = other_color.g
            self.b = other_color.b

    def get(self):
        return [self.r, self.g, self.b]

class Red(Color):
    def __init__(self):
        super().__init__(255, 0, 0)

class Green(Color):
    def __init__(self):
        super().__init__(0, 255, 0)

class Blue(Color):
    def __init__(self):
        super().__init__(0, 0, 255)

class Orange(Color):
    def __init__(self):
        super().__init__(255, 127, 0)

class Yellow(Color):
    def __init__(self):
        super().__init__(255, 255, 0)

class Cyan(Color):
    def __init__(self):
        super().__init__(0, 255, 255)

class Indigo(Color):
    def __init__(self):
        super().__init__(75, 0, 130)

class Violet(Color):
    def __init__(self):
        super().__init__(148, 0, 211)
