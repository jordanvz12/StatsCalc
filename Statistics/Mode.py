import collections
def mode(data):
    countItems = collections.Counter(data)
    return max(countItems)

