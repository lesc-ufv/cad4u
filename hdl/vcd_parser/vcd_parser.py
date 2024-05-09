import os
import sys
import io
import re
from typing import TextIO

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from vcd_signal import Signal, SignalStore


class VcdParser:
    def parse(self, vcd_file: TextIO) -> SignalStore:
        signals_store = SignalStore()
        with open(vcd_file) as file:
            self.set_ids(file, signals_store)
            self.load_values(file, signals_store)
            file.close()
        return signals_store

    def set_ids(self, file: TextIO, signals_store: SignalStore):
        upscope_str = r'\$scope (?P<type>\w+) (?P<name>\w+) \$end'
        downscope_str = r'\$upscope \$end'
        var_str = r'\$var (?P<type>\w+) (?P<width>\d+) (?P<id>\S+) (?P<name>\w+)( \[\d+:\d+\])? \$end'
        timescale_inline_str = r'\$timescale (?P<value>\d+)(?P<unit>\w+)'

        timescale_on_next = False

        scopes = []
        for line in file:
            var_match = re.match(var_str, line)
            if var_match:
                name = ".".join(scopes + [var_match.group('name')])
                id = var_match.group('id')
                type = var_match.group('type')
                width = int(var_match.group('width'))
                signals_store.signals[id] = Signal(name, id, type, width)
                signals_store.name_id_map[name] = id
            else:
                upscope_match = re.match(upscope_str, line)
                if upscope_match:
                    scopes.append(upscope_match.group('name'))
                else:
                    downscope_match = re.match(downscope_str, line)
                    if downscope_match:
                        scopes = scopes[:-1]
                    else:
                        timescale_inline_match = re.match(
                            timescale_inline_str, line)
                        if timescale_inline_match or timescale_on_next:
                            # update timescale
                            if timescale_on_next:
                                timescale_on_next = False
                                timescale_inline_match = re.match(
                                    r'\s*(?P<value>\d+)(?P<unit>\w+)', line)
                            signals_store.update_timescale(
                                int(timescale_inline_match.group('value')),
                                timescale_inline_match.group('unit'))
                        else:
                            if line.startswith("$timescale"):
                                timescale_on_next = True
                            else:
                                if line.startswith("$dumpvars"):
                                    return

    def load_values(self, file: TextIO, signals_store: SignalStore):
        timestamp = 0
        for line in file:
            if line.startswith('#'):
                timestamp = signals_store.get_time_scale() * int(line[1:])
                signals_store.set_max_time_stamp(
                    max(signals_store.get_max_time_stamp(), timestamp))
            else:
                match = re.match(r'[b]?(?P<value>([\d]+|x|z))[ ]?(?P<id>\S+)$',
                                 line)
                if match:
                    id = match.group('id')
                    value = match.group('value')
                    signals_store.signals[id].values.append((value, timestamp))
