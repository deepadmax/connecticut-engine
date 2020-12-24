# Implements a better range
# It's inclusive and possible to call in reverse

def brange(start, stop):
    step = 1 if stop > start else -1
    return range(start, stop + step, step)