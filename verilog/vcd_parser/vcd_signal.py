class Signal:
    def __init__(self, name: str, id: str, type: str, width: int):
        self.name = name
        self.id = id
        self.type = type
        self.width = width
        self.values = []

    def get_values(self, max_time_stamp: int) -> [str]:
        size = len(self.values)
        new_values = []
        self.values.append((self.values[size - 1][0], max_time_stamp))
        size = len(self.values)
        for i in range(size - 1):
            if self.values[i + 1][1] <= max_time_stamp:
                for j in range(self.values[i][1], self.values[i + 1][1]):
                    new_values.append(self.values[i][0])

        return new_values

    def __repr__(self):
        return "Name: %s\nID: %s\nType: %s\nWidth: %s\nValues: %s\n" % (
            self.name, self.id, self.type, self.width, self.values)


class SignalStore:
    def __init__(self):
        self.signals = {}
        self.name_id_map = {}
        self.time_scale = 1
        self.unit = 's'
        self.max_time_stamp = 0

    def update_timescale(self, time_scale: int, unit: str):
        self.time_scale = time_scale
        self.unit = unit

    def get_time_scale(self) -> int:
        return self.time_scale

    def get_unit(self) -> str:
        return self.unit

    def get_max_time_stamp(self) -> int:
        return self.max_time_stamp

    def set_max_time_stamp(self, time_stamp: int):
        self.max_time_stamp = time_stamp

    def get_signal(self, name):
        id = self.name_id_map[name]
        return self.signals[id]
