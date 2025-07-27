import math

class rgb:

    def __init__(self, r, g, b):
        self._r = r
        self._g = g
        self._b = b

class hsv:

    def __init__(self, h, s, v):
        self._h = h
        self._s = s
        self._v = v


def hsv2rgb(hsv_in: hsv):

    h = hsv_in._h * 360
    h = h % 360
    c = hsv_in._v * hsv_in._s
    # print("c:", c)
    x = c * (1 - abs(((h / 60) % 2) - 1))
    print("x:", x)
    m = hsv_in._v - c
    print("m:", m)

    if 0 <= h and h < 60:
        return rgb(255 * (c + m), 255 * (x + m), 0)
    elif 60 <= h and h < 120:
        return rgb(255 * (x + m), 255 * (c + m), 0)
    elif 120 <= h and h < 180:
        return rgb(0, 255 * (c + m), 255 * (x + m))
    elif 180 <= h and h < 240:
        return rgb(0, 255 * (x + m), 255 * (c + m))
    elif 240 <= h and h < 300:
        return rgb(255 * (x + m), 0, 255 * (c + m))
    elif 300 <= h and h < 360:
        return rgb(255 * (c + m), 0, 255 * (x + m))

if __name__ == "__main__":

    for i in range(10):
        source = hsv(i/10.0, 1.0, 1.0)
        converted = hsv2rgb(source)
        print('#'*80)
        print(converted._r)
        print(converted._g)
        print(converted._b)