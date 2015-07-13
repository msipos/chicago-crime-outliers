import numpy as np
import re

class UniquenessMapper:
    ''' Map a string into a unique ID (new IDs are assigned incrementally. '''
    def __init__(self):
        self.mapping = {}
        self.max_int = 0

    def get_id(self, str):
        if str in self.mapping:
            return self.mapping[str]
        else:
            self.max_int += 1
            self.mapping[str] = self.max_int
            return self.max_int

class WindowedHistogram:
    ''' Run a histogram in a sliding window (valid for integers). '''
    def __init__(self, window_size):
        self.window_size = window_size
        self.memory = np.zeros(window_size, dtype='int')
        self.memory_idx = 0
        self.histogram = {}
        self.histogram_total = 0

    def add(self, value):
        if self.histogram_total > self.window_size:
            old_value = self.memory[self.memory_idx]
            self.histogram[old_value] -= 1
        self.histogram_total += 1

        # Remember value in memory
        self.memory[self.memory_idx] = value
        self.memory_idx += 1
        if self.memory_idx >= self.window_size: self.memory_idx = 0

        if value not in self.histogram:
            self.histogram[value] = 0
        self.histogram[value] += 1

    def get_prop(self, value):
        total = self.histogram_total
        if total > self.window_size: total = self.window_size
        return float(self.histogram[value]) / total

    def debug(self):
        keys = sorted(self.histogram.keys())
        for key in keys:
            print key, self.get_prop(key)

date_re = re.compile('(..)/(..)/(....) (..):(..):(..) (..)')

def date_to_num(d):
    ''' Map ##/##/#### ##:##:## PM|AM into a [0... 1] floating point. '''
    result = date_re.match(d)
    num_hours = int(result.group(4))
    ampm = result.group(7)
    if num_hours == 12 and ampm == 'AM':
        num_hours = 0
    if ampm == 'PM' and num_hours < 12:
        num_hours += 12
    total = num_hours * 3600 + int(result.group(5)) * 60 + int(result.group(6))
    return float(total) / (24*3600)
