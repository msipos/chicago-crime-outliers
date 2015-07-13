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
