from color import Color
import hid

IT8297_RGB_CONTROLLER_VENDOR_ID = 0x048d
IT8297_RGB_CONTROLLER_PRODUCT_ID = 0x8297

# Aorus I X570 PRO WIFI INFO
# idVendor           0x048d Integrated Technology Express, Inc.
# idProduct          0x8297 IT8297 RGB LED Controller

FEATURE_REPORT_COLOR = (0xcc,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x01,0x5a,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)

FEATURE_REPORT_COMMIT = (0xcc, 0x28, 0xff,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)


class Device(object):

    def __init__(self, vendor_id, product_id):

        self._vendor_id = vendor_id
        self._product_id = product_id
        self._dev = None

    def open(self):

        assert self._dev is None, "Device already opened!"

        try:
            self._dev = hid.Device(self._vendor_id, self._product_id)
            # self._dev.open(self._vendor_id, self._product_id)
        except Exception as error_:
            print("Tried to open device:\nVendor ID:{}\nProduct ID:{}\nGot:{}".format(self._vendor_id, self._product_id, str(error_)))

    def __str__(self):

        if self._dev is None:
            self.open()

        info = (
            "Manufacturer: {}\n"
            "Product Info: {}"
        ).format(self._dev.get_manufacturer_string(), self._dev.get_product_string())
        return info

    def close(self):

        self._dev.close()
        self._dev = None

class AorusLEDController(Device):

    def __init__(self):
        super(AorusLEDController, self).__init__(IT8297_RGB_CONTROLLER_VENDOR_ID, IT8297_RGB_CONTROLLER_PRODUCT_ID)
        self._color = None
        self._current_group_idx = None
        self._feature_report_color = list(FEATURE_REPORT_COLOR)
        self._feature_report_commit = list(FEATURE_REPORT_COMMIT)

    def __str__(self):

        info = super(AorusLEDController, self).__str__()
        info += "\nAorus I X570 PRO WIFI - Side IO Leds Controller"
        return info

    @property
    def color(self):

        """
        Represents the whole color of the device.
        """

        return self._color

    @color.setter
    def color(self, new_color):

        """
        Sets the current color of the whole led group.
        """

        if self._current_group_idx is None:
            return

        self._color = new_color
        self._feature_report_color[16] = self._color[0] # R
        self._feature_report_color[15] = self._color[1] # G
        self._feature_report_color[14] = self._color[2] # B

    @property
    def current_group_idx(self):

        return self._current_group_idx

    @current_group_idx.setter
    def current_group_idx(self, new_group_idx):

        group_info = (
            (0x20,0x01), #IO_LED
            (0x21,0x02), #LED_CPU
            (0x22,0x04), #LED_CX
            (0x23,0x08), #LED_SID
            (0x25,0x20), #D_LED1 TODO PROBABLE MODES
            (0x26,0x40)  #D_LED2 TODO PROBABLE MODES
        )

        self._current_group_idx = new_group_idx
        self._feature_report_color[1] = group_info[new_group_idx][0]
        self._feature_report_color[2] = group_info[new_group_idx][1]

    def update(self, close=False):

        """
        Write current color to the device.
        """

        if self._color is None:
            return

        self._dev.send_feature_report(bytes(self._feature_report_color))
        self._dev.send_feature_report(bytes(self._feature_report_commit))
        if close:
            self.close()

    def set_color(self, color, idx=None, close=False):

        def _set_color(color):
            self.color = color.get()
            self.update()

        if idx is not None:
            self.current_group_idx = max(0, min(3, idx))
        else:
            for idx in range(4):
                self.current_group_idx = idx
                _set_color(color)

        if close:
            self.close()