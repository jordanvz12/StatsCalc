import numpy

from Statistics.Median import median
def quartiles(data):
    secondQuartile = median(data)
    firstQuartile = numpy.percentile(data, 25)
    thirdQuartile = numpy.percentile(data, 75)
    return firstQuartile, secondQuartile, thirdQuartile
